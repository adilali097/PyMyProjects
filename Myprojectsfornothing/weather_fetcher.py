import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("cod") != 200:
        print("City not found or API error")
        return
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description']}")

if __name__ == '__main__':
    city = input("Enter city: ")
    get_weather(city)
