from flask import Flask,render_template,request
import requests
import model as jsonconvert
import json

api_key = "7aefe5a60a05973fe5802edd2789731f"

url = "http://data.fixer.io/api/latest?access_key=" + api_key


def index():
    
    try:
        
        response = requests.get(url)
        #app.logger.info(response)

        jsonData = response.json()## Jason datası 
        data=jsonData["rates"] ## Json verisindeki modeli alıyoruz.
        my_rates= json.dumps(data) ## Python nesnelerini JSON biçimine dönüştürmek için kullanılır. 
        print("*********** JSON DATA**********************")
        print(data)



        print("*********** JSON Keys End Value**********************")
        for key in data.keys():
         print("Birim:{},Değer:{}".format(key,jsonData["rates"][key]))

        print("*********** JSON Datasını okuyup class listesine ekleme*********************")
        
        for key in data.keys():
         print("Birim:{},Değer:{}".format(key,jsonData["rates"][key]))




         print("*********** Class Keys**********************")
        mydata=jsonconvert.Root.from_dict(data) ## bu fonksiyonla json nesseni python class nesnesine set ederiz. 
        print("TR:{}\n,USD:{} \n,EUR:{} ".format(mydata.TRY,mydata.USD,mydata.EUR))
       
    except Exception as e:
    # Handle any other exceptions
     print(f"An error occurred: {e}")

    



index()