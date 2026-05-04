from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = sqlite3.connect('database.db')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = ? AND Password = ?", (username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successful!')
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = 'incorrect Credentials. Kindly check'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')