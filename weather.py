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
print()
print()
print("###################################")
print("#     Name of City : " + json_data['name'])
print("#")
print("#    Current Temperature : " + str(round(json_data['main']['temp'] - 273)) + " C")
print("#    Minimum Temperature : " + str(round(json_data['main']['temp_min'] - 273)) + " C")
print("#    Maximum Temperature : " + str(round(json_data['main']['temp_max'] - 273)) + " C")
print("#")
print("#    Mood of Your City : " + json_data['weather'][-1]['main'])
print("###################################")
print()
print()