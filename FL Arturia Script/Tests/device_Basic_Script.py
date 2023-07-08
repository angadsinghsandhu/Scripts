

Button_Previous = 110
Button_Next = 0x6F      # this is equavalent to decimalvalue of 111

def OnMidiMsg(event):
    event.handled = False       # if the script does not recognize the data 
    # Print Data (goes to interpreter Tab)
    print("MIDI ID : ", event.midiId, "DATA 1 : ",  event.data1, "DATA 2 : ", event.data2)

    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data1 == Button_Previous:
            print("Previous Button Pressed")
            ui.previous()       # Send `Previous` Command to UI
            event.handled = True
        elif event.data1 == Button_Next:
            print("Next Button Pressed")
            ui.next()           # Send `next` Command to UI
            event.handled = True