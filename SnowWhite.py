from Brain.AIBrain import ReplayBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The SnowWhite: Wait For Some Seconds. >>")
from Body.Speak import Speak
from Features.Wakeup import WakeupDetected
from Main import MainTaskExecution


def MainExe():

    Speak("Hello Jithu.")
    Speak("I'm SnowWhite, I'm Ready To Assist You.")
    while True:
        Data = MicExecution()
        Data = str(Data).replace(".","")
        Data = str(Data).lower()

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True:
            continue
        elif len(Data) < 3:
            continue
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Replay = QuestionsAnswer(Data)
        else:
            Replay = ReplayBrain(Data)
        Speak(Replay)

print(">> Starting The SnowWhite: Wait For Few Seconds More.")

def Wakeup(): 
    query = WakeupDetected()
    if "True-Mic" in query:
        print(" ")
        print(">> Wake up detected!! >>")
        print(" ")
        MainExe()
    else:
        pass

#while True:
Wakeup()