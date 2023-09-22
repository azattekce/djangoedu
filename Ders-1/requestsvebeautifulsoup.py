import requests 
from bs4 import BeautifulSoup

url = "https://www.opet.com.tr/"
response = requests.get(url)

print(response)


html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

print("html.parser:{}".format(*soup.find_all()))
print("*********************************")
print(*soup.find_all("div",{"class":"video"}))






