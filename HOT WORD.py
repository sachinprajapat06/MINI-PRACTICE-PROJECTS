
import os
import speech_recognition as sr #pip install speechRecognition

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=3)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

while True:

    query = takeCommand()
    if 'start' in query or 'hello' in query or 'hi' in query:
        os.startfile('C:\\Users\\sachi\\PycharmProjects\\pythonProject\\this sem project.py')
    else:
        print("by")