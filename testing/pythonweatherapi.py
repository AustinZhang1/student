import requests
import json
import time
from datetime import date
from flask import Flask, render_template


response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=33.014252&longitude=-117.121288&hourly=temperature_2m,precipitation_probability&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,precipitation_hours&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles")
#print(response.status_code)
#print(response.json())
weather = response.json()
print(weather)
def printweather(weather):
    counter = 0
    temps = []
    precipitation = []
    for x in weather["hourly"]["temperature_2m"]:
        temps.append(x)
    for x in weather["hourly"]["precipitation_probability"]:
        precipitation.append(x)
    print(dates)
    print(temps)
    print(precipitation)
    for i in range(7):
        print("Date:",dates[i])
        for i in range(24):
            print(f"The temperature at {i} o'clock is {temps[counter]} degrees.")
            print(f"The chance of precipitation at {i} o'clock is {precipitation[counter]}%\n")
            counter += 1

printweather(weather)



#print(weather["hourly"]["temperature_2m"][19])
#print("\n\n\n\n\n\n\n")
#print(weather)

'''
hourlyinfo = response.get('hourly')
temps = hourlyinfo.get("temperature_2m")
print(temps[0])
'''