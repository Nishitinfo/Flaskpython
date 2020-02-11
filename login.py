
from flask import Flask, render_template, redirect, url_for, request
import pymysql.cursors
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    error=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form :

        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MyS
        cursor = pymysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        users = cursor.fetchone()
        if users :
            session['loggedin'] = True
            session['id'] = users['id']
            session['username'] = users['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else :
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

    return render_template('Login.html', error=error)



if __name__ == "__main__" :
    app.run(host='127.0.0.2', port=8000, debug=True)







