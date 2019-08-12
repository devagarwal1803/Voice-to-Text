# import speech_recognition as sr
# while(True):
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Speak anything:")
#         voice = r.listen(source)
#         try:
#             text = r.recognize_google(voice)
#             print("You said : {}".format(text))
#             break
#         except:
#             print("Sorry could not recognize what you said. Try again")


import speech_recognition as sr  
from gtts import gTTS
import playsound
import os

num = 1
def assistant_speaks(output): 
    global num 
    num += 1
    print("Assistant : ", output) 
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
    playsound.playsound(file, True)  
    os.remove(file) 
  
  
  
def get_audio(): 
    rObject = sr.Recognizer() 
    audio = '' 
    with sr.Microphone() as source: 
        print("Listening...") 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Listened Stopped.") # limit 5 secs 
    try: 
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You said: ", text) 
        return text
    except: 
        assistant_speaks("Could not understand your audio, Please try again !")
        return get_audio()
  

def process_text(input): 
    try: 
        if "who are you" in input or "define yourself" in input: 
            speak = "Hello, I am your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etc..."
            assistant_speaks(speak) 
            return
        elif "who made you" in input or "created you" in input: 
            speak = "I have been created by Dev Agarwal."
            assistant_speaks(speak) 
            return
    
        elif 'open' in input: 
            assistant_speaks("No rights are available to perform such action")
            return
    
        else: 
            assistant_speaks("I can search the web for you, Do you want to continue?") 
            ans = get_audio() 
            if 'yes' in str(ans) or 'yeah' or 'yup' in str(ans): 
                search_web(input) 
            else:
                # process_text(ans)
                return
    except : 
        assistant_speaks("I don't understand") 
        return
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(input)
        else:
            assistant_speaks("Unable to understand. Bye")
    
  
# Driver Code 
if __name__ == "__main__": 
    assistant_speaks("What's your name?")
    name="" 
    name = get_audio() 
    assistant_speaks("Hello, " + name + '.') 
      
    while(1): 
        assistant_speaks("What can i do for you?") 
        text = get_audio().lower() 
        if text == 0: 
            continue
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            break
        process_text(text) 