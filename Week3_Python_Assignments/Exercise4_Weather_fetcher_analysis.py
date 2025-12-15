# Exercise 4: Weather Data Fetcher & Analyzer
# This program fetches real-time weather data using OpenWeatherMap API,
# analyzes the data, displays insights, and logs results into a CSV file.

# Import required libraries
import requests
import csv
from datetime import datetime

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather(city,api_key):
    try:

        # API URL with metric units
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        # Send GET request to API
        response = requests.get(url,timeout=10)
        # Raise error for Bad Http status
        response.raise_for_status()
        # returns a json response
        return response.json()
    
    # Handling any exception gracefully
    except requests.exceptions.HTTPError:
        print("Invalid city name or API error.")
    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"Unexpected error: {e}")    
    
    return None

# Function to analyze weather data
def Analyze_weather(weather_data):
    # Extracting data fields 
    temperature = weather_data['main']['temp']
    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']

    # Determine temperature condition
    if temperature < 10:
        summary = 'Cold (<10 degrees)'
    elif temperature >= 11 and temperature <= 24:
        summary = 'Mild (11- 24 degrees)'
    else:
        summary = 'Hot (>=25 degrees)'
    
    # Add warnings
    if wind_speed > 10:
        summary += "| High wind alert"
    if humidity > 80:
        summary += '| Humid conditions'
    
    return summary

# Function to fetch weather and log data into CSV file
def log_weather(city,filename,api_key):
    # Fetch weather data
    weather_data = fetch_weather(city,api_key)
    # If data fetch failed, exit function
    if weather_data is None:
        return 
    # Analyze weather
    analysis = Analyze_weather(weather_data)
    # Extract data for logging
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Append data to CSV file
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, city, temperature, humidity, wind_speed, analysis])
        
        # Display output
        print(f"Weather Summary for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Analysis: {analysis}")
        print(f"Data logged successfully in '{filename}'")

    except Exception as e:
        print('An Unexpected error {e} occured')

# Main execution
if __name__ == '__main__':
    # Ask user for city name
    city_name = input("Enter the city name: ")

    # API key (replace with your own OpenWeatherMap API key)
    API_KEY = '40303d2b2b0a11aa7d726144715c1fe3'

    # CSV file name
    csv_file = 'weather_log.csv'
    # Write CSV header if file is empty
    try:
        with open(csv_file, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "City", "Temperature(C)", "Humidity(%)", "WindSpeed(m/s)", "Analysis"])
    except FileExistsError:
        pass


    # Log weather data
    log_weather(city_name, csv_file, API_KEY)