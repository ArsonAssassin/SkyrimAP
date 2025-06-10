Scriptname ArchipelagoManager extends Quest

Actor Property PlayerRef Auto
Faction Property CurrentFollowerFaction Auto
Location Property LastLocation Auto Hidden
Bool Property IsInitialized Auto Hidden

string[] TrackedQuestIDs


Event OnItemAdded(Form inputForm, int number, ObjectReference ItemReference, ObjectReference SourceContainer)
	APLog("Item added to inventory")
	APLog(inputForm.GetFormID() + ": " + inputForm.GetName())
EndEvent

String storageKey = "Archipelago_LastPlayerLevel"

; Import the native function from our SKSE plugin
Function SendJSON(String jsonString) global native

; Shared initialization function
Function InitializeScript()
    APLog("Initializing")
    
    If !IsInitialized
        RegisterForSingleUpdate(1.0)
        APLog("Registered for update")
        
        If PlayerRef
            PlayerRef.AddToFaction(CurrentFollowerFaction)
            RegisterForTrackedStatsEvent()
            LastLocation = None
            IsInitialized = true
           APLog("Initialized Successfully")
        Else
            APLog("PlayerRef is null!")
        EndIf
    Else
       APLog("Archipelago Manager: Already initialized, restarting update cycle")
       RegisterForSingleUpdate(1.0)
    EndIf
EndFunction

Function SetTrackedQuests(string[] questIds)
	TrackedQuestIds = questIds
EndFunction



Function TriggerDeathlink()
	APLog("Deathlink Received")
EndFunction

Function ReceiveItem(string itemName, int skyrimId, int quantity)
	APLog("Received: " + quantity + "x " + itemName + " (ID: " + skyrimId + ")")
	Form itemForm = Game.GetForm(skyrimId)
   	if itemForm
       	Game.GetPlayer().AddItem(itemForm, quantity)
       	Debug.Notification("Added " + quantity + "x " + itemName + " to inventory")
    else
       	Debug.Notification("Could not find item with ID: " + skyrimId)
    endif
EndFunction


Event OnInit()
    APLog("New Game Start")
    InitializeScript()
EndEvent

Event OnPlayerLoadGame()
    APLog(" Save Game Loaded")
    InitializeScript()
EndEvent

Event OnUpdate()
    Location currentLoc = Game.GetPlayer().GetCurrentLocation()
    
    If currentLoc
        If !LastLocation || currentLoc != LastLocation
            String json = "{\"type\":\"location_change\",\"data\":\"" + currentLoc + "\"}"
            APLog("Sending location change - " + currentLoc)
            APLog(" JSON - " + json)
            SendJSON(json)
            LastLocation = currentLoc
        EndIf
    EndIf
    CheckQuestStatus()
    RegisterForSingleUpdate(5.0)
EndEvent

Function CheckQuestStatus()
	int index = 0
	while index < TrackedQuestIDs.length
		Quest questForm = Game.GetFormFromFile(0, TrackedQuestIDs[index]) as Quest
        if questForm != None
            if questForm.IsCompleted()
				OnQuestComplete(questForm)
			endif
        else
            APLog("Could not find quest: " + TrackedQuestIDs[index])
        endif
		index+=1
	endwhile
EndFunction

Event OnQuestComplete(Quest akQuest)
    String json = "{\"type\":\"quest_complete\",\"data\":\"" + akQuest.GetFormID() + "\"}"
    APLog("Quest Complete - " + akQuest.GetFormID())
    APLog("JSON - " + json)
    SendJSON(json)
EndEvent

Function APLog(string data)
	Debug.Notification("Archipelago Manager: " + data)
	Debug.Trace("Archipelago Manager: " + data)
EndFunction