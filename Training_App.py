import sys
from Athlete_Class import Athlete
#Once the name of files is fixed import the classes
def display_menu():
    print("\n--- Personalized Sports Training App ---")
    print("1. Create an Athlete Profile")
    print("2. Create a Workout")
    print("3. Modify Workout")
    print("4. View Workout Summary")
    print("5. Rate Workout")
    print("6. Exit")
def create_athlete():
    name = input("Enter athlete's name: ")
    sport = input("Enter athlete's sport: ")
    age = int(input("Enter athlete's age: "))
    skill_level = input("Enter athlete's skill level: ")
    athlete = Athlete(name, sport, age, skill_level)
    return athlete
def create_workout():
    name = input("Enter workout name: ")
    duration = float(input("Enter workout duration in hours: "))
    calories_burned = float(input("Enter calories burned: "))
    workout_type = input("Enter workout type (e.g., Strength, Cardio): ")
    exercises = {}
#rest is still to be implemented