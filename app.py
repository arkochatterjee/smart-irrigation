from flask import Flask,request,render_template,redirect,url_for,Markup
import pyrebase
import json
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
app = Flask(__name__)


config = {
"apiKey": "AIzaSyDQRfYhRwm9475oZHePdUarjdZJ7AyIYuI",
"authDomain": "smart-irigation.firebaseapp.com",
"databaseURL": "https://smart-irigation.firebaseio.com",
"storageBucket": "smart-irigation.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route('/')
def index():
   return render_template('index1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name=request.form['name']
            print(name)
    return render_template('login.html')

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name=request.form['name']
            password=request.form['password']
            print(name)
            print(password)
            auth = firebase.auth()
            try:
                user = auth.sign_in_with_email_and_password(name, password)
                data = {"name": name}
                db.child("users").push(data, user['idToken'])
                return redirect(url_for('adminPanel'))
            except Exception as e:
                print(e)
    return render_template('loginadmin.html')

@app.route('/memberLogin', methods=['GET', 'POST'])
def memberLogin():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name=request.form['name']
            password=request.form['password']
            print(name)
            print(password)
            auth = firebase.auth()
            try:
                user = auth.sign_in_with_email_and_password(name, password)
                data = {"name": name}
                db.child("users").push(data, user['idToken'])
                return redirect(url_for('adminPanel'))
            except Exception as e:
                print(e)
    return render_template('memberLogin.html')


@app.route('/adminPanel')
def adminPanel():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)

    # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )

    data = [trace]
    print(data)
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return render_template('chart1.html',graphJSON=graphJSON)

if __name__ == '__main__':
   app.run(debug=True)
