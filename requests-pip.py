import requests

try:

    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=20.659698&lon=-103.349609&appid=079b88a7c40541404923eb1416b5194c')

    print(response.json())

#except requests.exceptions.RequestException as e:
 #   print("Upsi, an error occurred")
 #   print(e)

except:
    print("Woopsi, an error occurred")
    