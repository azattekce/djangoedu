import requests

from bs4 import BeautifulSoup

url = "https://www.haberler.com/son-dakika/"

response = requests.get(url)
print("Reposne:{}".format(response))
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

times = soup.find_all("div",{"class":"hblnTime"})
contents = soup.find_all("span",{"class","hblnContent"})

div_tags = soup.find_all('div', class_='hblnImage') 
    
   
srcs=[]
for div in div_tags:
    img_tags = div.find_all('img') 
    for img in img_tags:
       srcs.append(img.get('src'))


for time,content,imgsrc in zip(times,contents,srcs):

     print("time: {} content  : {} Resim Adresi:{}".format(time.text,content.text,imgsrc))

 
  


