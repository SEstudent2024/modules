# 1. Python Modules and Data Handling Assignment
# Objective: The aim of this assignment is to assess your understanding and ability to implement Python modules, 
# both built-in and custom, and to apply data handling techniques using Python's data structures and error handling.

# Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered. - Code Example:

def mood_response(mood):
    mood = mood.lower()  
    if mood == "happy":
        return "That's great! Keep spreading positivity!"
    elif mood == "sad":
        return "I'm sorry to hear that. I hope things get better soon."
    elif mood == "excited":
        return "Wow, sounds like you've got some awesome energy!"
    elif mood == "angry":
        return "Take a deep breath. It's going to be okay."
    else:
        return "That's an interesting mood! Stay balanced."
  

# Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) 
# and return a corresponding custom message.

