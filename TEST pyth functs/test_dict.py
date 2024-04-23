user_input = input("Enter a note here: ")
user_input = user_input.lower()

note_dict = {"c":0, "d":2, "e":4}

print(note_dict.get(user_input))