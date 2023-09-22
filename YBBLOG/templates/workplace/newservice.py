import requests
from bs4 import BeautifulSoup



class NewsClass:
    def __init__(self, times, contents, srcs):
        self.times = times
        self.contents = contents
        self.srcs = srcs


def getNews():
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

    
    NewsList=[]
    for time,content,imgsrc in zip(times,contents,srcs):
     NewsList.append(NewsClass(time.text,content.text,imgsrc))

    for i in NewsList:
      print("time: {} content  : {} Resim Adresi:{}".format(i.times,i.contents,i.srcs))
    
    return NewsList
   
    
  
 