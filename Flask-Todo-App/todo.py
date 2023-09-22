from flask import Flask,render_template,redirect,url_for,request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure SQLAlchemy for MSSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://Fatihkumrulu:Opet2018!@195.87.225.168/OpetBTJokerDb?driver=ODBC+Driver+17+for+SQL+Server'
# Replace 'username', 'password', 'server', and 'database_name' with your MSSQL server details.

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
     app.run()


@app.route("/")
def index():
    """db.create_all()
    Todo.query.all()"""
    return render_template("index.html")
@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    """if todo.complete == True:
        todo.complete = False
    else:
        todo.complete = True"""
    todo.complete = not todo.complete

    db.session.commit()
    return redirect(url_for("index"))
@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(title = title,complete = False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))