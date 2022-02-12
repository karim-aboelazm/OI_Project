import speech_recognition as sr
import os

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source,0,4)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en')
        print(f'You said : {query}')
    except:
        return 
    query = str(query)
    return query.lower()

while True:
    wake_up = Listen()
    if 'wake up' in wake_up:
        os.startfile('E:\\AI_Voice_Project\Project\\assistant.py')
    else:
        print("Nothing...")