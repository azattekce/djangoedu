from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_py as chrom
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Firefox()  ##Firefox("./geckodriver.exe")
url = "https://joker-test.opetcloud.net"
browser.get(url)

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
    element1= WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "i0118"))
    )    

    element2= WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    ) 
    

    username=browser.find_element(By.XPATH,"//*[@id='i0116']")
    username.send_keys("JOKERCLOUDTSTUSR@opetonline.onmicrosoft.com")
    time.sleep(1)
    nextbtn =browser.find_element(By.XPATH,"//*[@id='idSIButton9']")
    nextbtn.click()
    time.sleep(2)
    password=browser.find_element(By.XPATH,"//*[@id='i0118']")
    password.send_keys("P783H3q6Kw9&")
    time.sleep(2)

    login = browser.find_element(By.XPATH,"//*[@id='idSIButton9']")
    login.click()

 
   

    time.sleep(2)    

    ok = browser.find_element(By.XPATH,"//*[@id='idSIButton9']")
    ok.click()
    time.sleep(2)

    element3= WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "SalesAllView"))
    )
    salesview_page = browser.find_element(By.XPATH,"//*[@id='SalesAllView']")
    salesview_page.click()
  



    plakaNo = browser.find_element(By.ID,"PlakaNo")
    checkStartDate = browser.find_element(By.XPATH,"//*[@id='CheckStartDate']")
    checkEndDate = browser.find_element(By.ID,"CheckEndDate")

    

    saleTypeId = browser.find_element(By.ID,"SaleTypeId")
    salesAllViewSearchFormBtn = browser.find_element(By.ID,"salesAllViewSearchFormBtn")



    startDate = "01.06.2023"
    checkStartDate.clear()
    time.sleep(2) 
    checkStartDate.send_keys(startDate)
   

    endDate = "16.06.2023"
    checkEndDate.clear()
    time.sleep(2)     
    checkEndDate.send_keys(endDate)

    
    saleTypeId.send_keys("0")
    plateNo = "1053TEST53"
    plakaNo.send_keys(plateNo)
    


    salesAllViewSearchFormBtn.click()
    time.sleep(100)

finally:
    browser.quit()