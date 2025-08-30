import requests

API_KEY = "{YOUR_API_KEY}"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter city name (or tyoe 'exit' to close app): ")

    if city.lower() == "exit":
        print("Goodbye!")
        break

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"🌤️ Weather in {city}: {temp}°C, {description}")
    else:
        print("City not found or error fetching data.")

