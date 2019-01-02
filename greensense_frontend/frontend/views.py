from django.shortcuts import render
from django.http import HttpResponse
from frontend.temppredict import temperature
from frontend.firebase0 import firebase_img
import requests
import json
import pyrebase
from frontend.temp import firebase_get
from frontend.weatherforecast import forecast5
from frontend.firebaselogin import firebase_login

from django.core.files.storage import FileSystemStorage

##config = {
#    "apiKey": "AAAAS5jDbs0:APA91bGaHI1TH-y1hqOSI1mJxGTThyVntfaORIqcjzPyWc1aP0rLBuFfdC9qFa9gmWlBBnQvILJvb_JPIkoXXziKmyW86fNKS-MeWQ2JYOypJ5BLOTyjmMBR5B-NCwmM2FBIUpmvjzWI",
#    "authDomain": "green-sense.firebaseapp.com",
#    "databaseURL": "https://green-sense.firebaseio.com",
#    "storageBucket": "green-sense.appspot.com"
#    }


config = {
"apiKey": "AIzaSyDQRfYhRwm9475oZHePdUarjdZJ7AyIYuI",
"authDomain": "smart-irigation.firebaseapp.com",
"databaseURL": "https://smart-irigation.firebaseio.com",
"storageBucket": "smart-irigation.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
smos=""
amos=""
atemp=""
ph=0
# Create your views here.
def index(request):

    if request.GET:
        email = request.GET.get("email", None)
        passw = request.GET.get("pass", None)
        print(email)
        print(passw)
        data1 = {"name": email,"pass":passw}
        print(data1)
        auth = firebase.auth()

        user = auth.sign_in_with_email_and_password(email, passw)
        data = {"name": email}
        db.child("users").push(data, user['idToken'])
        print(user)
        
        #print(ball.val())
        #db.child("users").push(data)
        #firebase_login(email,passw)
        print("-----------")



    return render(request, 'index.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = (filename)
        py_obj=uploaded_file_url
        print(py_obj)
        firebase_img(py_obj)
        return render(request, 'simple_upload.html' ,{'message': "Image Successfully Uploaded!"})

    return render(request, 'simple_upload.html')

def plant_more(request):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city1='Chennai'
    url1 = api_address + city1
    json_data1 = requests.get(url1).json()
    fah1=json_data1['main']['temp_max']
    #t=int(float(atemp))

    data=firebase_get()
    a = data["Data1"]
    print(a)

    b = a[0]
    print(b)
    if b == "1":
	    ph = "HIGH"
    else:
        ph = "LOW"
    print(ph)
    #print(type(a))

    for i in range(0,len(a)):
	       if a[i] == ",":
  	            smos = a[(i+1):(i+5)]
                #print(smos)
    for j in range(0,len(a)):
	       if a[j] == "!":
  	            amos = a[(j+1):(j+6)]
                #print(amos)
    for k in range(0,len(a)):
	       if a[k] == "@":
  	            atemp = a[(k+1):(k+6)]
                #print(atemp)
    for l in range (0,len(a)):
	       if a[l] == ";":
  	            min = a[(l+1):len(a)]
                #minsun = (int(min)*12)/60

    atemp=(float(atemp))
    print(type(atemp))
    T=str(int((atemp+(fah1-273))/2))+" °C"
    A=str(amos)+"%"
    S=str(smos)+"%"
    f=T+" | "+A+" | "+S
    if(T>="0"):
        return render(request,'plant_new.html',{'output':f,'message': "Irrigation Required!"})
    return render(request,'plant_new.html',{'output':f})

def plant_request(request):
    return render(request,'index1.html')
