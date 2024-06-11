import openmeteo_requests
from datetime import datetime

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 45.8144,
	"longitude": 15.978,
	"current": ["temperature_2m", "is_day", "rain"],
	"timezone": "auto"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Current values. The order of variables needs to be the same as requested.
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_is_day = current.Variables(1).Value()
current_rain = current.Variables(2).Value()

now = datetime.now()
#print(f"Timezone {response.Timezone()}")
print(f"Current time {now.strftime("%d/%m/%Y %H:%M:%S")}")
print(f"Current temperature_2m {current_temperature_2m:.2f}°C")
print(f"Current is_day {int(current_is_day)}")
print(f"Current rain {current_rain}mm")



