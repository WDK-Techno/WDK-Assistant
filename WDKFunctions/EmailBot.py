import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try :
        with sr.Microphone() as source:
            talk('listening..')
            voice=listener.listen(source)
            info = listener.recognize_google(voice)
            info = info.lower()
            if 'stop sending email' in info:
                talk("stopping email sending ")
                return 0
            print(info)
            return info
    except:
        talk("please say again.")
        infoE=get_email_info()
        return infoE

def send_email(receiver, subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('wdkprogramtest@gmail.com', 'wdkprogramtest123')
    email = EmailMessage()
    email['From']='wdkprogramtest@gmail.com'
    email['To']= receiver
    email['Subject']= subject
    email.set_content(message)
    server.send_message(email)

    # server.sendmail('wdkprogramtest@gmail.com',
    #                 'wdkcochero@gmail.com',
    #                 'Helow Mr.WDK.How are you..'
    #                 'Hope your are well.. '
    #                 'I send this message for testing my program.')
email_list={
    'hero': 'wdkcochero@gmail.com',
    'wdk' : 'wdilshankavindra@gmail.com',
    'kavi': 'dkavindraweerasinghe@gmail.com',
    'sas': 'sasandilantha@gmail.com',
    'suv': 'suvinilakshani@gmail.com',
    'si': 'sitharaathurupana@gmail.com',
    'ash': 'washanadithya@gmail.com',
    'father':'rohitha099@gmail.com'
}


def get_email_info():
    try:
        talk('To whom you want to send eamil?')
        name=get_info()
        receiver= email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = get_info()
        talk('Tel me the text in your email')
        message= get_info()
        send_email(receiver, subject, message)
        talk('Sir. Your email is sent')
        talk('Do you want to send more email?')
        send_more=get_info()
        if 'yes' in send_more:
            get_email_info()
        elif 'no' in send_more:
            talk('Ok sir. calling back to main program')
            return 0

    except:
        talk("Email sending process is terminated")
        return 0
