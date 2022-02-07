# pip install pyttsx3

import pyttsx3 as pytts

def voiceOutput(txt):
    engine = pytts.init('sapi5') # for voice 

    voices = engine.getProperty('voices') # Voice Import

    engine.setProperty('voices',voices[0].id) # Divied

    engine.setProperty('rate',180) # Voice Rate 150 - 200 

    print(f"Python : {txt}") # print the text

    engine.say(text=txt) # saying text

    engine.runAndWait() # for waiting

    print('   ') # New Line 

voiceOutput('Welcome To Our Voice Assistant System In Machine Learning and Deep Learning. ') 