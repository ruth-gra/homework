mood = input("Enter your current mood: ")

if mood == "happy" or mood == "Happy":
    print("It is great to see you happy!")
elif mood == "nervous" or mood == "Nervous":
    print("Take a deep breath 3 times.")
elif mood == "excited" or mood == "Excited":
    print("Chill, mate")
elif mood == "sad" or mood == "Sad":
    print("It gonna be fine")
elif mood == "relaxed" or mood == "Relaxed":
    print("Carry on!")
else:
    print("Please choose between happy, nervous, sad, excited, relaxed")