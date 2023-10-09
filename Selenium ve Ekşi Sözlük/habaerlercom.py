from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import time


try:
    browser = webdriver.Firefox()   ##Firefox("./geckodriver.exe")
    url = "https://www.haberler.com/son-dakika/"
    browser.get(url)
    a=0
    while a<=1 :
      a+=1
      elements = browser.find_elements(By.CLASS_NAME, "hblnBox")
      sayac=0
      with open("sondakikaentries.txt","w",encoding = "UTF-8") as file:
       for element in elements:
        sayac+=1     
        file.write(str(sayac) + ".\n" + element.text + "\n")
        file.write("***********************************\n")
        time.sleep(1)
  
        

    time.sleep(10)
    browser.close()

except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {e}")








