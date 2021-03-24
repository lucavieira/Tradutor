import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
#engine.setProperty('voice', voices[2].id)
#engine.say("Hello World")
#engine.runAndWait()
