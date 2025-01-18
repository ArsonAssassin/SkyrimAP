using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace SkyrimAP
{
    public class SkyrimTcpClient
    {
        private string _host;
        private int _port;

        public SkyrimTcpClient(string host = "127.0.0.1", int port = 54321)
        {
            _host = host;
            _port = port;
        }
        public async Task SendMessageAsync(string message)
        {
            try
            {
                using (TcpClient client = new TcpClient())
                {
                    // Connect to the server
                    await client.ConnectAsync(_host, _port);

                    // Get the network stream
                    using (NetworkStream stream = client.GetStream())
                    {
                        // Convert message to bytes
                        byte[] data = Encoding.UTF8.GetBytes(message + "\n");

                        // Send the message
                        await stream.WriteAsync(data, 0, data.Length);
                    }
                }
                Console.WriteLine($"Message sent: {message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error sending message: {ex.Message}");
            }
        }
        public async Task SendMessageAsync(SkyrimMessage message)
        {
            var jsonString = JsonSerializer.Serialize(message);
            await SendMessageAsync(jsonString);
        }
    }
}
