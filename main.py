import speech_recognition as sr
import webbrowser
import musiclibrary
import pyttsx3
import requests


recognizer =sr.Recognizer()
engine = pyttsx3.init()
newsapi = "77cf621000994c5fbbbac9abc92e3d0c"

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    # this will create all the command regardign all the tab opening in the browser as well as the given command also gone through to the given will take 
    # the moment to create the while
    
    if  "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://Linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"GET https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response 
            headlines = r.json()
            # Print the headlines
            for article in headlines['articles']:
                speak(f"Title: {article['title']}")
    
    else :
        # Let openai handle the request
        pass





if __name__ == "__main__":
    speak("Intializing jarvis for you ....")

        # Listen for  the wake word 'jarvis'

while True:
    # obtain audio from the microphone
    r = sr.Recognizer()
    
    

    print("Recognizing")
    # recognize speech using google
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2, phrase_time_limit=3)
        word = r.recognize_google(audio)
        if word.lower() == ("jarvis"):
            speak("Yes sir") 
            # Listen for command

            with sr.Microphone() as source:
                print("Jarvis is Active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)


                processCommand(command)
    except Exception as e:
        print("Error; {0}".format(e))