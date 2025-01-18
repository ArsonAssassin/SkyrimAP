Scriptname ArchipelagoManager extends Quest

Actor Property PlayerRef Auto
Faction Property CurrentFollowerFaction Auto
Location Property LastLocation Auto Hidden
Bool Property IsInitialized Auto Hidden
Keyword Property CheeseKeyword Auto

; Import the native function from our SKSE plugin
Function SendJSON(String jsonString) global native

; Shared initialization function
Function InitializeScript()
    Debug.Notification("Archipelago Manager: Initializing")
    Debug.Trace("Archipelago Manager: Initializing")
    
    If !IsInitialized
        RegisterForSingleUpdate(1.0)
        Debug.Notification("Archipelago Manager: Registered for update")
        Debug.Trace("Archipelago Manager: Registered for update")
        
        If PlayerRef
            PlayerRef.AddToFaction(CurrentFollowerFaction)
            RegisterForTrackedStatsEvent()
            LastLocation = None
            IsInitialized = true
            Debug.Notification("Archipelago Manager: Initialized Successfully")
            Debug.Trace("Archipelago Manager: Initialized Successfully")
        Else
            Debug.Notification("Archipelago Manager: PlayerRef is null!")
            Debug.Trace("Archipelago Manager: PlayerRef is null!")
        EndIf
    Else
        Debug.Notification("Archipelago Manager: Already initialized, restarting update cycle")
        Debug.Trace("Archipelago Manager: Already initialized, restarting update cycle")
        RegisterForSingleUpdate(1.0)
    EndIf
EndFunction

Function ReceiveCommand(string jsonString)
	Debug.Notification("Archipelago Manager: Message Received- " + jsonString)
EndFunction

int function CountCheese()
    ; Declare an array to hold the items
    Form[] specificItems = new Form[6]
    
    ; Get the forms from the form IDs
    specificItems[0] = Game.GetForm(0x00064B31)
    specificItems[1] = Game.GetForm(0x00064B32)
    specificItems[2] = Game.GetForm(0x00064B33)
    specificItems[3] = Game.GetForm(0x00064B34)
    specificItems[4] = Game.GetForm(0x00064B35)
    specificItems[5] = Game.GetForm(0x00064B36)
    
    ; Initialize total count
    int totalCount = 0
    
    ; Loop through the items and sum the item counts
    int i = 0
    while i < specificItems.Length
        if specificItems[i] != None
            totalCount += Game.GetPlayer().GetItemCount(specificItems[i])
        endif
        i += 1
    endwhile
    
    ; Optional: Debug notification to verify
    Debug.Notification("Total items: " + totalCount)
    
    return totalCount
EndFunction

Event OnInit()
    Debug.Notification("Archipelago Manager: New Game Start")
    Debug.Trace("Archipelago Manager: New Game Start")
    InitializeScript()
EndEvent

Event OnPlayerLoadGame()
    Debug.Notification("Archipelago Manager: Save Game Loaded")
    Debug.Trace("Archipelago Manager: Save Game Loaded")
    InitializeScript()
EndEvent

Event OnUpdate()
    Location currentLoc = Game.GetPlayer().GetCurrentLocation()
	int cheeseCount = CountCheese()
    If (cheeseCount == 0) 
		Debug.Notification("Player has no cheese")
	Else
		Debug.Notification("Player has " + cheeseCount + " cheese")
		SendJSON("{\"type\":\"cheese_update\",\"data\":\"" + "Player has " + cheeseCount + " cheese" + "\"}")
	EndIf
    If currentLoc
        If !LastLocation || currentLoc != LastLocation
            String json = "{\"type\":\"location_change\",\"data\":\"" + currentLoc + "\"}"
            Debug.Notification("Archipelago Manager: Sending location change - " + currentLoc)
            Debug.Trace("Archipelago Manager: Sending location change - " + currentLoc)
            Debug.Trace("Archipelago Manager: JSON - " + json)
            SendJSON(json)
            LastLocation = currentLoc
        EndIf
    EndIf
    
    RegisterForSingleUpdate(5.0)
EndEvent

Event OnQuestComplete(Quest akQuest)
    String json = "{\"type\":\"quest_complete\",\"data\":\"" + akQuest.GetFormID() + "\"}"
    Debug.Notification("Archipelago Manager: Quest Complete - " + akQuest.GetFormID())
    Debug.Trace("Archipelago Manager: Quest Complete - " + akQuest.GetFormID())
    Debug.Trace("Archipelago Manager: JSON - " + json)
    SendJSON(json)
EndEvent