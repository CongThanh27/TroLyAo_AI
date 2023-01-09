import nltk
from neuralintents import GenericAssistant 
import speech_recognition 
import pyttsx3
import sys
import data 
import random
recognizer = speech_recognition.Recognizer()
speaker = pyttsx3.init()

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
speaker.setProperty("voice",voice_id)
speaker.setProperty("rate",120)
todo_list = []

def Hello():
    index = random.randint(0,len(data.hello)-1)
    message = data.hello[index]

    speaker.say(message)
    speaker.runAndWait()

def Create_note():
    global recognizer
    done = False
    
    while not done:
        try:
            
            with speech_recognition.Microphone() as mic: 

                speaker.say("Chọn tên tệp")
                speaker.runAndWait()
                
                audio = recognizer.record(mic, duration= 5)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

                file = open(f"{filename}.txt",'a+', encoding="utf8")
            with file as f: 

                f.writelines(todo_list)
                done = True

                speaker.say(f"Tôi đã tạo thành công {filename} cho bạn")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()
            speaker.say("Tôi không hiểu bạn nói gì")
            speaker.runAndWait()

def Add_todo():

    global recognizer
    
    speaker.say("Bạn muốn thêm công việc gì ")
    speaker.runAndWait()
    
    done = False

    while not done: 
        try:

            with speech_recognition.Microphone() as mic:
                audio = recognizer.record(mic, duration= 5)

                item = recognizer.recognize_google(audio, language = 'vi-VN')
                item = item.lower()
                
                todo_list.append(item)

                done = True

                speaker.say(f"Tôi đã thêm {item} vào danh sách")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()

            speaker.say("Tôi không hiểu bạn nói gì")
            speaker.runAndWait()

def Show_todos():
    speaker.say("Các công việc trong danh sách của bạn là")

    for item in todo_list:

        speaker.say(item)

    speaker.runAndWait()
def Delete_todo():
    global recognizer
    
    speaker.say("Bạn muốn xóa công việc gì ")
    speaker.runAndWait()
    
    done = False

    while not done: 
        try:

            with speech_recognition.Microphone() as mic:
                audio = recognizer.record(mic, duration= 5)

                item = recognizer.recognize_google(audio, language = 'vi-VN')
                item = item.lower()
                if item in todo_list:
                    todo_list.pop(item)
                    speaker.say(f"Tôi đã xóa {item} ra khỏi danh sách")
                else: 
                    speaker.say(f"Không có {item} trong danh sách")
                done = True
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()

            speaker.say("Tôi không hiểu bạn nói gì")
            speaker.runAndWait()

def Quit():
    index = random.randint(0,len(data.bye)-1)
    message = data.bye[index]
    speaker.say(message)
    speaker.runAndWait()
    sys.exit(0)

def Main():
    
    if "chào" in message :
        print("Chào")
        Hello()
    elif "lưu" in message :
        print("lưu")
        Create_note()
    elif "xem" in message :
        print("Mở")
        Show_todos()
    elif "thêm"  in message:
        print("Thêm")
        Add_todo()
    elif "xóa" in message :
        print("xóa")
        Delete_todo()
    elif "tạm biệt"  in message : 
        print("Thoát")
        Quit()
    else :
        speaker.say("tôi không thể nghe bạn nói")
        speaker.runAndWait()

while True:
    
    try:

        with speech_recognition.Microphone() as mic:

            print("Bot đang nghe......")
            audio = recognizer.record(mic, duration= 5)

            message = recognizer.recognize_google(audio, language = 'vi-VN')
            message = message.lower()

            print(message)
    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
    Main()
    