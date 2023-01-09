#%%
import threading
import time
from tkinter import *
import tkinter
from PIL import Image, ImageTk

import os
from numpy import place
import playsound
import speech_recognition as sr
import wikipedia
from webdriver_manager.chrome import ChromeDriverManager
from gtts import gTTS
#%%
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

def speak(text):
    print("Bot: {}".format(text))
    sound=gTTS(text,lang="vi",slow=False)
    sound.save("sound.mp3")
    playsound.playsound('sound.mp3',True)
    
    os.remove("sound.mp3")
#%%   
window = Tk()
window.title("Trợ lý ảo")
window.geometry("1000x1000+0+0")


#%%
#Chao Mung
chaomung_1 = Image.open(f"./72ppi/Chaomung01.png")
Chaomung_1 = ImageTk.PhotoImage(chaomung_1)
chaomung_2 = Image.open(f"./72ppi/Chaomung02.png")
Chaomung_2 = ImageTk.PhotoImage(chaomung_2)



Bg = Label(window,image=Chaomung_1)
Bg.place(x=0, y=0)

def chaomung(Speak="Chào mừng bạn đến với trợ lý ảo anja"):
    Bg.configure(image=Chaomung_1)
    def xuly_1():
        for i in range(4):
            print (threading.current_thread().name, 'icon')
            Bg.configure(image=Chaomung_1)
            time.sleep(0.5)
            print (threading.current_thread().name, 'Speak')
            Bg.configure(image=Chaomung_2)
            time.sleep(0.75)
            if i==3:
                window.quit()
    def xuly_2():
        print (threading.current_thread().name, 'Nói')
        speak(Speak)   
    d = threading.Thread(name='Icon', target=xuly_1)
    t = threading.Thread(name='noichuyen', target=xuly_2)
    d.start()
    t.start()
    window.mainloop()
#chaomung()   
#%%
# Bot nói chuyện   
bg_botnoi = Image.open("./72ppi/Giaodien2doidap2.png")
Bg_botnoi = ImageTk.PhotoImage(bg_botnoi)

icon_botnoi1 = Image.open(f"./hh/noi1.jpg")
Icon_botnoi1 = ImageTk.PhotoImage(icon_botnoi1)
icon_botnoi2 = Image.open(f"./hh/noi2.jpg")
Icon_botnoi2 = ImageTk.PhotoImage(icon_botnoi2)

btn = Button(window, text="Hihi",wraplength=325,justify="left",bd=0,font=("UVN Dzung Dakao",15),bg="#FFF8F3")
icon = Label(window,bd=0)
icon.place(x=445, y=165) 
def Bot_noi(n=3,content="Anja có thể giúp gì cho bạn không"):
 
    btn.configure(text=content)
    btn.place(x=390,y=409)
    Bg.configure(image=Bg_botnoi)

    def xuly_1():
        for i in range(n):
            print (threading.current_thread().name, 'icon')
            icon.configure(image=Icon_botnoi1)
            time.sleep(0.5)
            print (threading.current_thread().name, 'Speak')
            icon.configure(image=Icon_botnoi2)
            time.sleep(0.75)
            if i==n-1:
                window.quit()
    def xuly_2():
        print (threading.current_thread().name, 'Nói')
        speak(content)
        d.daemon
        t.daemon   
    d = threading.Thread(name='Icon', target=xuly_1)
    t = threading.Thread(name='noichuyen', target=xuly_2)

    d.start()
    t.start()    
    window.mainloop()
#Bot_noi(7,"Xin Chào")
#%%
# Bot lang nghe  
bg_langnghe = Image.open("./72ppi/Giaodien2doidap2.png")
Bg_langnghe = ImageTk.PhotoImage(bg_langnghe)

icon_langnghe1 = Image.open(f"./hh/langnghe1.jpg")
Icon_langnghe1 = ImageTk.PhotoImage(icon_langnghe1)
icon_langnghe2 = Image.open(f"./hh/langnghe2.jpg")
Icon_langnghe2 = ImageTk.PhotoImage(icon_langnghe2)


def Bot_langnghe(n=4,content="Anja đang nghe bạn nói"):
   
    Bg.configure(image=Bg_botnoi)
    btn.configure(text=content)
    btn.place(x=390,y=409)
    def xuly_1():
        for i in range(n):
            print (threading.current_thread().name, 'icon')
            icon.configure(image=Icon_langnghe1)
            btn.configure(text="...")
            time.sleep(0.5)
            print (threading.current_thread().name, 'Speak')
            icon.configure(image=Icon_langnghe2)
            btn.configure(text=content)
            time.sleep(0.75)
            if i==n-1:
                window.quit()
    def xuly_2():
        print (threading.current_thread().name, 'Nói')
        speak(content)
        d.daemon
        t.daemon   
    d = threading.Thread(name='Icon', target=xuly_1)
    t = threading.Thread(name='noichuyen', target=xuly_2)

    d.start()
    t.start()  
    window.mainloop()
#Bot_langnghe()
#%%
#Bot hiển thị thông tin nghe được từ người nói 
bg_thongtin = Image.open("./72ppi/Giaodien1doidap1.png")
Bg_thongtin = ImageTk.PhotoImage(bg_thongtin)

icon_thongtin1 = Image.open(f"./hh/langnghe1.jpg")
Icon_thongtin1 = ImageTk.PhotoImage(icon_thongtin1)
icon_thongtin2 = Image.open(f"./hh/langnghe2.jpg")
Icon_thongtin2 = ImageTk.PhotoImage(icon_thongtin2)

