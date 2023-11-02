import pypyodbc

connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=195.87.225.168;DATABASE=OpetBTJokerDb;UID=Fatihkumrulu;PWD=Opet2018!')
cursor = connection.cursor()
cursor.execute("select*from [dbo].[Users]")
sonuc = cursor.fetchall()
for i in sonuc:
    print(i)