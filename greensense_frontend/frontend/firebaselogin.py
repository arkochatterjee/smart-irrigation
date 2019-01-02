import pyrebase
import firebase_admin
from firebase_admin import credentials
from datetime import datetime

def firebase_login(email,password):


    config = {
    "apiKey": "AIzaSyDQRfYhRwm9475oZHePdUarjdZJ7AyIYuI",
    "authDomain": "smart-irigation.firebaseapp.com",
    "databaseURL": "https://smart-irigation.firebaseio.com",
    "storageBucket": "smart-irigation.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    storage = firebase.storage()

    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    data = {"name": email}
    results = db.child("users").push(data, user['idToken'])


    #data = {"text": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"name": a}
    #db.child("plant").push(data)
