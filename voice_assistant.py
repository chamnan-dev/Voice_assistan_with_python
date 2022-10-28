import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path
import wolframalpha
import json
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 --> male voice 1 --> Female voice


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 16:
        speak('Good Afternoon')
    elif hour >= 16 and hour < 20:
        speak('Good Evening')
    else:
        speak('Good nigth')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    # it takes microphone input from the user and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening...')
        r.pause_threshold = 1
        user_audio = r.listen(source)
    try:
        print('Recognizing User Input...')
        query = r.recognize_google(user_audio, language='en-US')
        print(f"User Said: {query}\n")
    except Exception as e:
        # print(e) #use only if you want to print error
        print('Say that again please...')
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    speak('Hello Sir, I am Sophia your personal voice assistant, please tell me how i can help you')
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia','')
            query = query.replace(' ','_')
            result = wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
            webbrowser.get('chrome').open('https://www.youtube.com')
            
            time.sleep(60)

        elif 'open google' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
            webbrowser.get('chrome').open('https://www.google.com/')
            time.sleep(60)

        elif 'open facebook' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
            webbrowser.get('chrome').open('https://web.facebook.com/?_rdc=1&_rdr')
            time.sleep (60)

        elif 'find' in query:
            query = query.replace('search ','')
            query = query.replace(' ','+')
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
            webbrowser.get('chrome').open('https://www.google.com/search?q='+ query)
            time.sleep(60)
        
        elif 'play music' in query:
            speak('playing music from your playslist')
            music_dir = 'C:\\Personal_Voice_Assistant\\song'
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,song[4]))
            time.sleep(60)
        
        elif 'what time is it' in query:
            ctime = datetime.datetime.now().strftime('%H:%M:%S')
            print(ctime)
            speak(f'Sir them time is {ctime}')
            time.sleep(20)

        elif 'question' in query:
            speak('I can answer to computational and geographical question do you want to ask now')
            question = takeCommand()
            app_id = 'GQL78V-LX4E9TRKXR'
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            for i in res.results:
                print(i.text)
                speak(i.text)
        elif 'weather' in query:
            api_key = '4c933e966a931b46fa31303511b16ef7'
            base_url = 'https://api.openweathermap.org/data/2.5/weather?'
            speak('which city weather should i tell you')
            city_name = takeCommand()
            city_name = city_name.replace(' ','%20')
            complete_url = base_url+'q='+city_name+'&appid='+api_key
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature = int(current_temperature - 273.15)
                print(current_temperature)
                city_name = city_name.replace('%20',' ')
                speak('Temperature in '+city_name+'is '+str(current_temperature)+' degree celsius')
            
            
            

        elif 'quiet' in query:
            speak('Bye Bye, I am singing out , Good day to you')
            quit()
            
        #else:
            #speak('Hello sir, please say again...')
