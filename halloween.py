#Daedalus Hackathon - Sudiptto Biswas
# Halloween hackathon

import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.ndimage import zoom

ca = plt.imread('images/squad.png')
t = 0.50

""""
Psuedocode / Process

1) Set up the matplotlib.pyplot and numpy configs like in the lectures (Done)
     Sidenote: Had to get scipy library in order to resize (Learn via stack overflow: https://stackoverflow.com/questions/16276349/resizing-an-image-in-python)
2) Use the code for counting each pixel that is white (Done)
3) Modify the code to change the pixel shade based on the color of each pixel (Done)
4)Using the random library set up random creepy texts through out the screen for each pixel (Done)
5) Make an overlay somewhere (Partially done, going to create an overlay on the right)
6) Set up Tkinter or Flask (Python web framework) so their is gui + user can send own pictures

Optional:
If flask - Set up database and a seperate part of the website in order to show the creation to the world
"""



# Create a transparent image with the same dimensions as the main image
#overlay = np.zeros_like(ca)


# Get number of rows and columns
rows = ca.shape[0]
columns = ca.shape[1]

# make list 
creepy_phrases = ["Don't turn around", "Look behind you", ':)', "Shut the door:)", "Do you hear me?", "Is this you!?"]

for i in range(ca.shape[0]): # rows
     for j in range(ca.shape[1]): # columns
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] < t) and (ca[i,j,1] < t) and (ca[i,j,2] < t): # under a 0.5 intensity, so it's looking for the black 
               ca[i,j,1:3] = 0
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t): # also lighter intensity
               ca[i,j,1:3] = 0




pumpkin = plt.imread('images/pumpkin.png')
#print(type(pumpkin.shape[0]))
#print(pumpkin.shape[1] / 2)

# 10% of original size 
overlay_height = int(rows * 0.1)
overlay_width = int(columns * 0.1)

#pumpkin = plt.resize(pumpkin, (overlay_height, overlay_width))

# Resize the pumpkin image using scipy.ndimage.zoom
pumpkin = zoom(pumpkin, (overlay_height / pumpkin.shape[0], overlay_width / pumpkin.shape[1], 1))
                     
# set top left coordinates
topLeft_x = 0
topLeft_y = 0

ca[topLeft_y:topLeft_y + overlay_height, topLeft_x:topLeft_x + overlay_width] = pumpkin

# Add the text "Look behind you"
plt.text(rows/4, columns/2, random.choice(creepy_phrases), color='white', fontsize=23, fontweight='bold')
plt.text(rows/4, columns/6, random.choice(creepy_phrases), color='white', fontsize=23, fontweight='bold')


plt.imshow(ca)
plt.show()