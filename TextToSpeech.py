import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
             
engine.setProperty('rate', 200) # setting up new voice rate
engine.setProperty('volume',1.0) 
engine.runAndWait()    
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)   #printing current voice rate         
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)   #printing current volume level

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female/ 0 for male
engine.runAndWait()


engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()