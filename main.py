import mood_responses

mood = input("How are you feeling today? ")
response = mood_responses.mood_response(mood)
print(response)

import text_utils as tu  # Using alias for the module

text = input("Enter some text: ")

reversed_text = tu.reverse_string(text)
capitalized_text = tu.capitalize_string(text)

print(f"Reversed: {reversed_text}")
print(f"Capitalized: {capitalized_text}")
