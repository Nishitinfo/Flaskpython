import os

from flask import Flask, flash, render_template, request, session

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('Registration.html')
    else:
        return "Hello Boss! Logout"

@app.route('/Registration', methods=['POST'])
def Registration():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template('Login.html')
    else:
        flash('wrong password!')
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='127.0.0.1', port=4000)
