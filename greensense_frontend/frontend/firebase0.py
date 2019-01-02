import pyrebase
import firebase_admin
from firebase_admin import credentials
from datetime import datetime

def firebase_img(a):


    config = {
    "apiKey": "AAAAS5jDbs0:APA91bGaHI1TH-y1hqOSI1mJxGTThyVntfaORIqcjzPyWc1aP0rLBuFfdC9qFa9gmWlBBnQvILJvb_JPIkoXXziKmyW86fNKS-MeWQ2JYOypJ5BLOTyjmMBR5B-NCwmM2FBIUpmvjzWI",
    "authDomain": "green-sense.firebaseapp.com",
    "databaseURL": "https://green-sense.firebaseio.com",
    "storageBucket": "green-sense.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    storage = firebase.storage()

    #data = {"text": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"name": a}
    #db.child("plant").push(data)
    print(a)

    storage.child("plant/"+a).put("/media/arkochatterjee/MISC/GitHub/Green-Sense-VIT/green-sense/greensense_frontend/media/"+a)
