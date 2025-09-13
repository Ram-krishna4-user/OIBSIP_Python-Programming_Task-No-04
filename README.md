# OIBSIP_Python-Programming_Task-No-04
Here is our task-1 of Oasis Infobyte (Python Programming internship)

# Basic Weather App :

Objective :-- Create a command-line weather app in Python that shows current weather for a city name or ZIP code using a weather API.

Steps Performed :--
1. Take user input (city or ZIP code).
2. Decide URL based on input:
   2.1. If numbers → treat as ZIP code.
   2.2. Else → treat as city name.
3. Send request to OpenWeatherMap API using requests.get().
4. Get JSON response from API.
5. Extract weather info (city, country, temperature, humidity, condition).
6. Print the weather details on the screen.
7. Handle errors if the API key is wrong or location is invalid.

Tools / Libraries Used :-- 
1. Requests → to call the API and get weather data in JSON format.
2. OpenWeatherMap API → the online service that gives the weather data.

Outcome :-- 
1. The program shows: 1.1. City and country name 1.2. Temperature in °C 1.3. Humidity in % 1.4. Weather condition (like cloudy, clear, etc.) 2. If something goes wrong (invalid key, bad location), it shows an error message.

# Console view :
Enter a city name or ZIP code: kolkata

Weather in Kolkata, IN:
🌡️ Temperature: 28.97°C
💧 Humidity: 84%
☁️ Condition: Haze
