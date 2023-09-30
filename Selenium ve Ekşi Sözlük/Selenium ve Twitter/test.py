from selenium.webdriver.common.by import By
from selenium import webdriver
import loginInfo as twitteruser
import time


browser = webdriver.Firefox()   ##Firefox("./geckodriver.exe")
url = "https://twitter.com/"
browser.get(url)

time.sleep(3)

giris_yap = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div")

giris_yap.click()

print("username start.")
username = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

username.send_keys(twitteruser.username)
print("username end.")

time.sleep(10)

ileri_yap = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
ileri_yap.click()
time.sleep(5)

password = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]")
time.sleep(5)

print("username:{},password:{}".format(username,password))

time.sleep(10)