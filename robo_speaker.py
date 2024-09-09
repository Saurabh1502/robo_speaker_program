# this is robo_speaker_text to speach program

import pyttsx3

def robo_speak(message):
    # inititalize the TTS engine
    speak = pyttsx3.init()  
    # set properties (optional)
    
    speak.setProperty('rate',130) # speed of speech (word per minute)
    speak.setProperty('valume',1.0) # volume (0.0 to 1.0)
    # speak the message 
    speak.say(message)
    # wait for the speech to finish
    speak.runAndWait()
name = input("please enter your name : ")
robo_speak(f"hii{name}, welcome to robo speaker")
while True:
    message = input("Enter the message here to speak: ")
    if message =="exit":
        robo_speak("bye bye")
        break
    robo_speak(message)

