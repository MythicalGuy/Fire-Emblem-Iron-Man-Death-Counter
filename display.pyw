import os, pygame
from pygame.locals import * #From https://stackoverflow.com/questions/34910086/pygame-how-do-i-resize-a-surface-and-keep-all-objects-within-proportionate-to-t

directory = ""
files = []
 
choice = 0
 
background = pygame.image.load("bg.png")

#Taken from https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
for root, dirnames, filenames in os.walk('.'):
  if len(dirnames) > 0:
    files = dirnames.copy()
    break
 
def rewrite(): #This function updates the list of dead characters to the ones specified in the directory's dead.txt file.
  old = open(directory +'/dead.txt').readlines()
  new = old
  for i in range(len(new)):
    new[i] = new[i].rstrip("\n")
  return old, new
settings = open('settings.txt').readlines()
 
def changeSettings(): #This function updates the settings to the new ones specified in settings.txt
  while True:
    try:
      readSettings = open('settings.txt').readlines()
      print(readSettings)
      s = readSettings[0].split(":")[1]
      g = readSettings[1].split(":")[1]
      r = readSettings[2].split(":")[1]
      gr = readSettings[3].split(":")[1]
      b = readSettings[4].split(":")[1]
      bg = readSettings[5].split(":")[1]
      break
    except IndexError: #Makes sure that the program doesn't try to read the file while it is still being written to.
      print(readSettings)
      print("retrying")
      continue

  s = s.strip(" ")
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

  print(s)
  print(g)
  print(r)
  print(gr)
  print(b)
  print(bg)

  if bg.lower() == "true":
    returnBg = True
  else:
    returnBg = False

  return readSettings, s, g, (r,gr,b), returnBg
 
color = (0,0,0)

settings, size, choice, color, bgCheck = changeSettings() #Updates the settings related to the settings file.
directory = files[choice] #Sets the correct directory
deadold = []
deadnew = []
 
two_d = [[]]
 
screenx = 400
screeny = 400

 
deadimg = []

def screenChange(x): #Re-organizes the characters when the size of the screen is changed.
  row = int(x/size) #How many characters fit in one row
 
  j = 0

  while("" in deadnew) :
    deadnew.remove("")

  for i in range(len(deadnew)): #Used to display the dead characters. If there are too many in one row, it goes to the next row.
    while True:
      try:
        if i % row == 0 and i != 0:
          j += 1
          two_d.append([])
        two_d[j].append(deadnew[i])
        break
      except ZeroDivisionError: #If the window is too small to fit one image, the program only allows one character in each row
        row = 1

  for j in range(len(two_d)): #Makes another list of the properly sized images.
    deadimg.append([])
    for i in range(len(two_d[j])):
      x = pygame.image.load(directory+"/"+two_d[j][i])
      x = pygame.transform.scale(x, (size,size))
      deadimg[j].append(x)
 
deadold, deadnew = rewrite() #Returns the dead characters.
screenChange(screenx) #Makes the images fit on the current screen size.
 
characters = os.listdir(directory)
 
for i in characters:
  if not i.endswith(".png") and not i.endswith(".jpg"): #Removes any files that aren't images from the characters list.
    characters.remove(i)
 
pygame.init()
screen = pygame.display.set_mode((screenx,screeny),HWSURFACE|DOUBLEBUF|RESIZABLE) #From https://stackoverflow.com/questions/34910086/pygame-how-do-i-resize-a-surface-and-keep-all-objects-within-proportionate-to-t
 
pygame.display.set_caption("Death Counter")
 
done = False

bgScreen = screen.copy()
 
icon = pygame.image.load('icon2.ico')
pygame.display.set_icon(icon)

while not done:
  myPos = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True          
    elif event.type == VIDEORESIZE: #https://stackoverflow.com/questions/34910086/pygame-how-do-i-resize-a-surface-and-keep-all-objects-within-proportionate-to-t
      two_d = [[]]
      deadimg = []
      screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
      screenx, screeny = pygame.display.get_surface().get_size()
      screenChange(screenx)
           
  screen.fill(color)
  if bgCheck: #Shows the custom background if the box is checked in the config program.
    screen.blit(pygame.transform.scale(bgScreen, screen.get_rect().size), (0, 0))
  bgScreen.blit(background,[0,0])
  if settings != open('settings.txt').readlines(): #Checks if the settings file has been changed
    settings, size, choice, color, bgCheck = changeSettings()
    directory = files[choice]
 
  if deadold != open(directory+'/dead.txt').readlines(): #Checks if the dead.txt file has been changed
    deadimg = []
    two_d = [[]]
    deadold, deadnew = rewrite()
  screenChange(screenx) #Constantly changes the amount of characters that can fit in one row to be correct to the screen size.
 
  for j in range(len(two_d)): # Displays the dead characters in the same order as the 2D array.
    for i in range(len(two_d[j])):
      screen.blit(deadimg[j][i],[size*i,j*size])
  pygame.display.flip()
pygame.quit()
