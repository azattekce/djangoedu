from flask import Flask,render_template,redirect,url_for,request


app = Flask(__name__)
app.secret_key= "ybblog"

if __name__ == '__main__':  
     app.run(host='127.0.0.1', debug=True,port=5005)


@app.route("/azat")
def azat():
   return "Merhaba AZAT BEY"

@app.route("/about")
def about():
    return render_template("about.html")