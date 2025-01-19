import requests

try:

    response = requests.get('https://api.openweathermap.org/data/2.5/weather?units=metric&lat=20.659698&lon=-103.349609&appid=079b88a7c40541404923eb1416b5194c')

except:
    print("Woopsi, an error occurred")

response_weatherjson = response.json()

#print(response_weatherjson["main"]["temp"])

temp = response_weatherjson["main"]["temp"]
temp_min = response_weatherjson["main"]["temp_min"]
temp_max = response_weatherjson["main"]["temp_max"] 
feels_like = response_weatherjson["main"]["feels_like"]

print(f"Temperatura en Guadalajara: {temp}°C")
print(f"Temperatura mínima en Guadalajara: {temp_min}°C")
print(f"Temperatura máxima en Guadalajara: {temp_max}°C")
print(f"Se siente como: {feels_like}°C")

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_weather()

    #def get_weather(self):
     #   response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=079b88a7c40541404923eb1416b5194c')
     #   response_weatherjson = response.json()
     #   temp = response_weatherjson["main"]["temp"]
     #   temp_min = response_weatherjson["main"]["temp_min"]
     #   temp_max = response_weatherjson["main"]["temp_max"] 
     #   feels_like = response_weatherjson["main"]["feels_like"]
     #   print(f"Temperatura en {self.name}: {temp}°C")
     #   print(f"Temperatura mínima en {self.name}: {temp_min}°C")
     #   print(f"Temperatura máxima en {self.name}: {temp_max}°C")
     #   print(f"Se siente como: {feels_like}°C")

    def get_weather(self):
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=079b88a7c40541404923eb1416b5194c')
        except:
            print("Woopsi, an error occurred")
        response_weatherjson = response.json()
        self.temp = response_weatherjson["main"]["temp"]
        self.temp_min = response_weatherjson["main"]["temp_min"]
        self.temp_max = response_weatherjson["main"]["temp_max"] 
        self.feels_like = response_weatherjson["main"]["feels_like"]
        
    def print_weather(self):   
        print(f"Temperatura en {self.name}: {self.temp}°C")
        print(f"Temperatura mínima en {self.name}: {self.temp_min}°C")
        print(f"Temperatura máxima en {self.name}: {self.temp_max}°C")
        print(f"Se siente como: {self.feels_like}°C")

City1 = City("Guadalajara", 20.67666667, -103.34750000)
#City2 = City("Hayward", 37.66882, -122.0808)
#City3 = City("San Francisco", 37.7749, -122.4194)

#City3.get_weather()
#City2.get_weather()

City1.print_weather()

City2 = City("Hayward", 37.66882, -122.0808)
City2.print_weather()


#EXERCISE

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units

    def get_weather(self):
       response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=079b88a7c40541404923eb1416b5194c')
       response_weatherjson = response.json()
       temp = response_weatherjson["main"]["temp"]
       temp_min = response_weatherjson["main"]["temp_min"]
       temp_max = response_weatherjson["main"]["temp_max"] 
       feels_like = response_weatherjson["main"]["feels_like"]
       units_symbol = "°C"
       if self.units == "imperial":
           units_symbol = "°F"
       print(f"Temperatura en {self.name}: {temp}{units_symbol}")
       print(f"Temperatura mínima en {self.name}: {temp_min}{units_symbol}")
       print(f"Temperatura máxima en {self.name}: {temp_max}{units_symbol}")
       print(f"Se siente como: {feels_like}{units_symbol}")


City1 = City("Guadalajara", 20.67666667, -103.34750000)
City2 = City("Hayward", 37.66882, -122.0808)
City3 = City("San Francisco", 37.7749, -122.4194)
City4 = City("New York", 40.7128, -74.0060)

City3.get_weather()
City4.get_weather()

#CHALLENGE

import json

thestr = """
{
	"title":"Intermediate Python",
	"students": [
		{
			"name":"Nick",
			"scores": [
				56,
				73,
				68,
				84
			]
		},
		{
			"name":"Jane",
			"scores": [
				88,
				74,
				91,
				73
			]
		},
		{
			"name":"Mark",
			"scores": [
				93,
				66,
				52,
				33
			]
		}
	]
}
"""
json_course_data = json.loads(thestr)

def get_scores():
	first_test_scores = []
	return first_test_scores
	
def get_scores():
    first_test_scores = []
    for student in json_course_data["students"]:
        first_test_scores.append(student["scores"][0])
    return first_test_scores


print(get_scores())



