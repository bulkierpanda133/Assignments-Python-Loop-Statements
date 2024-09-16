# task 1
import random



days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Relaxed"]
time_of_day = ['Morning', 'Afternoon', 'Evening']



for day in days_of_week:
    print(f"\nOn {day}:")
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"  - {time}: {mood}")