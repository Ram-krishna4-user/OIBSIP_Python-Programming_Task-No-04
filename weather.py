# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 11:47:03 2025

@author: gramk
"""
'''
import requests

# Replace with your OpenWeatherMap API key
API_KEY = "abc123yourrealapikey"
BASE_URL = "http://api.openweathermap.org/data/ 2.5/weather"

def get_weather(location):
    try:
        # Prepare request parameters
        params = {
            "q": location,        # City name or "City,CountryCode"
            "appid": API_KEY,
            "units": "metric"     # Use "imperial" for Fahrenheit
        }

        # Fetch weather data
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check for errors
        if response.status_code != 200:
            print("Error:", data.get("message", "Unable to fetch weather data"))
            return

        # Parse weather data
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        # Display results
        print(f"\nWeather in {city}, {country}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Condition: {condition}\n")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    while True:
        location = input("Enter a city name or ZIP code (or type 'exit' to quit): ").strip()
        if location.lower() == "exit":
            break
        elif not location:
            print("⚠️ Please enter a valid location.")
            continue
        get_weather(location)
        
'''

import requests

def Get_Weather(location, api_key, country_code="us"):
    # Decide if input is ZIP or City
    if location.isdigit():
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={location},{country_code}&appid={api_key}&units=metric"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    response = requests.get(url)
    print("DEBUG:", response.json())
    
    if response.status_code == 200:
        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print(f"\nWeather in {city_name}, {country}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Condition: {condition.capitalize()}")
    else:
        print("❌ Error: Could not fetch weather. Please check your input or API key.")


if __name__ == "__main__":
    api_key = "b122a86cc018e67b8205537f9ee0647d"  # replace with your actual key
    location = input("Enter a city name or ZIP code: ").strip()
    if location:
        Get_Weather(location, api_key)
    else:
        print("⚠️ Invalid input. Please enter a valid city name or ZIP code.")
