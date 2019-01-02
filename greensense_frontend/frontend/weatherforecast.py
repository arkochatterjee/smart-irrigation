import requests
import json

api_address='http://api.openweathermap.org/data/2.5/forecast?appid=0c42f7f6b53b244c78a418f4f181282a&q='
def forecast5(city):
#city = input('City Name :')
    url = api_address + city
    json_data = requests.get(url).json()
#format_add = json_data['base']
#print(json_data)
    temp=json_data["list"][0]["main"]["temp"]
    pressure=json_data["list"][0]["main"]["pressure"]
    humidity=json_data["list"][0]["main"]["humidity"]
    description=json_data["list"][0]["weather"][0]["description"]

    out=str(temp)+" | "+str(pressure)+" | "+str(humidity)+" |   "+str(description)
    return out

#print(a)
