import requests
import json

def weather(cityName):
    apiID = "0c42f7f6b53b244c78a418f4f181282a"
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid="+apiID)
    return response


# ---------- Main Program --------
print()
print()
city = input("Enter Your City Name : ")
data = weather(city)
json_data = json.loads(data.text)
print()
print()
print(json_data)
