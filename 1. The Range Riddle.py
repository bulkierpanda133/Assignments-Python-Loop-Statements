#task 1
import random
import time



name = input("whats is your name\n")

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Relaxed"]
while True:
    for i in range(len(days_of_week)):
        mood = random.choice(moods)
        print(f"On {days_of_week[i]}, {name} was feeling {mood}.")
        time.sleep(1)

    user_input = input(f"{name} do you want to reset the moods for the week? (yes/no)\n").lower()
    if user_input != 'yes':
     print(f"goodbye {name}!")
     break