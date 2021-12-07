import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import wikipedia
import pyjokes
import sys
import keyboard
import urllib.request
import WDKFunctions.OpenApps
from WDKFunctions.OpenFolder import OpenFolderF
#from WDKFunctions import OpenApps, OpenFolder
from WDKFunctions.EmailBot import get_email_info

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#check internet Connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Listening... ')
            #print('Listening... ')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if command == botName:
                talk('Yes sir. I am here.')
                command = take_command()
                return command
            elif botName in command:
                # talk(command)
                command = command.replace(botName, '')  # remove 'alexa' in command
                # print(command)
                return command
            else:
                talk('please say the command again.')
                command = take_command()
                return command

    except ConnectionError:
        talk('Sir your internet connection is unstable.')
        sys.exit()
    except LookupError:
        talk('LookupError')
        print('LookupError')
        talk('Sir Do you need more.?')
        command = take_command()
        if 'yes' in command:
            run_alexa()
        elif 'no' in command:
            talk('ok sir. Have a good day.')
            sys.exit()
        else:
            talk('I am shutting down..')
            sys.exit()
    except :
        talk('Sir Do you need more.?')
        command = take_command()
        if 'yes' in command:
            run_alexa()
        elif 'no' in command:
            talk('ok sir. Have a good day.')
            sys.exit()
        else:
            talk('I am shutting down..')
            sys.exit()


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')  # remove 'play' voiceKeyword
        talk('playing' + song)
        print('playing' + song)
        # print(song)
        if song == ' ':
            talk('please say the command again.')
            run_alexa()
        else:
            pywhatkit.playonyt(song)
            run_alexa()

    elif 'time' in command:
        t = datetime.datetime.now().strftime('%H:%M %p')
        print(t)
        talk('Current time is ' + t)
        run_alexa()

    elif 'tell me about' in command:
        try:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
            run_alexa()
        except:
            talk('please say the command again.')
            run_alexa()

    elif 'are you single' in command:
        talk('I am in relationship with wifi')
        print('I am in relationship with wifi')
        run_alexa()

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
        run_alexa()

    elif 'my name' in command:
        print('Your are ' + myName)
        talk('Your are ' + myName)
        run_alexa()

    elif 'your name' in command:
        print('I am ' + botName)
        talk('I am ' + botName +'. I am '+ myName +'\'s personal assistant')
        run_alexa()

    elif 'how are you' in command:
        print('Well, I am fine thank you sir.')
        talk('Well, I am fine thank you sir.')
        run_alexa()

    elif 'sleep' in command:
        talk('ok sir. sleep command executed. press home key to wake me')
        print('ok sir. sleep command executed. press home key to wake me')
        while True:
            time.sleep(0.1)
            if keyboard.is_pressed('home'):
                talk('Waking up executed.')
                print('Waking up executed')
                talk(' What can I do for you sir?')
                print(' What can I do for you sir?')
                break
        run_alexa()

    #OpenApps Command
    elif ('open' and 'app') in command:
        commandF = command.replace('open', '')
        commandF1 = commandF.replace('app', '')
        commandF2 = commandF1.replace(' ', '')
        openF = WDKFunctions.OpenApps.open_app(commandF2)
        if openF == 'Invalid':
            talk('please say the command again.')
        elif openF == 'done':
            talk('Opening ' + commandF)

        run_alexa()
    #CloseApp Command
    elif 'stop' in command:
        commandF = command.replace('stop', '')
        commandF = commandF.replace(' ', '')
        closeF = WDKFunctions.OpenApps.close_app(commandF)
        if closeF == 'Invalid':
            talk('please say the command again.')
        elif closeF == 'done':
            talk('closing ' + commandF)
        run_alexa()

    #OpenFolder Commands

    elif ('open' and 'folder') in command:
        commandF = command.replace('open', '')
        commandF = commandF.replace('folder', '')
        commandF = commandF.replace(' ', '')
        openF = OpenFolderF(commandF)
        if openF == 'Invalid':
            talk('please say the command again.')
        elif openF == 'done':
            talk('Opening ' + commandF)
        run_alexa()

    #Send Email
    elif 'send email' in command:
        get_email_info()
        talk(' What can I do for you sir?')
        run_alexa()

    # Shut Down Command
    elif 'shut down' in command:
        talk('ok sir. Shutting down executed. Have a good day.')
        print('ok sir. Shutting down executed. Have a good day.')
        sys.exit()

    else:
        talk('please say the command again.')
        print('please say the command again.')
        run_alexa()


myName = input("Enter Your name : ")
botName = input("Enter your assistance name : ")
# myName = 'WDK'
# botName = 'alexa'
talk('connected' if connect() else 'no internet!')
talk("Hello " + myName + ". I am your personal assistant " + botName + ". What can I do for you sir?")
run_alexa()
