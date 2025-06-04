# Project 1: Calculator CLI
# Description: A simple command-line calculator for basic arithmetic operations.
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    a = float(input("Enter first number: "))
    op = input("Enter operator: ")
    b = float(input("Enter second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator")

if __name__ == '__main__':
    calculator()

"""
README.md
# Calculator CLI
A simple Python command-line calculator that supports basic operations: +, -, *, /

## How to Run
```
python calculator.py
```

## Features
- Accepts two numbers and an operator
- Performs addition, subtraction, multiplication, or division
"""

# Project 2: To-Do List
# Description: A CLI-based To-Do list that stores tasks in a text file.
def main():
    while True:
        print("\nTo-Do List Options:\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a task: ")
            with open("tasks.txt", "a") as f:
                f.write(task + "\n")
        elif choice == '2':
            try:
                with open("tasks.txt", "r") as f:
                    tasks = f.readlines()
                    for i, task in enumerate(tasks):
                        print(f"{i + 1}. {task.strip()}")
            except FileNotFoundError:
                print("No tasks found.")
        elif choice == '3':
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()

"""
README.md
# To-Do List CLI
A simple to-do list application that runs in the terminal.

## How to Run
```
python todo.py
```

## Features
- Add tasks
- View tasks
- Stores tasks in a text file
"""

# Project 3: Random Password Generator
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))

"""
README.md
# Password Generator
Generates secure random passwords using Python's standard library.

## How to Run
```
python password_generator.py
```

## Features
- Customizable password length
- Uses letters, numbers, and symbols
"""

# Project 4: QR Code Generator
import qrcode

def create_qr(text):
    img = qrcode.make(text)
    img.save("qrcode.png")
    print("QR Code saved as qrcode.png")

if __name__ == '__main__':
    data = input("Enter text or URL: ")
    create_qr(data)

"""
README.md
# QR Code Generator
Generate QR codes from text or URLs.

## How to Run
```
pip install qrcode[pil]
python qr_generator.py
```

## Features
- Converts text/URL into QR code
- Saves output as an image
"""

# Project 5: Weather Fetcher (using OpenWeatherMap API)
import requests

def get_weather(city):
    API_KEY = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("cod") != 200:
        print("City not found")
        return
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description']}")

if __name__ == '__main__':
    city = input("Enter city: ")
    get_weather(city)

"""
README.md
# Weather Fetcher
Fetch current weather using OpenWeatherMap API.

## How to Run
```
pip install requests
python weather.py
```

## Requirements
- Get an API key from [OpenWeatherMap](https://openweathermap.org/api)

## Features
- Displays temperature and weather condition of the entered city
"""
