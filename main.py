import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
from pywikihow import search_wikihow
import operator
import webbrowser
from playsound import playsound
import pywhatkit
from keyboard import press
from keyboard import press_and_release
import psutil
from bs4 import BeautifulSoup
import speedtest
import smtplib
import pprint
import sys
import requests
import time
import pyjokes
import pyautogui
import instadownloader
import instaloader
import PyPDF2
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisSuperUI import Ui_Form as mainUIPage
from jarvisSuperUI import Ui_Form

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to wish
def wish():
    speak("Allow me to introduce myself")
    time.sleep(0.3)
    speak("I am Jarvis, the virtual artificial intelligence, made by,  Mr.Maahi ")
    time.sleep(0.3)
    speak("And I'm here to assist you with a variety of tasks, as best I can")
    time.sleep(0.3)
    speak("24 hours a day, seven days a week")
    time.sleep(0.3)
    speak("Importing all preferences from home interface")
    time.sleep(0.3)
    speak("system's now fully operational")
    time.sleep(0.3)
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak(f"good morning sir")
    elif hour > 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("please tell me how can i help you?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your mail', 'password')
    server.sendmail('your mail', to, content)
    server.close()


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=ebf37f4bd8fd4ecf9724b363e1bfce2e"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


def pdf_reader():
    speak("sir please tell me which one to read")
    time.sleep(3)
    speak("okay sir, please enter the name of the pdf")
    pg1 = input("Please enter the name of the pdf: ")
    book = open(pg1, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)



class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution

    # convert voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"you said: {query}")

        except Exception as e:
            # speak("Say that again please...")
            return 'none'
        query = query.lower()
        return query

    @property
    def TaskExecution(self):
        global time
        wish()
        while True:
            self.query = self.takecommand()

            # logic building for tasks

            if "open notepad" in self.query:
                speak("what do you want me to write?")
                time.sleep(5)
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
                speak("ok sir, opening notepad")

            elif "to tell" in self.query:
                speak("anything. as your wish sir")

            elif "presentation" in self.query or "demo" in self.query:
                speak("but sir, i am in incomplete as of now")
                speak("still you are in the intermediate stage of coding")
            elif "not a problem" in self.query or "problems" in self.query or "problem" in self.query:
                speak("not at all sir, you please continue the presentation, i will give my best")
            elif "command prompt" in self.query:
                os.system("start cmd")
                speak("opening...")
                time.sleep(3)
                speak("what's the next command?")

            elif "camera" in self.query:
                speak("opening...")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "open zoom" in self.query or "zoom" in self.query:
                speak("opening...")
                npath = "C:\\Users\\maahi\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
                os.startfile(npath)

            elif "open vs code" in self.query or "update" in self.query:
                speak("okay sir, opening visual studio code...")
                npath = "C:\\Users\\maahi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(npath)

            elif "music" in self.query or "hit" in self.query:
                music_dir = "C:\\Users\\maahi\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
                speak("would you like this?")
                time.sleep(4)

           # elif "focus" in self.query:
                music_dir = "C:\\Users\\maahi\\Desktop\\bot"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
                speak("okay, what about this?")

                time.sleep(10)

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif 'wikipedia' in self.query:
                speak("searching wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif "shopping" in self.query:
                speak("sir, which shopping website you want me to open?")

            elif "amazon" in self.query:
                webbrowser.open("www.amazon.in")
                speak("opening")
            elif "flipkart" in self.query:
                webbrowser.open("www.flipkart.com")
                speak("opening")
            elif "facebook" in self.query:
                speak("checking facebook")
                webbrowser.open("https://www.facebook.com/deekshith.fc/")
                time.sleep(6)
                speak("looks like you are all caught up sir!")



            elif "google" in self.query:
                speak("sir, what should i search on google")
                self.cm = self.takecommand().lower()
                webbrowser.open(f"https://www.google.com/search?q={self.cm}&oq={self.cm}&aqs=chrome.0.69i"
                                f"59j0i67j35i39j69i57j0i512j69i60l3.1224j0j4&sourceid=chrome&ie=UTF-8")

            elif 'close tab' in self.query or "close the tab" in self.query or 'Close the tab' in self.query or "tab" in self.query or "tap" in self.query:
                press_and_release('ctrl + w')

            elif 'new window' in self.query:
                press_and_release('ctrl + n')

            elif "last night" in self.query:
                speak("sir, we are working on a artificial intelligence project. you should check it.")

            elif "song on youtube" in self.query:
                speak("sir, which song should i play on youtube")
                self.cm = self.takecommand().lower()
                pywhatkit.playonyt(f"{self.cm}")

            elif "video" in self.query:
                speak("sir, which one to play?")
                self.cm = self.takecommand().lower()
                pywhatkit.playonyt(f"{self.cm}")
                time.sleep(25)
                speak("sir, what's the next command")

            elif 'pause' in self.query:
                 press('space bar')

            elif 'resume' in self.query:
                press('space bar')

            elif 'full screen' in self.query:

                press('f')

            elif "time" in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is ' + time)

            # closing applications
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
                time.sleep(3)
                speak("tell me the next task")

            elif "close vs code" in self.query or "code" in self.query:
                speak("okay sir, closing visual studio code")
                os.system("taskkill /f /im Code.exe")

            elif "close zoom" in self.query:
                speak("okay sir, closing zoom")
                os.system("taskkill /f /im Zoom.exe")

            # set alarm

            elif 'alarm' in self.query or 'set alarm' in self.query:
                speak("sir please tell me the time to set alarm.")
                time = input("Enter The Time to set alarm :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")
                    if now == time:
                        speak("Time To Wake Up Sir!")
                        playsound('jarvis_morning_alarm.mp3')
                        speak("Alarm Closed!")

                    elif now > time:
                        break

            # to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep mode" in self.query:
                os.system("rundll32.exe.powrpof.dllSetSuspendState 0,1,0")

            elif "switch window" in self.query or "switch" in self.query:
                speak("switching...")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")

            elif "news" in self.query:
                speak("please wait sir, fetching the latest news")
                news()

            elif "screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                self.name = self.takecommand().lower()
                speak("please sir hold the screen for few seconds, i am taking sreenshot")
                # time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{self.name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for the next command")

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                self.condition = self.takecommand().lower()
                if "yes" in self.condition or "of course" in self.condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                else:
                    pass

            elif "where am i located" in self.query or "where are we" in self.query or "location" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print (geo_data)
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city, {state}, {country}")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass

            elif "relax" in self.query:
                speak('ok sir, what do you want me to do for your relaxation')

            elif "read pdf" in self.query or "pdf" in self.query:
                pdf_reader()

            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")
                if percentage >= 75:
                    speak("we have enough power to continue our work")
                elif percentage >= 40 and percentage <= 75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage <= 15 and percentage <= 30:
                    speak("we don't have enough power to work, please connect to charging")
                elif percentage <= 15:
                    speak("we have very low power, please connect to charging the system will shutdown very soon")

            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                self.condition = self.takecommand().lower()
                if "hide" in self.condition or "all files" in self.codnition or "files" in self.condition:
                    os.system("attrib +h /s /d")  # os module
                    speak("sir, all the files in this folder are now hidden.")
                elif "visible" in self.condition or "make them" in self.condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone. i wish you are taking a peace")
                elif "leave it" in self.condition or "leave for now" in self.condition:
                    speak("Ok sir")

            elif "internet speed" in self.query or "speed of internet" in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
                # try:
                #   os.system('cmd /k "speedtest"')
                # except:
                #  speak("sorry sir, i couldn't fetch the speed of our internet due to network issues")

            elif "temperature" in self.query:
                search = "temperature in tanuku"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "do some calculations" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,  # plus
                        '-': operator.sub,  # minus
                        'x': operator.mul,  # multiplied by
                        'divided': operator.__truediv__,  # divided
                        }[op]

                def eval_binary_expr(op1, oper, op2):  # 5 plus 8
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))

            elif 'hello' in self.query or 'hey' in self.query or 'hi' in self.query:
                speak("hello sir, may i help you with something")

            elif 'how are you' in self.query or 'hello' in self.query:
                speak("i am fine sir, what about you?")

            elif "good" in self.query or "fine" in self.query or "well" in self.query:
                speak("that's great to hear from you sir")
                speak("please assign me the tasks that i can perform sir")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir")

            elif "bye" in self.query or "offline" in self.query:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay sir, i am going to sleep, you can call me anytime.")
                break

            elif "volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "volume mute" in self.query or "mute" in self.query:
                pyautogui.press("volumemute")

            elif "question" in self.query:
                speak("ofcourse yes, what's that sir?")
                self.cmnd = self.takecommand().lower()
                search = self.cmnd
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(temp)

            elif 'send email' in self.query:
                speak("what should i say?")
                content = self.takecommand().lower()

                try:
                    speak("what should I say?")
                    content = self.takecommand().lower()
                    to = "maahi2175@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent to Mr.Maahi")
                except Exception as e:
                    print(e)
                    speak("Sorry sir, I cannot sent this email")

            elif "activate how " in self.query:
                speak("How to do mode is activated")
                while True:
                    speak("please tell me what you want to know")
                    self.how = self.takecommand()
                    try:
                        if "exit" in self.how or "close" in self.how:
                            speak("okay sir, how to do mode is closed")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(self.how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry sir, i am not able to find this")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.startpushButton.clicked.connect(self.startTask)
        self.ui.quitpushButton.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/gggf.jpg")
        self.ui.border1.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/gggf.jpg")
        self.ui.border2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/gggf.jpg")
        self.ui.jarvisborder.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/jarviss.gif")
        self.ui.jarvisui.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/Private.gif")
        self.ui.iornman.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/Start.png")
        self.ui.startpic.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/Quit.png")
        self.ui.quitpic.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/Jarvis_Gui (1).gif")
        self.ui.speakergif.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/gggf.jpg")
        self.ui.datebox.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/gggf.jpg")
        self.ui.timebox.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/initial.gif")
        self.ui.initiating.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/Jarvis UI Files-20220406T122401Z-001/Jarvis UI Files/GUI files/Earth.gif")
        self.ui.earth.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        currentTime = QTime.currentTime()
        currentDate = QDate.currentDate()
        labelTime = currentTime.toString('hh:mm:ss')
        labelDate = currentDate.toString(Qt.ISODate)
        self.ui.datetextBrowser.setText(f"Date: {labelDate}")
        self.ui.timetextBrowser.setText(f"Time: {labelTime}")


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())


















