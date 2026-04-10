import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=45.0845&longitude=-1.1869&hourly=wind_speed_10m,wind_direction_10m&timezone=Europe%2FBerlin'

response = requests.get(url)
data = response.json()

print(data)
