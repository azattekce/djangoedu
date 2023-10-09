from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import time


entries=[]
entryCount=0
try:
    browser = webdriver.Firefox()   ##Firefox("./geckodriver.exe")
    url = "https://altin.doviz.com/"
    browser.get(url)
    a=0
    while a<=1 :
      a+=1
      names = browser.find_elements(By.CLASS_NAME, "name")
      values = browser.find_elements(By.CLASS_NAME, "value")
  
      for x,y in zip(names,values):
       print("Adı:{}, Değeri:{}".format(x.text,y.text))
     
       time.sleep(3)
        

    time.sleep(10)
    browser.close()

except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {e}")








