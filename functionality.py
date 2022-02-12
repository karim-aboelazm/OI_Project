import time
import datetime
import wikipedia
import webbrowser
import pywhatkit
from pywikihow import search_wikihow
import requests
import speedtest
import wolframalpha
from pyautogui import click, position
from keyboard import write , press
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

def open_word():
    click(x=13, y=754)
    time.sleep(3)
    write('word')
    time.sleep(3)
    press('enter')

def close_word():
    pass

def open_chrome():
    click(x=13, y=754)
    time.sleep(3)
    write('google chrome')
    time.sleep(3)
    press('enter')

def close_chrome():
    pass

def open_excel():
    click(x=13, y=754)
    time.sleep(3)
    write('excel')
    time.sleep(3)
    press('enter')

def close_excel():
    pass

def open_access():
    click(x=13, y=754)
    time.sleep(3)
    write('access')
    time.sleep(3)
    press('enter')

def close_access():
    pass

def open_zoom():
    click(x=13, y=754)
    time.sleep(3)
    write('zoom')
    time.sleep(3)
    press('enter')

def close_zoom():
    pass

def open_vscode():
    click(x=13, y=754)
    time.sleep(3)
    write('vscode')
    time.sleep(3)
    press('enter')

def close_vscode():
    pass

def open_powerpoint():
    click(x=13, y=754)
    time.sleep(3)
    write('powerpoint')
    time.sleep(3)
    press('enter')

def close_powerpoint():
    pass

def open_notepad():
    click(x=13, y=754)
    time.sleep(3)
    write('notepad')
    time.sleep(3)
    press('enter')

def close_nodepad():
    pass

def open_chrome():
    click(x=13, y=754)
    time.sleep(3)
    write('google chrome')
    time.sleep(3)
    press('enter')

def close_chrome():
    pass

def open_downloads():
    time.sleep(1)
    startfile('C:\\Users\\Karim Aboelazm\\Downloads')

def close_downloads():
    pass

def open_cmd():
    click(x=13, y=754)
    time.sleep(3)
    write('cmd')
    time.sleep(3)
    press('enter')

def close_cmd():
    pass

def check_internet_speed():
    voiceOutput('Checking Sir ...')
    speed = speedtest.Speedtest()
    download_speed = speed.download()
    correct_Dspeed = int(download_speed/800000)
    upload_speed = speed.upload()
    correct_Uspeed = int(upload_speed/800000)
    voiceOutput(f'Download speed is {correct_Dspeed} m/s , upload speed is {correct_Uspeed} m/s')

def break_assistant():   
    voiceOutput("Ok Sir , You Can Call Me At Anytime ..")
    voiceOutput("Just Say Wake Up !")
    exit()  


def get_error(query): 
    query = str(query)
    if 'time' in query:
        get_time()
    elif 'date' in query:
        get_date()
    elif 'day' in query:
        get_day()
    elif "break" in query:
        break_assistant()
    elif "open word" in query:
        open_word()
    elif "open powerpoint" in query:
        open_powerpoint()
    elif "open vscode" in query:
        open_vscode()
    elif "open chrome" in query:
        open_chrome()
    elif "open notepad" in query:
        open_notepad()
    elif "open access" in query:
        open_access()
    elif "open excel" in query:
        open_excel()
    elif "open zoom" in query:
        open_zoom()
    elif "open cmd" in query:
        open_cmd()
    elif "internet speed" in query:
        check_internet_speed()
    

# -----------------------------------------------------------------------------
def wolframalpha_setting(query):
    api_key = "WY8246-963Y55UH56"
    request = wolframalpha.Client(api_key)
    response = request.query(query)
    try:
        return next(response.results).text
    except:
        voiceOutput("Something went wrong Sir..")

def whatsapp_msg(name,message):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)
    click(x=862, y=703)
    time.sleep(2)
    write(message)
    time.sleep(2)
    press('enter')

def whatsapp_call(name):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)
    click(x=1203, y=44)

def whatsapp_video(name):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)
    click(x=1147, y=51)

def whatsapp_chat(name):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)


