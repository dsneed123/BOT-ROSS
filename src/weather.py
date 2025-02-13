import requests

 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(API_KEY, city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        return f" {weather_desc}, Temp: {temp}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"
    else:
        error_message = response.json().get("message", "No error message provided")
        return f"Error: Unable to fetch weather for {city}. Reason: {error_message}"

def get_daily_forecast(API_KEY, city):
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast/daily"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial",
        "cnt": 7  # Number of days to forecast
    }
    response = requests.get(forecast_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        forecast_list = data["list"]
        forecast_str = f"7-day forecast for {city}:\n"
        
        for day in forecast_list:
            date = day["dt_txt"]
            weather_desc = day["weather"][0]["description"]
            temp_min = day["temp"]["min"]
            temp_max = day["temp"]["max"]
            forecast_str += f"{date}: {weather_desc}, Min Temp: {temp_min}°F, Max Temp: {temp_max}°F\n"
        
        return forecast_str
    else:
        error_message = response.json().get("message", "No error message provided")
        return f"Error: Unable to fetch forecast for {city}. Reason: {error_message}"

def get_daily_forecast_for_spokane(API_KEY):
   return get_daily_forecast(API_KEY,"Spokane")
def get_weather_for_spokane(API_KEY):
    return get_weather(API_KEY,"Spokane")


