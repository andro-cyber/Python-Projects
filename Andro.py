import speech_recognition as sr
import pyttsx3
import webbrowser
import music
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="34917d48fad54fb89f3699f0d99829d4"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def openai_response(command):
#     client = OpenAI(
#         api_key="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",
#     )
#     complition=client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": "You are a virtual assistant named Andro. Your task is to help users with various tasks such as opening websites, playing music, and providing news updates. You should respond in a friendly and helpful manner."},
#             {"role": "user", "content": command},
#         ])
    # return(complition.choices[0].message)
def processcommand(c):
    if "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open gmail" in c.lower():
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif "what is your name" in c.lower():
        speak("My name is Arya")  
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play music"):
        song=c.lower().split(" ")[1]
        link=music.music[song]
        webbrowser.open(link)
    elif c.lower().startswith("news"):
        speak("Here are some latest news")
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if response.status_code==200:
            data=r.json()
            articles=data["articles"]
            for ar in articles:
                speak(ar["title"])
                
    # else:
    #     response = openai_response(c)
    #     print(f"Assistant: {response['content']}")
    #     speak(response['content'])
        
if __name__ == "__main__":
    speak("Hello, how can I assist you?")
    while True:
         r=sr.Recognizer()
        
         try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=5,phrase_time_limit=5)
            word=r.recognize_google(audio)
            print(f"You said: {word}")
            if "arya" in word.lower():
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                
                    audio=r.listen(source,timeout=5,phrase_time_limit=5)
                command=r.recognize_google(audio)

                processcommand(command)
            
            
                        
         except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
         except sr.RequestError:
            print("Could not request results; check your network connection.")