#!/usr/bin/env python
# coding: utf-8

# In[24]:


#import pygame

from pygame import mixer

songs={"Manike Mage Hithe":"C:\\Users\Admin\Desktop\Project\songs\Manike Mage Hithe.mp3",
       "kanta laga":"C:\\Users\Admin\Desktop\Project\songs\kanta laga.mp3",
      "Srivalli":"C:\\Users\Admin\Desktop\Project\songs\Srivalli.mp3",
      "Srivalli hindi":"C:\\Users\Admin\Desktop\Project\songs\Srivalli hindi version.mp3",
      "Desh mere":"C:\\Users\Admin\Desktop\Project\songs\desh mere.mp3",
      "Dosti":"C:\\Users\Admin\Desktop\Project\songs\dosti.mp3",
      "Guche Gulabi":"C:\\Users\Admin\Desktop\Project\songs\Guche Gulabi.mp3",
      "jaago jaago bakre":"C:\\Users\Admin\Desktop\Project\songs\jaago jaago bakre.mp3",
      "Leharaayi":"C:\\Users\Admin\Desktop\Project\songs\Leharaayi.mp3",
      "o yaara dil lagana":"C:\\Users\Admin\Desktop\Project\songs\o yaara dil lagana.mp3",
      "mann bharryaa":"C:\\Users\Admin\Desktop\Project\songs\mann bharryaa.mp3",
      "chura liya":"C:\\Users\Admin\Desktop\Project\songs\chura liya.mp3",
      "Tera naam":"C:\\Users\Admin\Desktop\Project\songs\Tera naam.mp3",
      "Ranjha":"C:\\Users\Admin\Desktop\Project\songs\Ranjha"}

print("Songs in the list are \n")
print(songs.keys())
s=input("enter song name : ")
# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load(songs[s])

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:
	
	print("Press 'p' to pause, 'r' to resume,Press 'z' to rewind the song")
	print("Press 'e' to exit the program")
	query = input(" ")
	
	if query == 'p':

		# Pausing the music
		mixer.music.pause()	
	elif query == 'r':

        # Resuming the music
		mixer.music.unpause()

        
	elif query == 'e':

		# Stop the mixer
		mixer.music.stop()
		break
	elif query == 'z':
		mixer.music.rewind()

