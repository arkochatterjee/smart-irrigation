import pyrebase

config = {
"apiKey": "AAAAS5jDbs0:APA91bGaHI1TH-y1hqOSI1mJxGTThyVntfaORIqcjzPyWc1aP0rLBuFfdC9qFa9gmWlBBnQvILJvb_JPIkoXXziKmyW86fNKS-MeWQ2JYOypJ5BLOTyjmMBR5B-NCwmM2FBIUpmvjzWI",
"authDomain": "green-sense.firebaseapp.com",
"databaseURL": "https://green-sense.firebaseio.com",
"storageBucket": "green-sense.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def firebase_get():



    storage = firebase.storage()

    #data = {"text": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"name": a}
    #db.child("plant").push(data)
    #user = db.child("arduino").get()
    #users = db.child("arduino").get()
    #for user in all_users.each():
        #print(user.key()) # Morty
    #print(user.val()) # {name": "Mor.keytimer 'Morty' Smith"}
    print(db.child("arduino").get().val())
    return(db.child("arduino").order_by_key().limit_to_last(1).get())



firebase_get()
#my_stream = db.child("arduino").stream(stream_handler)


    #storage.child("plant/example.jpg").put("a")
#firebase_get('a')
