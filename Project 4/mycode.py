import requests

# API key for OpenWeatherMap (you need to sign up on their website to get a free API key)
api_key = 'd143747957e17fd85d71f031be632bfe'

# Base URL for the OpenWeatherMap API
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

# City name for which you want to fetch weather data
city_name = 'New York'

# Complete URL for the API request
url = f"{base_url}q={city_name}&appid={api_key}"

# Send a GET request to the API
response = requests.get(url)

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()

    # Display the weather data
    print(f"Weather in {city_name}:")
    print(f"Temperature: {data['main']['temp']} K")
    print(f"Description: {data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data.")
