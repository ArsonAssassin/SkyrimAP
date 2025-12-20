using Archipelago.Core;
using Archipelago.Core.MauiGUI;
using Archipelago.Core.MauiGUI.Models;
using Archipelago.Core.MauiGUI.ViewModels;
using Archipelago.Core.Models;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using Serilog;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using SkyrimAP.Models;
using Archipelago.Core.GameClients;

namespace SkyrimAP
{
    public partial class App : Application
    {
        static MainPageViewModel Context;
        public static ArchipelagoClient Client { get; set; }
        public static List<SkyrimItem> AllItems { get; set; }
        public static List<SkyrimQuest> AllQuests { get; set; }
        private static readonly object _lockObject = new object();
        private SkyrimTcpClient TcpSender { get; set; }
        public App()
        {
            InitializeComponent();

            Context = new MainPageViewModel();
            Context.ConnectClicked += Context_ConnectClicked;
            Context.CommandReceived += (e, a) =>
            {
                Client?.SendMessage(a.Command);
            };
            MainPage = new MainPage(Context);
            Context.ConnectButtonEnabled = true;
        }

        private async void Context_ConnectClicked(object? sender, ConnectClickedEventArgs e)
        {
            Context.ConnectButtonEnabled = false;
            Log.Logger.Information("Connecting...");
            if (Client != null)
            {
                Client.Connected -= OnConnected;
                Client.Disconnected -= OnDisconnected;
                Client.ItemReceived -= Client_ItemReceived;
                Client.MessageReceived -= Client_MessageReceived;
                Client.CancelMonitors();
            }
            GenericGameClient client = new GenericGameClient("SkyrimSE");
            var connected = client.Connect();
            if (!connected)
            {
                Log.Logger.Error("Skyrim not running, open Skyrim before connecting!");
                Context.ConnectButtonEnabled = true;
                return;
            }

            Client = new ArchipelagoClient(client);

            AllItems = Helpers.GetAllItems();
            AllQuests = Helpers.GetAllQuests();
            Client.Connected += OnConnected;
            Client.Disconnected += OnDisconnected;

            await Client.Connect(e.Host, "Skyrim");

            Client.ItemReceived += Client_ItemReceived;
            Client.MessageReceived += Client_MessageReceived;

            await Client.Login(e.Slot, !string.IsNullOrWhiteSpace(e.Password) ? e.Password : null);
            TcpSender = new SkyrimTcpClient();
            StartListener();
            InitializeQuests();
            Context.ConnectButtonEnabled = true;
        }
        private async Task StartListener()
        {
            var listener = new TcpListener(IPAddress.Loopback, 51234);
            listener.Start();
            Log.Logger.Information("Successfully started listener");
            Log.Logger.Information("Listening on localhost:51234...");

            while (true)
            {
                Log.Logger.Information("Waiting for connection...");
                using (var client = await listener.AcceptTcpClientAsync())
                {
                    Log.Logger.Information("Client connected!");
                    using (var stream = client.GetStream())
                    using (var reader = new StreamReader(stream, Encoding.UTF8))
                    {
                        string? message = await reader.ReadLineAsync();
                        if (message != null)
                        {
                            Log.Logger.Information($"Received: {message}");
                            var skyMessage = JsonSerializer.Deserialize<SkyrimMessage>(message);

                            switch (skyMessage.type)
                            {
                                case "quest_complete":
                                    var questId = skyMessage.data;
                                    var quest = AllQuests.First(x => x.Id == questId);
                                    var location = new Archipelago.Core.Models.Location() { Id = (int)quest.ApId };
                                    Client.SendLocation(location);
                                    break;
                                case "location_change":
                                    Log.Logger.Information("Player moved to {location}", skyMessage.data);
                                    break;
                                case "position_update":
                                    Log.Logger.Verbose("Updating Player co-ords");
                                    break;
                                default:
                                    Log.Warning("Unknown message type received");
                                    break;
                            }

                        }
                    }
                }
            }
        }

        private void InitializeQuests()
        {
            Log.Logger.Information($"Initializing Quest Listener");
            var idList = AllQuests.Select(x => x.Id).ToList();
            Log.Logger.Information($"{idList.Count} quests found");
            TcpSender.SendMessageAsync(new SkyrimMessage() { type = "init_quests", data = JsonSerializer.Serialize(idList) });
        }
        private void Client_MessageReceived(object? sender, Archipelago.Core.Models.MessageReceivedEventArgs e)
        {
            if (e.Message.Parts.Any(x => x.Text == "[Hint]: "))
            {
                LogHint(e.Message);
            }
            Log.Logger.Information(JsonSerializer.Serialize(e.Message));
        }
        private void Client_ItemReceived(object? sender, ItemReceivedEventArgs e)
        {
            LogItem(e.Item);
            var itemId = e.Item.Id;
            var itemToReceive = AllItems.FirstOrDefault(x => x.ApId == itemId);

            TcpSender.SendMessageAsync(new SkyrimMessage() { type = "receive_item", data = $"{itemToReceive.Id},1" });

        }
        private static void LogItem(Item item)
        {
            var messageToLog = new LogListItem(new List<TextSpan>()
            {
                new TextSpan(){Text = $"[{item.Id.ToString()}] -", TextColor = Color.FromRgb(255, 255, 255)},
                new TextSpan(){Text = $"{item.Name}", TextColor = Color.FromRgb(200, 255, 200)},
            });
            lock (_lockObject)
            {
                Application.Current.Dispatcher.DispatchAsync(() =>
                {
                    Context.ItemList.Add(messageToLog);
                });
            }
        }
        private static void LogHint(LogMessage message)
        {
            var newMessage = message.Parts.Select(x => x.Text);

            if (Context.HintList.Any(x => x.TextSpans.Select(y => y.Text) == newMessage))
            {
                return; //Hint already in list
            }
            List<TextSpan> spans = new List<TextSpan>();
            foreach (var part in message.Parts)
            {
                spans.Add(new TextSpan() { Text = part.Text, TextColor = Color.FromRgb(part.Color.R, part.Color.G, part.Color.B) });
            }
            lock (_lockObject)
            {
                Application.Current.Dispatcher.DispatchAsync(() =>
                {
                    Context.HintList.Add(new LogListItem(spans));
                });
            }
        }
        private static void OnConnected(object sender, EventArgs args)
        {
            Log.Logger.Information("Connected to Archipelago");
            Log.Logger.Information($"Playing {Client.CurrentSession.ConnectionInfo.Game} as {Client.CurrentSession.Players.GetPlayerName(Client.CurrentSession.ConnectionInfo.Slot)}");
        }

        private static void OnDisconnected(object sender, EventArgs args)
        {
            Log.Logger.Information("Disconnected from Archipelago");
        }
        protected override Window CreateWindow(IActivationState activationState)
        {
            var window = base.CreateWindow(activationState);
            if (DeviceInfo.Current.Platform == DevicePlatform.WinUI)
            {
                window.Title = "SkyrimAP - Skyrim Archipelago Randomizer";

            }
            window.Width = 600;

            return window;
        }
    }
}
