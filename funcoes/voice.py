import pyttsx3


def falar(texto):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(texto)
    engine.runAndWait()
