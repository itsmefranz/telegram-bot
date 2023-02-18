from datetime import datetime
import requests

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
        print("After sorting the said ntegers:")
        print(*nums)

        return "There you go! Did you have fun?"
    
    return "Sorry, I do not understand you"

