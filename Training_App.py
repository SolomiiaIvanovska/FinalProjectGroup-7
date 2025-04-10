import sys
from Athlete_Class import Athlete
from Exercise_Class import Exercise
from Workout_Class import Workout

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

    print("Enter exercises (Enter 'done' when finished):")
    while True:
        exercise_name = input("Exercise name: ")
        if exercise_name.lower() == 'done':
            break
        sets = int(input(f"Sets for {exercise_name}: "))
        exercises[exercise_name] = sets

    workout = Workout(name, duration, calories_burned, exercises, workout_type)
    return workout
def modify_workout(workout):
    print("\nWhat would you like to do?")
    print("1. Add Exercise")
    print("2. Remove Exercise")
    print("3. Update Exercise Sets")
    choice = int(input("Enter your choice: "))
    if choice == "1":
        exercise_name = input("Enter the exercise name to add: ")
        sets = int(input(f"Enter number of sets for {exercise_name}: "))
        workout.add_exercise(exercise_name, sets)

    elif choice == "2":
        exercise_name = input("Enter the exercise name to remove: ")
        workout.remove_exercise(exercise_name)

    elif choice == "3":
        exercise_name = input("Enter the exercise name to update: ")
        new_sets = int(input(f"Enter the new number of sets for {exercise_name}: "))
        workout.update_sets(exercise_name, new_sets)
def view_workout(workout):
    print("\nWorkout Summary:")
    summary = workout.get_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")
def rate_workout(workout):
    rating = input("Enter workout rating (e.g., Easy, Moderate, Hard): ")
    workout.rate_workout(rating)
def main():
    athlete = None
    workout = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            athlete = create_athlete()
            print("Athlete {athlete.get_name()} created successfully!.")
        elif choice == "2":
            if athlete is not None:
                workout = create_workout()
                print(f"\nWorkout  {workout.name} created successfully!")
            else:
                print("\nYou need to create an athlete profile first!")
        elif choice == '3':
            if athlete is not None:
                modify_workout(workout)
            else:
                print("\nWorkout {workout.name} modified successfully!")
        elif choice == '4':
            if workout is not None:
                view_workout_summary(workout)
            else:
                print("\nNo workout to view. Create a workout first.")
        elif choice == '5':
            if workout is not None:
                rate_workout(workout)
            else:
                print("\nNo workout to rate. Create a workout first.")
        elif choice == 6:
            print("\nThank you for using the Personalized Sports Training App!")
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")
if __name__ == '__main__':
    main()








