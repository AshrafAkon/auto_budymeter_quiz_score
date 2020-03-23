#this code is for educational purpose only
#please see the license file for more information
#please install google chrome browser first

from selenium import webdriver
import time
import sys


name = "Your Name" #you have to provide your name, which will be used to submit the answer
score = 10 #your desired score. which can be 1-10


s_link = "https://buddymeter.com/quiz.html?q=XXXXXXX" #the link of buddymeter quiz

try:
    
    if "win" in sys.platform:
        dri = webdriver.Chrome("./chromedriver.exe") #use latest chromedriver
    else:
        dri = webdriver.Chrome("./chromedriver") #use latest chromedriver
    dri.get(s_link)
    time.sleep(5)
    dri.execute_script('answerer_name = "'+name+'";')
    dri.execute_script("score = "+str(score)))

    dri.execute_script("send_score_to_firebase(score);")
    time.sleep(5)
    dri.close()
except:
    print("error")
    try:
        dri.close()
    except:
        print("cant close browser")
