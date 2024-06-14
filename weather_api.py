import openmeteo_requests
from datetime import datetime

import requests_cache
import pandas as pd
from retry_requests import retry


class WeatherAPI:

    def __init__(self):
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        self.client = openmeteo_requests.Client(session=retry_session)

    # Function to format temperature with unit
    def format_temperature(self, value):
        return f"{value:.2f}°C"

    # Function to format rain/snowfall with unit
    def format_precipitation(self, value):
        return f"{value:.2f}mm"

    # Function to format cloud cover with unit
    def format_cloud_cover(self, value):
        return f"{value:.2f}%"

    # Function to format current time
    def format_current_time(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    # Function to get current weather data string
    def get_current_weather_string(self, response):
        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()
        current_is_day = int(current.Variables(1).Value())
        current_rain = current.Variables(2).Value()
        snowfall = current.Variables(3).Value()
        cloud_cover = current.Variables(4).Value()

        weather_string = (
            f"Timezone: {response.Timezone()}\n"
            f"Current Time: {self.format_current_time()}\n"
            f"Current temperature: {self.format_temperature(current_temperature_2m)}\n"
            f"Daylight: {current_is_day}\n"  # 1 means daytime
            f"Rain: {self.format_precipitation(current_rain)}\n"
            f"Snowfall: {self.format_precipitation(snowfall)}\n"
            f"Cloud cover: {self.format_cloud_cover(cloud_cover)}\n"
        )
        return weather_string

	#def get_current_fragmented_weather_string(self, response):
		#weather_string_fragmented = (
		# 		f"Rain: {self.format_precipitation(current_rain)}\n"
		#		f"Snowfall: {self.format_precipitation(snowfall)}\n"
		#		)
		#return weather_string_fragmented

    # Function to fetch and format weather data
    def get_weather_data(self, latitude, longitude):
        # Define weather variables to request
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "is_day", "rain", "snowfall", "cloud_cover"],
            "timezone": "auto",
        }

        # Fetch weather data
        responses = self.client.weather_api(url="https://api.open-meteo.com/v1/forecast", params=params)

        # Process first location (assuming single location)
        response = responses[0]

        # Return formatted weather string
        return self.get_current_weather_string(response)


# Example usage
weather_api = WeatherAPI()
weather_data = weather_api.get_weather_data(latitude=45.8144, longitude=15.978)
print(weather_data)