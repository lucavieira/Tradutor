import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
print(rate)
rate = engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.say('We are the champions')
engine.say('안녕하세요')
engine.runAndWait()
