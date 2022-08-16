# FE Death Counter
This tool is for streamers to keep track of characters lost in their Fire Emblem iron man run streams. This program was made for my AP Computer Science Principles exam, and I decided to publish it as I thought some people might get some use out of it. I'm still fairly new to python and this is the biggest project I've ever attempted to make with it, so my code is definitely not as clean and efficient as it could be.

## How to Use
This tool allows you to mark what characters have been lost in your run and will display them in a PNG named "output.png". You can add this PNG to OBS or whatever streaming software you use and it will update as you make changes.
### Marking Dead Characters
Click on a character to mark them as being dead. This will make them show on the output file. Click them again to undo this. You can change what game you are playing with the left and right arrows at the bottom of the config window. This will change the characters shown to the characters from that game.
### Image Size
Changing this value will change the size of the character's portraits on the output image.
### Background
You can change the color of the background by changing the RGB values at the bottom of the config window. The last value is the opacity. At 255, the image's background is completely opaque, and at 0 it's background will be transparent.
###Output Size
Changing this value will adjust the dimensions of the output file. The portraits of the characters will wrap to the next line to make sure that all of them fit onscreen.

## Other Information

### Plus/Minus Shortcut
When changing the image size, background dimensions or the RGB values, if you hold the control key, shift key or both at the same time you can increment them at larger amounts.

Control - 10

Shift - 50

Control + Shift - 100

### Adding More Games
You can add more games to this program if you are playing a romhack or another game that isn't included. To do so, simply make a new folder in the same directory as the config and display files. Add any images of characters you want to use into this folder. These will be displayed in alphabetical order in the config file. When you run the config file, you should be able to select the new folder you've created. A text file will be created in this folder that will store what characters you have marked as dead inside. Make sure the images used have equal width and height or else they will appear stretched when they are displayed.

## Credits
Big thanks to:

Both https://fireemblem.fandom.com/wiki/Fire_Emblem_Wiki and https://fireemblemwiki.org/wiki/Main_Page for providing the all the images of all characters in the series in recruitment order. Organizing them was made so much easier thanks to them!

My programming teacher, for inspiring me to create a project like this and being an amazing teacher.

Nintendo and Intelligent Systems for creating the Fire Emblem Series.
