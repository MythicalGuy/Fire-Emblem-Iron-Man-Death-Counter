# FE Death Counter
This tool is for streamers to keep track of characters lost in their Fire Emblem iron man run streams. This program was made for my AP Computer Science Principles exam, and I decided to publish it as I thought some people might get some use out of it. I'm still fairly new to python and this is the biggest project I've ever attempted to make with it, so my code is definitely not as clean and efficient as it could be.

## How to Use
This tool uses two different program files to function. The "display" file is what you will show to your viewers. It displays the characters that you have marked as being dead. The "config" file is what you will use to configure what is shown on the display window, such as what characters are shown and the background color. Both of these files are intended to be running at the same time as the other.

## Config File
The config file is used to configure display of the display file.
### Marking Dead Characters
Click on a character to mark them as being dead. This will make them show on the display file. Click them again to undo this. You can change what game you are playing with the left and right arrows at the bottom of the config window. This will change the characters shown to the characters from that game.
### Image Size
Changing this value will change the size of the character's portraits on the display file.
### Background
You can change the color of the background by changing the RGB values at the bottom of the config window. Alternatively, you can check the "Use BG img?" option to use a custom background for the window. You can change the default one by replacing the "bg.png" file with your own image with the same file name.

## Display File
This file simply shows what characters have been killed and can be changed with the config file.
### Wrapping
Portaits will wrap to the next line if they will not fit fully on screen. You can resize this window or change the portrait's size in the config file to change how many characters are shown in each row.

## Other Information

### Plus/Minus Shortcut
When changing the image size or the RGB values, if you hold the control key, shift key or both at the same time you can increment them at larger amounts.

Control - 10

Shift - 50

Control + Shift - 100

### Transparent Background
If you want the background of the death counter to show as transparent while you're streaming, you can use the "Save to PNG?" option. This will save a PNG of the display screen with just the characters in the folder where the program is located. It should update whenever you change the display, such as by adding new characters or changing the size of the images. Instead of recording the display window, instead just show the "transparent.png" image.

### Adding More Games
You can add more games to this program if you are playing a romhack or another game that isn't included. To do so, simply make a new folder in the same directory as the config and display files. Add any images of characters you want to use into this folder. These will be displayed in alphabetical order in the config file. When you run the config file, you should be able to select the new folder you've created. A text file will be created in this folder that will store what characters you have marked as dead inside. Make sure the images used have equal width and height or else they will appear stretched when they are displayed.

## Credits
Big thanks to:

Both https://fireemblem.fandom.com/wiki/Fire_Emblem_Wiki and https://fireemblemwiki.org/wiki/Main_Page for providing the all the images of all characters in the series in recruitment order. Organizing them was made so much easier thanks to them!

My programming teacher, for inspiring me to create a project like this and being an amazing teacher.

Nintendo and Intelligent Systems for creating the Fire Emblem Series.
