import speech_recognition 
import gtts as gTTS
import sys
import playsound
import os
from Giaodien_chinh import *
# %%
def ToDoList():
    todo_list = []
    def get_audio(limmit_timed=5):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tôi: ", end='')
            audio = r.listen(source, phrase_time_limit=limmit_timed)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                print(text)
                return text
            except:
                print("...")
                return 0
    # %%
    def stop(name):
        Bot_khongnghe(4,f"Chúc một ngày tốt lành, hẹn gặp lại {name}")
    # %%
    def get_text():
        for i in range(3):
            text = get_audio()
            if text:
                return text.lower()
            elif i < 2:
                #speak("Bot không nghe rõ. Bạn nói lại được không!")
                Bot_khongnghe(4,"Anja không nghe bạn nói, bạn nói lại được không?")
        time.sleep(2)
        stop()
        return 0
    def Create_note():
        Bot_noi(3,"Bạn muốn lưu danh sách với tên ? ")
        filename = get_text()
        if filename:
            file = open(f"{filename}.txt",'a+', encoding="utf8")
            
            with file as f: 
                
                f.writelines(todo_list)
                Bot_noi(2,f"Anja đã tạo thành công {filename} cho bạn")
        else:    
            Bot_khongnghe()
    def Add_todo():
        
        Bot_noi(2,"Bạn muốn thêm công việc gì ")
        item =get_text()
        if item:
            todo_list.append(item)
            Bot_noi(2,f"Anja đã thêm {item} vào danh sách")
        else:
            Bot_khongnghe()

    def Show_todos():
        Bot_noi(2,"Các công việc trong danh sách của bạn là")
        for item in todo_list:
            Bot_noi(2,item)

    def Delete_todo():
        
        Bot_noi(2,"Bạn muốn xóa công việc gì ")
        item = get_text()
        if item:
            if item in todo_list:
                todo_list.remove(item)
                Bot_noi(3,f"Anja đã xóa {item} ra khỏi danh sách")
            else: 
                Bot_noi(3,f"Không có {item} trong danh sách")
        else:
            Bot_khongnghe()
    Bot_noi(3,"Đã tạo danh sách, bạn muốn làm gì tiếp theo")
    
    done = True
    while done:
        if done==False:
            return
        message = get_text()
        Hienthithongtinngheduoc(2,message)
        if "lưu" in message :
            Create_note()
        elif "xem" in message :
            Show_todos()
        elif "thêm"  in message:
            Add_todo()
        elif "xóa" in message :
            Delete_todo()
        elif "kết thúc" in message:
            Bot_noi(3,"Thoát chức năng tạo danh sách")
            done = False
        else :
            Bot_khongnghe(3,"Anja không có chức năng này, bạn nói lại được không")
            
     
        