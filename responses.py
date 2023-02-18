from datetime import datetime
import requests, json

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! How is it going?"
    
    if user_message in ("who are you", "who are you?"):
        return "I am Dani's bot!"
    
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time= now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    if user_message in ("what do you do", "what do you do?", "what are you", "what are you?"):
        return "I am a telegram bot that can converse with users like you! :)"
    
    if user_message in ("can we play a game?", "do u know any games?", "play"):
        print("Input six integers:")
        nums = list(map(int, input().split()))
        nums.sort()
        nums.reverse()
        print("After sorting the said integers:")
        print(*nums)

        return "There you go! Did you have fun?"
    
    if user_message in ("can you help me with this?", "can you help me with this"):
        return "I'm sure we can work something out together"
    
    if user_message in ("trivia"):
        return "There are over 500 million pet cats!"

    if user_message in ("what is the weather today?", "weather"):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = "Philippines"
        API_KEYS = "e0e82e3a8dd5a5ff87b661f85c86f0ba"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEYS
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")
            print(f"Pressure: {pressure}")
            print(f"Weather Report: {report[0]['description']}")
        else:
            print("Error in the HTTP request")

    return "Sorry, I do not understand you"

