import requests
import json

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=32.7157&longitude=-117.1647&hourly=temperature_2m,precipitation_probability,precipitation,rain&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum&temperature_unit=fahrenheit&windspeed_unit=mph&timezone=America%2FLos_Angeles")
print(response.status_code)
print(response.json())
text = json.dumps(obj, sort_keys=True, indent=4)
print(texts)
'''
hourlyinfo = response.get('hourly')
temps = hourlyinfo.get("temperature_2m")
print(temps[0])
'''