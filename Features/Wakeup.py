import speech_recognition as sr

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5) # Listening Mode.....
    
    try:
        print("Recognizing...")
        response = r.recognize_google(audio,language = "en-in", show_all=True)#"ml-IN"
        query = response['alternative'][0]['transcript']
        #print(query)

    except:
        return ""
    
    query = str(query).lower()
    #print(query)
    return query

def WakeupDetected():

    while True:

        queery = Listen().lower()

        if "wake up" in queery:
            return "True-Mic"
        
        else:
            pass
