from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure SQLAlchemy for MSSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://Fatihkumrulu:Opet2018!@195.87.225.168/OpetBTJokerDb?driver=ODBC+Driver+17+for+SQL+Server'
# Replace 'username', 'password', 'server', and 'database_name' with your MSSQL server details.

db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username


@app.route('/')
def index():
    Creattesttablo()
    return 'Hello, Flask-SQLAlchemy with MSSQL!'

if __name__ == '__main__':
    app.run()

def Creattesttablo():
    db.create_all()

