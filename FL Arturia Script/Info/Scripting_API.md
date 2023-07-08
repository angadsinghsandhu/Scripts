# FL Studio Scripting Tutorial

This has been taken from : [Midi Scripting API Reference](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm?_ga=2.46935143.1945153060.1628335138-780936187.1628335138)

- **Script hierarchy** - You only need to edit what you want to change everything else is handled automatically

---

### *Script Locations and File Names*

**Script files** - Scripted device files are located in the User data folder under ... `Documents\Image-Line\FL Studio\Settings\Hardware\devicename\device_devicename.py.`

**Script folder naming** - The sub folder `devicename` is arbitrary and can be anything you like. Normally you would use the name of the MIDI hardware you are scripting for.

**The controller name** - Shown in the MIDI Settings > Controller type menu is defined on first line of 'device_devicename.py' script file, e.g. #name=devicename. This will appear in the device list as `devicename (user)`. 

The (user) suffix is to distinguish your device scripts from installed factory scripts.

---

### *Getting Started Tutorials*

**Create a folder** - Inside your FL Studio User data folder, usually '...Documents\Image-Line\FL Studio\Settings\Hardware\YourScriptSubFolder', Create a sub folder to store your script. e.g. `...Settings\Hardware\Arturia`

**Add .py fIle** - In the 'YourScriptSubFolder' folder, create a plain python file 'device_YourScriptName.py'.

---

### *Edit your Script*

Here we now add our personal script to our controller type to activate it

then, go to `VIEW > Sript Output > FL STUDIO FIRE (or the name of your script) > EDIT SCRIPT` to edit your script file

---

### *Look for incomming MIDI Data*

pressing puttons on our MIDI creates output log i the `FL STUDIO FIRE (or the name of your script)` tab.

- Now we identify the kind of Data that is sent by the MIDI when we press a button to later assign it to some function.
- The best way to find the incomming MIDI Data is to go to `OPTIONS > Debugging Log` and start pressing buttons to see log show up on screen. 
- The output might be `Hex` or `Deimal` values.
- we can look at [Expanded MIDI 1.0 Messages List (Status Bytes)](https://www.midi.org/specifications-old/item/table-2-expanded-messages-list-status-bytes/) to see what all these Hex and Deciml values actualy mean.
- Buttons are secifiesd as `Control Change`, Keyboad Noes are specified as `Note On/Off`

---

### *Imcommind Data Types*

**Notes** (Keys and Pads) : the 3 hex balues depict [data type, note value, velocity] respectively.

**Control Change** (Knobs and Sliders) : the 3 hex balues depict [data type, note index, velocity] respectively.

In code, these 3 data values are depicted as (event.midiId, event.data1, event.data2) respectively.


---

### *Setting up Script*

we definr important variable names as `Button _Previous` and `Button_Next`