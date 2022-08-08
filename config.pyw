#This file configures the what display file shows.
import os, pygame

pygame.init()
directory = "" #What folder the program will use images from
files = [] #The files in said folder

#default settings
mainSize = 100
choice = 0
color = [161,199,150]

bgCheck = False

#loading images
plus = pygame.image.load("plus.png")
minus = pygame.image.load("minus.png")
left = pygame.image.load("left.png")
right = pygame.image.load("right.png")
off = pygame.image.load("off.png")
on = pygame.image.load('on.png')

icon = pygame.image.load('icon.ico')
pygame.display.set_icon(icon)

smallplus = pygame.transform.scale(plus, (15,15)) #for changing BG color
smallminus = pygame.transform.scale(minus, (15,15))

#Lists all the folders in the folder the program is located in.
for root, dirnames, filenames in os.walk('.'): #Taken from https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
  if len(dirnames) > 0:
    files = dirnames.copy()
    break

class Char: #This class is used to represent each character.
  def __init__(self, img, name):
    self.img = img #The image of the character
    self.selected = False #Whether or not the user has marked the character as dead.
    self.collide = 0 #Set to 0 at first, later and used to check if the user clicked the image.
    self.name =  name #File name of the character

screenx = 400
screeny = 850

#Used when the program needs to update the settings file.
def writeSettings(x):
  x.write("size: " + str(mainSize))
  x.write("\n")
  x.write("game: " + str(choice))
  x.write("\n")
  x.write("bgred: " + str(color[0]))
  x.write("\n")
  x.write("bggreen: " + str(color[1]))
  x.write("\n")
  x.write("bgblue: " + str(color[2]))
  x.write("\n")
  if bgCheck == True:
    x.write("bg: true")
  else:
    x.write("bg: false")
  x.write("\n")

def changeSettings(): #Loads the settings from the settings file.
  while True:
    try:
      settingsFile = open('settings.txt')
      settings = settingsFile.readlines()
      settingsFile.close()
      s = settings[0].split(":")[1]
      g = settings[1].split(":")[1]
      r = settings[2].split(":")[1]
      gr = settings[3].split(":")[1]
      b = settings[4].split(":")[1]
      bg = settings[5].split(":")[1]
      break
    except IndexError:
      with open('settings.txt', 'w') as f: #resets to default settings if the text file is formatted incorrectly
        writeSettings(f)

  s = s.strip(" ") #Getting rid of unecessary characters
  g = g.strip(" ")
  r = r.strip(" ")
  gr = gr.strip(" ")
  b = b.strip(" ")
  bg = bg.strip(" ")

  s = s.strip("\n")
  g = g.strip("\n")
  r = r.strip("\n")
  gr = gr.strip("\n")
  b = b.strip("\n")
  bg = bg.strip("\n")

  s = int(s)
  g = int(g)
  r = int(r)
  gr = int(gr)
  b = int(b)

  if bg.lower() == "true":
    returnBg = True
  else:
    returnBg = False

  return s,g, [r,gr,b], returnBg

mainSize, choice, color, bgCheck = changeSettings()

directory = files[choice] #Opens the folder of the game that the user has specified.

size = 50 #Size of the characters on this window.
row = screenx / size #Amount of images that can fit on one row

rip = pygame.image.load("x.png")
rip = pygame.transform.scale(rip, (size,size))

