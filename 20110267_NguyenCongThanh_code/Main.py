
import os
#import pyttsx3
import random as rd
import playsound
import speech_recognition as sr
import time
#import sys
#import ctypes
import wikipedia
import datetime
#import json
import re
import webbrowser
import smtplib
import requests
#import urllib
#import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from Giaodien_chinh import *
# from open_app_function import *
# some_file.py
# import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.append(1, './Học cách chào hỏi/Học cách chào của con người.py')


wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()


# %%
def speak(text):
    print("Bot: {}".format(text))
    sound=gTTS(text,lang="vi",slow=False)
    sound.save("sound.mp3")
    playsound.playsound('sound.mp3',True)
    
    os.remove("sound.mp3")
# %%
def get_audio(limmit_timed=4):
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
# %%

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")

# %%
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        Bot_noi(4,f"Chào buổi sáng {name}. Chúc bạn một ngày tốt lành")
        #speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        #speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
        Bot_noi(4,f"Chào buổi chiều {name}. Bạn đã dự định gì cho chiều nay chưa")
    else:
        #speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
        Bot_noi(4,f"Chào buổi tối bạn {name}. Bạn đã ăn tối chưa nhỉ.")
# %%
def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
# %%
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False
# %%
def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)

# %%
def current_weather():
    #speak("Anja muốn biết bạn muốn xem thời tiết ở đâu ạ")
    Bot_noi(3,"Anja muốn biết bạn muốn xem thời tiết ở đâu ạ")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
   # Bot_langnghe(4,"Anja đang nghe bạn nói")
    city = get_text()#tên thành phố
    #tên thành phố
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]#nhiệt độ int độ C
        current_pressure = city_res["pressure"]#
        current_humidity = city_res["humidity"] # độ ẩm int %
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        binhluan=""
        city_wea=data["weather"][0]["icon"]  
        if city_wea =="01d" or  city_wea =="01n":
            binhluan="Bầu trời hôm nay quang đãng, rất thích hợp để bạn ra ngoài hít không khí trong lành, đừng để cảm nắng nhé"
        elif city_wea =="02d" or  city_wea =="02n":
            binhluan="Trời có vài đám mây, có thể bạn sẽ không nóng lắm "
        elif city_wea =="03d" or  city_wea =="03n":
            binhluan="Trời vài đám mây rải rác, vẫn rất dễ chịu "
        elif city_wea =="04d" or  city_wea =="04n":
            binhluan=" Hôm nay có thể có mưa, khi ra đường bạn nên chuẩn bị 1 chiếc ô hoặc áo mưa đễ tránh bị cảm nhé "  
            
        content = f"""
        Anya chào bạn
        Với yêu cầu dự báo thời tiết của {city} hôm nay, là ngày {now.day} tháng {now.month} năm {now.year} dương lịch
        , thì anya dự đoán là,
        Nhiệt độ trung bình sẽ là {current_temperature} độ C
        và độ ẩm là {current_humidity}%,
        Như vậy thì anya khuyên bạn {binhluan}
        ."""
       # xulygiaodienthoitiet(city,current_temperature,current_humidity,now.day,now.month,now.year,"nang",65,26,335,content)
        dubaothoitiet(city,current_temperature,current_humidity,now.day,now.month,now.year,weather_description,15,26,335,content,city_wea)
        time.sleep(20)

    else:
        Bot_khongnghe(4,"Rất tiết Anja không tìm thấy địa chỉ của bạn, bạn nói lại nha")
        #speak("Không tìm thấy địa chỉ của bạn")
        
#current_weather()    
#xulygiaodienthoitiet()
# %%
def play_song():
    #speak('Xin mời bạn chọn tên bài hát')
    Bot_noi(3,'Xin mời bạn chọn tên bài hát')
   
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    #speak("Bài hát bạn yêu cầu đã được mở.")
    Bot_noi(4,f"Anja đã giúp bạn mở bài hát {mysong},chúc bạn nghe vui vẻ")
#play_song()
#%% Hỏi giờ
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        #speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
        Bot_noi(3,f"Bây giờ là {now.hour} giờ {now.minute} phút")
    elif "ngày" in text:
        Bot_noi(5,f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}, ngày hôm nay rất thích hợp đi chơi ")
        #speak("Hôm nay là ngày %d tháng %d năm %d" %
              #(now.day, now.month, now.year))
    else:
        Bot_khongnghe(3,"Anja chưa hiểu ý của bạn. Bạn nói lại được không?")

