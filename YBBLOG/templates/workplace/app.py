from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
import newservice as newssrc
import asyncio
import pypyodbc
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

app=Flask(__name__)## __name__ python özel bir tanımdır.
app.secret_key="azattekce"

# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min = 4,max = 25)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min = 5,max = 35)])
    email = StringField("Email Adresi",validators=[validators.Email(message = "Lütfen Geçerli Bir Email Adresi Girin...")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message = "Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız Uyuşmuyor...")
    ])
    confirm = PasswordField("Parola Doğrula")
  

def get_db_connection():
    return pypyodbc.connect(
     'DRIVER={SQL Server};SERVER=195.87.225.168;DATABASE=OpetBTJokerDb;UID=Fatihkumrulu;PWD=Opet2018!'
    )


@app.route("/")
def star():   
    sayi=10
    return render_template("index.html",number=sayi)

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/news")
def news():
  newsList=newssrc.getNews()
  asyncio.run(newssrc.getNewsasync())
  return render_template("news.html",news=newsList)


@app.route("/detail/<string:id>")
def detail(id):
 return "Gelen parametre"+id

@app.route("/db")
def db():
   
    try:
      connection = get_db_connection()
      cursor = connection.cursor()
      cursor.execute('select top 100 *from Users order by Id desc')
      data = cursor.fetchall()
      connection.close()
      
    except  Exception as e:
     print("DB okuma hatası:{}".format(e))
    
    flash("Başarıyla Kayıt Oldunuz...","success")
    return render_template("db.html",data=data)


@app.route("/regitser",methods = ["GET","POST"])
def regitser():
    form = RegisterForm(request.form)
    dataList=[]
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        sorgu = "Insert into users(Name,Email,UserName,Password) VALUES('{}','{}','{}','{}')".format(name,email,username,password)
        print(sorgu)
     

        ##INSERT 
        try:
            ##connection = get_db_connection()
            connection =get_db_connection()
            cursor = connection.cursor()
            cursor.execute(sorgu)
            connection.commit()           
           
        except Exception as e:
            print("Hata:{}".format(e))
        finally:
            cursor.close()
            connection.close()      


          ##OKUMA 
        try:
         
            connection1 = get_db_connection()
            cursor1 = connection1.cursor()
            cursor1.execute('select Name, UserName,Email from Users order by Id desc')
            rows= cursor1.fetchall()
            for row in rows:
             dataList.append(row)   
             print("Name:"+row[0],"SurName:"+row[1],"Email:"+row[2])         
           
        except Exception as e:
            print("Hata:{}".format(e))
        finally:
            cursor1.close()
            connection1.close()    
       
        flash("Başarıyla Kayıt Oldunuz...","success")
        return render_template("regitser.html",form = form,data=dataList)
    else:
        return render_template("regitser.html",form = form,data=dataList)

if(__name__=="__main__"):
  app.run(debug=True)
