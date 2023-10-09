from selenium.webdriver.common.by import By
from selenium import webdriver
import loginInfo as azattekce
import time


browser = webdriver.Firefox()   ##Firefox("./geckodriver.exe")
url = "https://azattekce.pythonanywhere.com/articles/"
browser.get(url)

time.sleep(2)

giris_yap = browser.find_element(By.XPATH,"//*[@id='navbarCollapse']/ul[2]/li[1]/a")

giris_yap.click()

print("username start.")
username = browser.find_element(By.XPATH,"//*[@id='id_username']")
username.send_keys(azattekce.username)
print("username end.")

time.sleep(2)
print("password start.")
password = browser.find_element(By.XPATH,"//*[@id='id_password']")
password.send_keys(azattekce.password)
print("password end.")
time.sleep(2)

print("username:{},password:{}".format(username,password))

ileri_yap = browser.find_element(By.XPATH,"/html/body/div/div/div/form/button")
ileri_yap.click()

hakkimda_tikla = browser.find_element(By.XPATH,"//*[@id='navbarCollapse']/ul[1]/li[1]/a")
hakkimda_tikla.click()
time.sleep(2)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

time.sleep(2)

hakkimda_tikla = browser.find_element(By.XPATH,"//*[@id='navbarCollapse']/ul[1]/li[2]/a")
hakkimda_tikla.click()

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
        
time.sleep(2)

time.sleep(2)

"""Kontrol Pnalei"""

kontrol_tikla = browser.find_element(By.XPATH,"//*[@id='navbarCollapse']/ul[2]/li[1]/a")
kontrol_tikla.click()

time.sleep(2)



makale_tikla = browser.find_element(By.XPATH,"/html/body/div/a")
makale_tikla.click()


print("title start.")
time.sleep(2)
title = browser.find_element(By.XPATH,"//*[@id='id_title']")
title.send_keys("Title Test -1")
print("title end.")

time.sleep(2)
print("content start.")

iframe = browser.find_element(By.TAG_NAME,"iframe")
browser.switch_to.frame(iframe)


ckeditor = browser.find_element(By.CLASS_NAME,".cke_editable .cke_editable_themed .cke_contents_ltr .cke_show_borders")
ckeditor.send_keys("Hello, CKEditor!")

# Switch back to the main content
browser.switch_to.default_content()

print("content end.")


time.sleep(2)
makale_save= browser.find_element(By.XPATH,"/html/body/div[1]/div/div/form/button")
makale_save.click()


time.sleep(2)

browser.close()