import sys
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
import pypyodbc
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps


# Kullanıcı Giriş Decorator'ı
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapın.","danger")
            return redirect(url_for("login"))

    return decorated_function

#isteklerin loglanması 
def request_log(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
              for anahtar, deger in kwargs.items():
               print(f"{anahtar}: {deger}")
              return f(*args, **kwargs)     
    return decorated_function

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
class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")

app = Flask(__name__)
app.secret_key= "ybblog"

def get_db_connection():
    return pypyodbc.connect(
     'DRIVER={SQL Server};SERVER=195.87.225.168;DATABASE=OpetBTJokerDb;UID=Fatihkumrulu;PWD=Opet2018!'
    )


@app.route("/")
def index():
   return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
# Makale Sayfası
@app.route("/articles")
def articles():
    connection = get_db_connection()
    cursor = connection.cursor()
    sorgu = "Select * From Articles"

    result = cursor.execute(sorgu)
    rows=cursor.fetchall()
    if len(rows)> 0:
        articles = rows
        return render_template("articles.html",articles = articles)
    else:
        return render_template("articles.html")

@app.route("/dashboard")
@login_required
def dashboard():
    connection = get_db_connection()
    cursor = connection.cursor()

    sorgu = "Select * From Articles where Author ='{}'".format(session["username"])
    print("Sorgu:",sorgu)
    cursor.execute(sorgu)
    rows=cursor.fetchall()
    print("len(rows)>:",len(rows))
    if len(rows)> 0:
        articles = rows
        return render_template("dashboard.html",articles = articles)
    else:
        return render_template("dashboard.html")
#Kayıt Olma
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        connection = get_db_connection()
        cursor = connection.cursor()

        sorgu = "Insert into users(Name,Email,UserName,Password) VALUES('{}','{}','{}','{}')".format(name,email,username,password)

        cursor.execute(sorgu)
        connection.commit()

        cursor.close()
        flash("Başarıyla Kayıt Oldunuz...","success")
        return redirect(url_for("login"))
    else:
        return render_template("register.html",form = form)
# Login İşlemi
@app.route("/login",methods =["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
       username = form.username.data
       password_entered = form.password.data
       print("form.password.data:",form.password.data)
       connection = get_db_connection()
       cursor = connection.cursor()
       sorgu = "Select * From Users where UserName='{}'".format(username)
       result = cursor.execute(sorgu)

       column_names = [column[0] for column in cursor.description]
       print("Column Names:", column_names)
       rows=cursor.fetchall()
       print("cursor.fetchall().count():", len(rows))

       """for row in cursor.fetchall():
           row_dict = dict(zip(column_names, row))
           print("password:",row_dict["password"],row_dict)
        """
    
       print("password_entered:",password_entered)

       if len(rows)> 0:
         for row in rows:
             row_dict = dict(zip(column_names, row))
             print("password:",row_dict["password"],row_dict)
             if password_entered==row_dict["password"]:
                flash("Başarıyla Giriş Yaptınız...","success")

                session["logged_in"] = True
                session["username"] =row_dict["username"]
                return redirect(url_for("index"))
             else:
                flash("Parolanızı Yanlış Girdiniz...","danger")
                return redirect(url_for("login")) 

       else:
           flash("Böyle bir kullanıcı bulunmuyor...","danger")
           return redirect(url_for("login"))

    
    return render_template("login.html",form = form)

# Detay Sayfası
@app.route("/article/<string:id>")
@request_log
def article(id):
    connection = get_db_connection()
    cursor = connection.cursor()    
    sorgu = "Select * from Articles where Id={}".format(int(id))
    result = cursor.execute(sorgu)
    column_names = [column[0] for column in cursor.description]
    rows=cursor.fetchall()

    if len(rows)> 0:
        for row in rows:
         row_dict = dict(zip(column_names, row))
         article =row_dict
        return render_template("article.html",article = article)
    else:
        return render_template("article.html")
# Logout İşlemi
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
# Makale Ekleme
@app.route("/addarticle",methods = ["GET","POST"])
@request_log
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data

        connection = get_db_connection()
        cursor = connection.cursor()
        sorgu = "Insert into Articles(Title,Author,Content) VALUES('{}','{}','{}')".format(title,session["username"],content)
        cursor.execute(sorgu)
        connection.commit()

        cursor.close()

        flash("Makale Başarıyla Eklendi","success")

        return redirect(url_for("dashboard"))

    return render_template("addarticle.html",form = form)

#Makale Silme
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sorgu = "Select * from Articles where author ='{}' and Id={}".format(session["username"],int(id))

    cursor.execute(sorgu)
    rows=cursor.fetchall()

    if len(rows)> 0:
        sorgu2 = "Delete from Articles where Id ={}".format(int(id))

        cursor.execute(sorgu2)

        connection.commit()

        return redirect(url_for("dashboard"))
    else:
        flash("Böyle bir makale yok veya bu işleme yetkiniz yok","danger")
        return redirect(url_for("index"))
#Makale Güncelleme
@app.route("/edit/<string:id>",methods = ["GET","POST"])
@login_required
def update(id):
   if request.method == "GET":
       connection = get_db_connection()
       cursor = connection.cursor()
       sorgu = "Select * from Articles where author ='{}' and Id={}".format(session["username"],int(id))
       cursor.execute(sorgu)
       column_names = [column[0] for column in cursor.description]
       rows=cursor.fetchall()
      

       if len(rows)==0:
           flash("Böyle bir makale yok veya bu işleme yetkiniz yok","danger")
           return redirect(url_for("index"))
       else:
           form = ArticleForm()
           for row in rows:
            row_dict = dict(zip(column_names, row))  
            form.title.data = row_dict["title"]
            form.content.data = row_dict["content"]

           return render_template("update.html",form = form)

   else:
       # POST REQUEST
       form = ArticleForm(request.form)

       newTitle = form.title.data
       newContent = form.content.data

       sorgu2 = "Update Articles Set title='{}',content='{}' where Id={} ".format(newTitle,newContent,int(id))

       connection = get_db_connection()
       cursor = connection.cursor()

       cursor.execute(sorgu2)

       connection.commit()

       flash("Makale başarıyla güncellendi","success")

       return redirect(url_for("dashboard"))

       pass
# Makale Form
class ArticleForm(Form):
    title = StringField("Makale Başlığı",validators=[validators.Length(min = 5,max = 100)]) 
    content = TextAreaField("Makale İçeriği",validators=[validators.Length(min = 10)])

# Arama URL
@app.route("/search",methods = ["GET","POST"])
def search():
   if request.method == "GET":
       return redirect(url_for("index"))
   else:
       keyword = request.form.get("keyword")

       connection = get_db_connection()
       cursor = connection.cursor()

       sorgu = "Select * from Articles where Title like '%" + keyword +"%'"

       result = cursor.execute(sorgu)

       if result == 0:
           flash("Aranan kelimeye uygun makale bulunamadı...","warning")
           return redirect(url_for("articles"))
       else:
           articles = cursor.fetchall()

           return render_template("articles.html",articles = articles)
if __name__ == "__main__":
    app.run(debug=True)
