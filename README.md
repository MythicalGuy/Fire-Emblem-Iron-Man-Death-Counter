#FE Death Counter
This tool is for streamers to keep track of characters lost in their Fire Emblem iron man run streams.

##How to Use
This tool uses two different program files to function. The "display" file is what you will show to your viewers. It displays the characters that you have marked as being dead. The "config" file is what you will use to configure what is shown on the display window, such as what characters are shown and the background color. Both of these files are able to be running at the same time as the other.

##Config File
The config file is used to configure display of the display file.
###Marking Dead Characters
Click on a character to mark them as being dead. This will make them show on the display file. Click them again to undo this. You can change what game you are playing with the left and right arrows at the bottom of the config window. This will change the characters shown to the characters from that game.
###Image Size
Changing this value will change the size of the character's portraits on the display file.
###Background
You can change the color of the background by changing the RGB values at the bottom of the config window. Alternatively, you can check the "Use BG img?" option to use a custom background for the window. You can change the default one by replacing the "bg.png" file with your own image with the same file name.

##Display File
This file simply shows what characters have been killed and can be changed with the config file.
###Wrapping
Portaits will wrap to the next line if they will not fit fully on screen. You can resize this window or change the portrait's size in the config file to change how many characters are shown in each row.

##Other Information

###Plus/Minus Shortcut
When changing the size or the RGB values, if you hold the control key, shift key or both at the same time you can increment them at larger amounts.
Control - 10
Shift - 50
Control + Shift - 100

###Chroma Keying
Recording software like OBS and Streamlabs have options to chroma key out certain colors and make them transparent. It's possible to do this with the background of the display window. However, due to how colorful Fire Emblem characters are finding a color which no character uses is difficult.

GBA Games - (161,199,150)
