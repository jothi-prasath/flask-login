from flask import Flask, render_template, request, redirect, session
from config import USERNAME, PASSWORD

app = Flask(__name__)

@app.route('/')
def home():
    if 'username' in session:
        return redirect('/index')
    else:
        return render_template('login.html', error=False)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        session['username'] = username
        return redirect('/index')
    else:
        return render_template('login.html', error=True)

@app.route('/index')
def success():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()
