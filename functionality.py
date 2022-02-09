import time
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
from voice_input import voiceInput
from voice_output import voiceOutput

# this function for getting time now
def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    voiceOutput(f"Time Now Is : {time}")

# this function for getting datetime now
def get_date():
    date = datetime.date.today()
    voiceOutput(f"Today Is : {date}")

# this function for getting today name
def get_day():
    day = datetime.datetime.now().strftime("%A")
    voiceOutput(f"Today Is : {day}")

def get_error(query): 
    query = str(query)
    if 'time' in query:
        get_time()
    elif 'date' in query:
        get_date()
    elif 'day' in query:
        get_day()


def get_input_error(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        voiceOutput(wikipedia.summary(name))
    
    elif "google" in tag:
        name = str(query).replace("google","")
        name = name.replace("search for","")
        name = name.replace("search","")
        pywhatkit.search(name)