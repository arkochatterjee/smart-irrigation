import pyowm

  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
def temperature(city):
    owm = pyowm.OWM('3f9016bb3dfa9458c4682e4ed23a43e6')
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    #print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

                              # Weather details
    w.get_wind()                  # {'speed': 4.6, 'deg': 330
    w.get_humidity()              # 87
    a=w.get_temperature('celsius')
    return(a)  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    #return(a['temp'])
