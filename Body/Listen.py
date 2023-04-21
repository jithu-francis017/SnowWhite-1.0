import speech_recognition as sr
from googletrans import Translator

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print("Recognizing...")
        response = r.recognize_google(audio,language = "ml-IN", show_all=True)
        query = response['alternative'][0]['transcript']
        #print(query)
    except:
        return ""
    
    query = str(query).lower()
    return query

def TranslationMalToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    if len(data) < 2:
        return data
    else:
        print(f"You said: {data}")
        return data
#TranslationMalToEng("സുഖാണോ")

def MicExecution():
    query = Listen()
    data = TranslationMalToEng(query)
    return data

#MicExecution()