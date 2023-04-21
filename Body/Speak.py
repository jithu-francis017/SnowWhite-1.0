import pyttsx3


def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('language', 'en-in')
    engine.setProperty('gender', 'female')
    engine.setProperty('volume', 1)
    engine.setProperty('age', 'adult')
    lengthcode = len(Text)
    if lengthcode>30:
        engine.setProperty('rate', 180)
    else:
        engine.setProperty('rate', 175)
    print("    ")
    print(f"SnowWhite: {Text}")
    print("     ")
    engine.say(text=Text)
    engine.runAndWait()