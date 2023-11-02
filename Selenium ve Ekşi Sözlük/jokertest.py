from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_py as chrom
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Firefox()  ##Firefox("./geckodriver.exe")
url = "https://joker-test.opetcloud.net"
browser.get(url)


