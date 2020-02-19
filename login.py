
from flask import Flask, render_template, redirect, url_for, request
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    error=''
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'Test'
    mysql = MySQL(app)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
    # Create variables for easy access
         username = request.form['username']
         password = request.form['password']
    # Check if account exists using MySQL
         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
         cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    # Fetch one record and return result
         users = cursor.fetchone()
    # If account exists in accounts table in out database
         if account :
        # Create session data, we can access this data in other routes
          session['loggedin'] = True
          session['id'] = users['id']
          session['username'] = users['username']
        # Redirect to home page
          return 'Logged in successfully!'
    else :
        # Account doesnt exist or username/password incorrect
        msg = 'Incorrect username/password!'
    # Show the login form with message (if any)

    return render_template('Login.html', error=error)


#
# if __name__ == "__main__" :
#     app.run(host='127.0.0.2', port=8000, debug=True)