def newGame(d): #This function is used whenever the user wants to switch to a different game folder. It opens the appropriate directory and puts the contents into a list.
  dead = []
  charimg = []
  s = []
  char = os.listdir(d)
  try:
    deadlist = open(d+'/dead.txt',"r").readlines() #List of the dead characters.
  except FileNotFoundError: #Creates dead.txt if it doesn't exist in the current folder.
    deadlist = open(d+'/dead.txt',"w+").readlines()
  for i in range(len(deadlist)): #Goes through deadlist and removes the new line characters.
    deadlist[i] = deadlist[i].rstrip("\n")

  for i in char: #Removes any files in the directory that aren't png or jpg files from the list.
    if not i.endswith(".png") and not i.endswith(".jpg"):
      char.remove(i)

  z = 0 #Represents the row number in the clist array.
  clist = [[]]

  for i in range(len(char)): #Converts the char list into a 2D array called clist.
    if i % row == 0 and i != 0: 
      z += 1
      clist.append([])
    clist[z].append(char[i])

  for j in range(len(clist)): #Converts the clist into a 2D array of instances of the Char class.
    charimg.append([]) #Charimg is a 2D array of instances of the "Char" class that will store information about them, like if they are dead or not and their image.
    for i in range(len(clist[j])):
      x = Char(pygame.image.load(d+"/"+clist[j][i]), clist[j][i]) #Creates an instance of the Char class with the character's file name and it's path.
      if x.name in deadlist: #Checks if the character's file name is in deadlist, and if so adds the instance to a new list called dead.
        dead.append(x)
      x.img = pygame.transform.scale(x.img, (size,size)) #Resizes the character's image to the proper size.
      charimg[j].append(x) #Adds the instance for the character to the charimg list.
  for i in char: #Goes through the list of characters and the list of dead ones. Any character that is in the list of dead ones is added to the list of selected characters and marked as selected.
    for j in dead:
      if j.name == i:
        s.append(j.name)
        j.selected = True
  return char, clist, charimg, dead, s

characters, characterList, characterImages, characterDead, selected = newGame(directory)
screen = pygame.display.set_mode((screenx,screeny))

pygame.display.set_caption("Counter Config")

done = False

collidelist = []

font = pygame.font.SysFont("Times New Roman", 30, False, False)

plusClick = screen.blit(plus, (50,540))
minusClick = screen.blit(minus, (100,540))
leftClick = screen.blit(left, (150,460))
rightClick = screen.blit(right, (200,460))
toggleClick = screen.blit(on, (275,740))

#Used to check if these keys are being held by the user.
controlHeld = False
shiftHeld = False

#Used for the plus and minus icons.
def plusMinus(x,add,min,max):
  if controlHeld and shiftHeld:
    if add:
      x += 100
    else:
      x -= 100
  elif controlHeld:
    if add:
      x += 10
    else:
      x -= 10
  elif shiftHeld:
    if add:
      x += 50 
    else:
      x -= 50
  else: 
    if add:
      x += 1
    else:
      x -= 1
  if x < min:
    x = min
  if x > max:
    x = max
  return x

