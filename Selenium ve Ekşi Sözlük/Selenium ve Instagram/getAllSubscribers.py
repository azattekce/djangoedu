from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import loginInfo


browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")

time.sleep(2)


username = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
password = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)


loginButton = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]")

loginButton.click()



time.sleep(5)
print("Profil start")

_list = browser.find_elements(By.XPATH,"//*[@src='https://scontent-cdg4-1.cdninstagram.com/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=1&_nc_ohc=HAahVpYjX1UAX9SVLbw&edm=AAAAAAABAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AfAu9iY-lY-tCM4jZPvP2-Rkb5j-8YhPZEfYQKnStTmf9w&oe=65240ACF&_nc_sid=000000']")
for x in _list:
    print(" İtem {} \n".format(x))
    print("***************************")



#rofilButton = browser.find_element(By.XPATH,"//*[@id='mount_0_0_k5']/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div")
#profilButton.click()
print("Profil end")





time.sleep(50)

          
browser.close()


