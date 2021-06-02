import pyttsx3
import datetime
import requests
import speech_recognition as sr
import webbrowser
import pyaudio
import pyjokes
import wikipedia
import os
import random
import pywhatkit
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak('good morning sir')
    elif hour >=12 and hour<18:
        speak('good afternoon sir')
    else:
        speak('good evening sir')
    speak('what you want me to do for you sir?')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognising...')
        command = r.recognize_google(audio, language='en-in')
        command = command.lower()
        print('You asked for:',command)
    except Exception as e:
        print('Sorry, i did not understand, say that again...')
        speak('Sorry, i did not understand, say that again...')
        return 'None'
    return command

if __name__ == '__main__':
    wish_me()
    while True:
        command = take_command()

        if 'open youtube' in command:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'play' in command:
            command = command.replace('play', '')
            speak('playing' + command)
            pywhatkit.playonyt(command)

        # elif 'what' or 'how' or 'why' or 'when' in command:
        #     pywhatkit.search(command)

        elif 'play music' in command:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            song_items =len(songs)
            rand = random.randint(0, song_items)
            os.startfile(os.path.join(music_dir, songs[rand]))

        elif 'wikipedia' in command:
            speak('searching wikipedia')
            command = command.replace('wikipedia', '')
            results = wikipedia.summary(command, sentences=2)
            speak('according to wikipedia,')
            speak(results)

        elif 'open vs code' in command:
            speak('opening code')
            code_path = "C:\\Users\\MAYANK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open pycharm' in command:
            speak('opening pycharm')
            pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            os.startfile(pycharm_path)

        elif 'open brave' in command:
            speak('opening brave browser')
            brave_path = path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(brave_path)

        if 'whatsapp coders' in command:
            html = requests.get('https://a2oj.pratikdaigavane.me/ladder4').text
            soup = BeautifulSoup(html, 'html.parser')
            questions = soup.find_all('tr')
            questions = questions[4:]
            links = []
            for question in questions:
                link = question.a['href']
                links.append(link)
            pywhatkit.sendwhatmsg_to_group('L0N1yZn9Um36mKqcNg9abW', links[random.randint(0, 100)], 20, 0)



        elif 'tell a joke' in command:
            speak('searching joke')
            joke = pyjokes.get_joke(language='en', category='chuck')
            speak(joke)

        elif 'thank you' in command:
            speak('always there for you sir!')

        elif 'how are you' in command:
            speak('until you left me, I was doing good.')

        elif 'goodbye' in command:
            speak('goodbye sir! I will miss you!')
            break