#%% Chạy ứng dụng
def open_app(text):
    try:
    #Các ứng dụng Microsoft Office
        if "word" in text:
            speak("Đang mở Microsoft Word.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word")
        elif "excel" in text:
            speak("Đang mở Microsoft Excel.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel")    
        elif "powerpoint" in text:
            speak("Đang mở Microsoft PowerPoint.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint")
        elif "edge" in text:
            speak("Đang mở Microsoft Excel.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel") 
        elif "edge" in text:
            speak("Đang mở Microsoft Edge.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Edge")
        elif "note" in text:
            speak("Đang mở Microsoft OneNote 2016.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote 2016")
        elif "outlook" in text:
            speak("Đang mở Microsoft Outlook.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook")
        elif "access" in text:
            speak("Đang mở Microsoft Access.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Access")
        elif "publisher" in text:
            speak("Đang mở Microsoft Publisher.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Publisher")
        elif "skype" in text:
            speak("Đang mở Skype for Business.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Skype for Business")
        elif "health" in text:
            speak("Đang mở PC Health Check.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PC Health Check")    
        #Các ứng dụng của người dùng
        #Note: Nếu chuyển máy khác phải thay đổi tên người dùng trong các đường dẫn dưới
        elif "chrome" in text:
            speak("Đang mở Google Chrome.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome")
        elif "cốc cốc" in text:
            speak("Đang mở Cốc Cốc.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Cốc Cốc")
        elif "studio" in text:
            speak("Đang mở Visual Studio 2019.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2019")
        elif "SQL" in text:
            speak("Đang mở My SQL.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Workbench 8.0 CE")        
        elif "unikey" in text:
            speak("Đang mở Unikey.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\UniKey\UniKey")   
        elif "task manager" in text:
            speak("Đang mở Task Manager.....")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\System Tools\Task Manager")                 
        else:
            Bot_khongnghe(3,"Bạn chưa cài đặt ứng dụng này...")
            #speak("Bạn có muốn cài đặt ứng dụng này?")
            #text = get_text()
            #while True:
            #    if "có" in text:
            #        #lệnh mở trang web tìm kiếm ứng dụng đó
            #        break
            #    elif "không" in text:
            #        break
            #    else:
            #        speak("Bot không nghe rõ. Mời bạn nói lại...")
    except OSError as err:
       # print("OS error: {0}".format(err)) 
        Bot_khongnghe(2,f"OS error: {err}")
        
# %%
def help_me(): 
    Bot_noi(3,"Anja có thể giúp bạn:")
    Bot_noi(2,"Chào hỏi")
    Bot_noi(2,"Hiển thị giờ")
    Bot_noi(2,"Dự đoán giá nhà")
    Bot_noi(3,"Mở website, application, ứng dụng")
    Bot_noi(2,"Tìm kiếm trên Google")
    Bot_noi(2,"Dự báo thời tiết")
    Bot_noi(2,"Mở video nhạc")
    Bot_noi(2,"Tạo danh sách công việc")
#%% HỌC LỜI CHÀO
def chao_hoi_khi_bat_dau():
    Bot_noi(1,'...')
    hoc_chao_hoi(get_audio()) # Tiếp thu lời chào từ con người và
    # nhớ để lần sau chào lại người khác
    result = pd.read_csv('datasets\Loi_chao.csv')
    chao = rd.choice(result['LoiChao'].values)
    Bot_noi(2,chao)
#%%
def hoc_chao_hoi(greeting):
    result = pd.read_csv('datasets\Loi_chao.csv')
    C = {'LoiChao': [greeting]}
    df = pd.DataFrame(C, columns= ['LoiChao'])
    df_new = pd.concat([result, df], ignore_index=True)
    df_new.to_csv ('datasets\Loi_chao.csv', index = None, header=True)

# %%
from Du_doan_gia_nha import *
from ToDoList import *
def assistant():
    chaomung()
    chao_hoi_khi_bat_dau()
    Bot_noi(3,'Anja muốn biết tên bạn là gì?')
    name = get_text()
    if name:
        #speak("Chào bạn {}".format(name))
        Bot_noi(3,f'Quả là một cái tên đẹp, không biết {name} cần anja giúp gì cho bạn không?')
        i=0
        while True:
            if i==0:
                i=1
            else:
                Bot_noi(3,f"{name} cần Anja giúp gì nữa không?")
                
            text = get_text()
            
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "hẹn gặp lại" in text or "bái bai"  in text:
                stop(name)
                break
            elif "có thể làm gì" in text:
                help_me()
            elif "chào" in text:
                Hienthithongtinngheduoc(2,text)
                hello(name)
            elif "giờ" in text:
                Hienthithongtinngheduoc(2,text)
                get_time("giờ")
            elif "ngày" in text:
                Hienthithongtinngheduoc(2,text)
                get_time("ngày")
            elif "mở" in text:
                if 'tìm' in text:
                    open_google_and_search(text)
                elif "." in text:
                    open_website(text)
                else :
                    open_app(text)           
            elif "thời tiết" in text:
                Hienthithongtinngheduoc(1,text)
                current_weather()
            elif "giá nhà" in text:
                Hienthithongtinngheduoc(2,text)
                doan_gia_nha(test_set)
            elif "danh sách" in text:
                Hienthithongtinngheduoc(2,text)
                ToDoList()
            elif "nhạc" in text:
                Hienthithongtinngheduoc(1,text)
                play_song()
            else:
                Bot_khongnghe(6,f"Anja không hiểu câu nói này của bạn, bạn có thể yêu cầu lại được không?")
                i=0

assistant()


# %%
