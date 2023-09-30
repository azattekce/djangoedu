from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import time


entries=[]
entryCount=0
try:
    browser = webdriver.Firefox()   ##Firefox("./geckodriver.exe")
    url = "https://azattekce.pythonanywhere.com/articles/"
    browser.get(url)
    a=0
    while a<=1 :
      a+=1
      elements = browser.find_elements(By.CLASS_NAME, "mt-4")
      print(elements)
      for element in elements:
       print(element.text)
       entries.append(element.text)
       time.sleep(3)
        

    time.sleep(10)
    browser.close()

except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {e}")




with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("***********************************\n")
        entryCount += 1