def get_input_error(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        voiceOutput(wikipedia.summary(name))
    
    elif "google" in tag:
        name = str(query).replace("google","")
        name = name.replace("search for","")
        name = name.replace("search","")
        pywhatkit.search(name)
    
    elif "YouTube" in tag:
        query = str(query).replace("YouTube","").replace("Open Youtube","").replace("in YouTube","").replace(" ","")
        youtube = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(youtube)

    elif "website" in tag:
        query = str(query).replace("open","").replace(" ","")
        site = "https://www."+str(query)+".com/"
        webbrowser.open(site)

    elif "playvideo" in tag:
        query = str(query).replace("open video","")
        query = query.replace("start video","")
        query = query.replace("YouTube video","")
        query = query.replace("play on YouTube","")
        query = query.replace(" ","")
        query = query.replace("play","")
        pywhatkit.playonyt(query)

    elif "remember that" in tag:
        rmsg = str(query).replace("remember that","")
        rmsg = rmsg.replace("remind me that","")
        voiceOutput(f"You Told me to remind you that {rmsg}")
        remember = open('remind.txt','w')
        remember.write(rmsg)
        remember.close()

    elif "what do you remember" in tag:
        remember_message = open('remind.txt','r')
        voiceOutput(f"You Told me to remember you that {str(remember_message.read())}")

    elif "weather" in tag:
        query = str(query).replace("weather in","")
        query = query.replace("what is weather in","")
        query = query.replace("weather for","")
        api_key = "382898aca8ccf36781e1452584f5d79a"
        root_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = f"{root_url}appid={api_key}&q={query}"
        r = requests.get(url)
        data = r.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            weather_stat = data["weather"][0]["description"]
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            wind_speed = data["wind"]["speed"]
            voiceOutput(f"Weather Information in {query}")
            voiceOutput(f"The Weather conditions is {weather_stat}")
            voiceOutput(f"The temperature is {temp} Kelvin")
            voiceOutput(f"The pressure is {pressure} hpa")
            voiceOutput(f"The humidity is {humidity} %")
            voiceOutput(f"The wind speed is {wind_speed} m/s")
        else:
            voiceOutput("Something went wrong sir Check Again..")

    elif "temperature" in tag:
        query = str(query).replace("what is the temperature","temperature in")
        query = query.replace("temperature for","temperature in")
        voiceOutput(wolframalpha_setting(query))

    elif "calculate" in tag:
        query = str(query).replace("multiply","*")
        query = query.replace("in","*")
        query = query.replace("into","*")
        query = query.replace("power","**")
        query = query.replace("to the power","**")
        query = query.replace("plus","+")
        query = query.replace("minus","-")
        query = query.replace("divide","/")
        query = query.replace("over","/")
        query = query.replace("div","/")
        try:
            voiceOutput(f'The result is : {wolframalpha_setting(query)}')
        except:
            voiceOutput("I Can Not Calculate This Query")

    elif "whatsapp massage" in tag:
        voiceOutput('For Whom Sir ..')
        name = voiceInput()
        voiceOutput('Ok Sir , Tell me The Message..')
        query = voiceInput()
        whatsapp_msg(str(name),str(query))

    elif "whatsapp call" in tag:
        voiceOutput('For Whom Sir ..')
        query = voiceInput()
        voiceOutput(f'Ok Sir , Calling now to {query} ..')
        whatsapp_call(str(query))

    elif "whatsapp video" in tag:
        voiceOutput('For Whom Sir ..')
        query = voiceInput()
        voiceOutput(f'Ok Sir , Making Video With {query} ..')
        whatsapp_video(str(query))

    elif "whatsapp chat" in tag:
        voiceOutput('For Whom Sir ..')
        query = voiceInput()
        voiceOutput(f'Ok Sir , Opening whatsapp chat With {query} ..')
        whatsapp_chat(str(query))

    elif "how to" in tag:
        voiceOutput('Getting Data from The Internet...')
        max_result = 1
        how_to = search_wikihow(query, max_result)
        assert len(how_to) == max_result
        voiceOutput(how_to[0].summary)