while not done: 
  myPos = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True          
    elif event.type == pygame.MOUSEBUTTONDOWN: 
      if event.button == 1: #Checks what the user clicked.
        #Plus/Minus Clicks
        if plusClick.collidepoint(myPos):
          mainSize = plusMinus(mainSize,True,1,1000)
          with open('settings.txt', 'w') as f: #Updates the settings file
            #taken from https://www.pythontutorial.net/python-basics/python-write-text-file/
            writeSettings(f)
        if minusClick.collidepoint(myPos):
          mainSize = plusMinus(mainSize,False,1,1000)
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        if redplus.collidepoint(myPos):
          color[0] = plusMinus(color[0],True,0,255)
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        if redminus.collidepoint(myPos):
          color[0] = plusMinus(color[0],False,0,255)
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        if blueplus.collidepoint(myPos):
          color[1] = plusMinus(color[1],True,0,255)
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        if blueminus.collidepoint(myPos):
          color[1] = plusMinus(color[1],False,0,255)
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        if greenplus.collidepoint(myPos):
          color[2] = plusMinus(color[2],True,0,255)
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        if greenminus.collidepoint(myPos):
          color[2] = plusMinus(color[2],False,0,255)
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        #Arrow Clicks
        if leftClick.collidepoint(myPos): #Goes to the previous directory in the folder.
          choice -= 1
          if choice < 0: #If the index is too low, and if so loops back to the end of the list.
            choice = len(files) - 1
          directory = files[choice] #Changes the directory that the program is taking the characters from
          characters, characterList, characterImages, characterDead, selected = newGame(directory) #Recreates the lists the program uses to now have the characters from the specified game.
          with open('settings.txt', 'w') as f: 
            writeSettings(f)
        if rightClick.collidepoint(myPos): #Goes to the next directory in the folder.
          choice += 1
          if choice > len(files) - 1: #Checks if the index is at the end of the list, and if so loops to the beginning of the list.
            choice = 0
          directory = files[choice] #Changes the directory that the program is taking the characters from
          characters, characterList, characterImages, characterDead, selected = newGame(directory) #Recreates the lists the program uses to now have the characters from the specified game.
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        if toggleClick.collidepoint(myPos): #Toggles if the bg.png image should be used as the background.
          if bgCheck == True:
            bgCheck = False
          else:
            bgCheck = True
          with open('settings.txt', 'w') as f:
            writeSettings(f)
        for i in collidelist: #Checks if the user has clicked on a character.
          if i.collide.collidepoint(myPos) and i.selected == False: #Marks the character as dead if it isn't already
            i.selected = True
            selected.append(i.name)
            #Taken from https://www.pythontutorial.net/python-basics/python-write-text-file/
            with open(directory+'/dead.txt', 'w') as f: #Retwrites the list of dead characters with the updated information.
              for line in selected:
                  f.write(line)
                  f.write('\n')
          elif i.collide.collidepoint(myPos) and i.selected == True: #Unmarks the character as dead
            i.selected = False
            selected.remove(i.name)
            with open(directory+'/dead.txt', 'w') as f: #Retwrites the list of dead characters with the updated information.
              for line in selected:
                  f.write(line)
                  f.write('\n')

  collidelist = [] #Clears the list of the current locations of characters so that it can be updated later.
  screen.fill("black")

  keys = pygame.key.get_pressed()  #https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down
  if keys[pygame.K_LCTRL]: #If the key is being held, it sets the relevant variable to True. Otherwise, it sets it to False.
    controlHeld = True
  else:
    controlHeld = False
  if keys[pygame.K_LSHIFT]:
    shiftHeld = True
  else:
    shiftHeld = False

  #Text
  sizeText = font.render("Image Size: " + str(mainSize), True, "white")
  gameText = font.render("Game: " + directory, True, "white")
  bgText = font.render("Use BG img?", True, "white")
  colorText  = font.render("BG Color:", True, "white")
  redText  = font.render(str(color[0]), True, "red")
  blueText  = font.render(str(color[1]), True, "blue")
  greenText  = font.render(str(color[2]), True, "green")

  #Displaying text and images

  screen.blit(sizeText, (0,700))
  screen.blit(gameText, (0,650))
  screen.blit(bgText, (215,700))
  screen.blit(colorText, (0,770))
  screen.blit(redText, (150,770))
  screen.blit(blueText, (225,770))
  screen.blit(greenText, (300,770))

  plusClick = screen.blit(plus, (100,740))
  minusClick = screen.blit(minus, (50,740))
  leftClick = screen.blit(left, (200,660))
  rightClick = screen.blit(right, (250,660))

  redminus = screen.blit(smallminus, (150,800))
  redplus = screen.blit(smallplus, (180,800))
  
  blueminus = screen.blit(smallminus, (225,800))
  blueplus = screen.blit(smallplus, (255,800))
  
  greenminus = screen.blit(smallminus, (300,800))
  greenplus = screen.blit(smallplus, (330,800))
  
  
  if bgCheck == True:
    toggleClick = screen.blit(on, (275,740))
  else:
    toggleClick = screen.blit(off, (275,740))

#Goes through the list of characters and displays them as they are organized in the 2D array..
  for j in range(len(characterList)):
    for i in range(len(characterList[j])):
      characterImages[j][i].collide = screen.blit(characterImages[j][i].img,[size*i,j*size]) #This sets the collide attribute of the current character to the character's location and displays them there
      collidelist.append(characterImages[j][i])
      if characterImages[j][i].selected == True: #Displays an "x" over any character who has been marked as dead.
        screen.blit(rip,[size*i,j*size])
  
  pygame.display.flip()
pygame.quit()