def Hienthithongtinngheduoc(n=4,content="TPHCM"):
    window.client() 
    Bg.configure(image=Bg_thongtin)
    btn.configure(text=content)
    btn.place(x=295,y=460)
    def xuly_1():
        for i in range(n):
            print (threading.current_thread().name, 'icon')
            icon.configure(image=Icon_thongtin1)
            time.sleep(0.5)
            print (threading.current_thread().name, 'Speak')
            icon.configure(image=Icon_thongtin2)
            time.sleep(0.75)
            if i==n-1:
                window.quit()
    def xuly_2():
        print (threading.current_thread().name, 'Nói')
        speak(content)
        d.daemon
        #t.daemon   
    d = threading.Thread(name='Icon', target=xuly_1)
    #t = threading.Thread(name='noichuyen', target=xuly_2)

    d.start()
    window.mainloop()
   # t.start()
#Hienthithongtinngheduoc()
# Bot không nghe được bạn nói
#%%
bg_loi = Image.open("./72ppi/Giaodien2doidap2.png")
Bg_loi = ImageTk.PhotoImage(bg_loi)

icon_loi = Image.open(f"./hh/loi.jpg")
Icon_Loi = ImageTk.PhotoImage(icon_loi)

def Bot_khongnghe(n=4,content="Anja không nghe bạn nói, bạn nói lại được không?"):
    Bg.configure(image=Bg_loi)
    icon.configure(image=Icon_Loi)
    btn.configure(text=content)
    btn.place(x=390,y=409)
    
    def xuly_1():
        for i in range(n):
            print (threading.current_thread().name, 'icon')
            btn.configure(text="...")
            time.sleep(0.5)
            print (threading.current_thread().name, 'Speak')
            btn.configure(text=content)
            time.sleep(0.75)
            if i==n-1:
                window.quit()
                
    def xuly_2():
        print (threading.current_thread().name, 'Nói')
        speak(content)
        d.daemon
        t.daemon   
    d = threading.Thread(name='Icon', target=xuly_1)
    t = threading.Thread(name='noichuyen', target=xuly_2)

    d.start()
    t.start()  
    window.mainloop()
#Bot dự báo thời tiết
#%%
#Bot_khongnghe()
def dubaothoitiet(tentp="TPHCM",nhietdotb=0,doam=0,nowday=0, nowmonth=0,nowyear=0,dubao="nang",n=5,f=26,w=325,conten="Trời mưa nặng hạt",hinhanh="01d"):  
    bg_dubaothoitiet = Image.open(f"./72ppi/dubaothoitiet.png")
    Bg_dubaothoitiet = ImageTk.PhotoImage(bg_dubaothoitiet)  
    Bg.configure(image=Bg_dubaothoitiet)
    btn.place_forget()
    btntentp = Button(window, text=tentp,justify="left",bd=0,font=("UVN Dzung Dakao",f),fg="red",bg="#FFF8F3",padx=0,pady=0,height=0)
    btntentp.place(x=490,y=355)
    btnnhietdo = Button(window, text=nhietdotb,justify="left",bd=0,font=("UVN Dzung Dakao",f),fg="red",bg="#FFF8F3",padx=0,pady=0)
    btnnhietdo.place(x=485,y=595)
    btndoam = Button(window, text=doam,justify="left",bd=0,font=("UVN Dzung Dakao",f),fg="red",bg="#FFF8F3",padx=0,pady=0)
    btndoam.place(x=390,y=645)   
    btnngay = Button(window, text=nowday,justify="left",bd=0,font=("UVN Dzung Dakao",f),fg="red",bg="#FFF8F3",padx=0,pady=0)
    btnngay.place(x=350,y=710) 
    btnthang = Button(window, text=nowmonth,justify="left",bd=0,font=("UVN Dzung Dakao",f),fg="red",bg="#FFF8F3",padx=0,pady=0)
    btnthang.place(x=510,y=710) 
    btnnam = Button(window, text=nowyear,justify="left",bd=0,font=("UVN Dzung Dakao",f),fg="red",bg="#FFF8F3",padx=0,pady=0)
    btnnam.place(x=668,y=710)  
    btndubao = Button(window, text=f"Dự báo: {dubao}",justify="left",bd=0,font=("UVN Dzung Dakao",f),fg="red",bg="#FFF8F3",padx=0,pady=0)
    btndubao.place(x=450,y=450)    
    
    img_bg_dubaothoitiet = Image.open(f"./icon_dubaothoitiet/{hinhanh}.png")
    Img_bg_dubaothoitiet = ImageTk.PhotoImage(img_bg_dubaothoitiet)  
    img = Button(window, image=Img_bg_dubaothoitiet,justify="left",bd=2,font=("UVN Dzung Dakao",f),fg="red",padx=0,pady=0)
    img.place(x=300,y=450)  
    
    def xuly_1():
        for i in range(n):
            print (threading.current_thread().name, 'icon')
            icon.configure(image=Icon_botnoi1)
            
            time.sleep(0.5)
            print (threading.current_thread().name, 'Speak')
            icon.configure(image=Icon_botnoi2)
          
            time.sleep(0.75)
            if i==n-2:
                window.quit()
    def xuly_2():
        print (threading.current_thread().name, 'Nói')
        speak(conten)
        d.daemon
        t.daemon   
    d = threading.Thread(name='Icon', target=xuly_1)
    t = threading.Thread(name='noichuyen', target=xuly_2)

    d.start()
    t.start() 
    window.mainloop() 
    btntentp.place_forget()
    btnnhietdo.place_forget()
    btndoam.place_forget()
    btnngay.place_forget()
    btnthang.place_forget()
    btnnam.place_forget()
    btndubao.place_forget()
    img.place_forget()
   
#dubaothoitiet()


