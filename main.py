import requests
import pandas as pd
import pprint as pp

# define main function to load data from api and save as JSON

def main():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=45.0845&longitude=-1.1869&hourly=wind_speed_10m,wind_direction_10m&timezone=Europe%2FBerlin'
    response = requests.get(url)
    api_data = response.json()
    return api_data

# only run main when script is directly triggered, not when imported

if __name__ == "__main__":
    api_data = main()
    pp.pprint(api_data)

print(api_data["hourly"]["wind_speed_10m"])

hourly = api_data["hourly"]
api_df = pd.DataFrame(hourly)

print(api_df)