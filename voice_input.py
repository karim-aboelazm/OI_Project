# pip install speechrecognition
# pip install pipwin  >> pipwin install pyaudio

import speech_recognition as sr

def voiceInput():

    mic = sr.Recognizer()   # Recognizer object

    with sr.Microphone() as source: # Microphone object

        print('Listening... ') # print listening  

        mic.pause_threshold = 1 # wait for a second
        
        audio = mic.listen(source) # listen to the voice input 

    try:
        print('Recognizing ... ') # print recognizing

        query = mic.recognize_google(audio,language='en') # Query of Listened
        
        print(f'You said : {query}') # print with it listen
    except:
       return   # None
    query = str(query)

    return query.lower()
