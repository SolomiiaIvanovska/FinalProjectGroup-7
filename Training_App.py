import sys
from Athlete_Class import Athlete #, readData
from Exercise_Class import Exercise
from Workout_Class import Workout

athlete = None

PREDEFINED_WORKOUTS = {
    "Legs": {
        "Beginner": [
            Exercise("Bodyweight Squats", 3, [12, 12, 12], [0, 0, 0]),
            Exercise("Glute Bridges", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Step-ups", 2, [10, 10], [0, 0]),
            Exercise("Wall Sit", 3, [30, 30, 30], [0, 0, 0]),  # seconds
            Exercise("Calf Raises", 2, [15, 15], [0, 0])
        ],
        "Intermediate": [
            Exercise("Goblet Squats", 3, [10, 10, 8], [30, 35, 40]),
            Exercise("Lunges", 3, [10, 10, 10], [15, 15, 15]),
            Exercise("Romanian Deadlifts", 3, [8, 8, 8], [40, 40, 40]),
            Exercise("Bulgarian Split Squat", 3, [8, 8, 8], [20, 20, 20]),
            Exercise("Calf Raises (Weighted)", 3, [15, 15, 15], [20, 20, 20])
        ],
        "Advanced": [
            Exercise("Barbell Squats", 4, [6, 6, 5, 5], [135, 145, 155, 165]),
            Exercise("Deadlifts", 3, [5, 5, 5], [185, 195, 205]),
            Exercise("Walking Lunges", 3, [12, 12, 12], [25, 25, 25]),
            Exercise("Jump Squats", 3, [15, 15, 15], [0, 0, 0]),
            Exercise("Sled Push", 3, [30, 30, 30], [90, 90, 90])
        ]
    },
    "Arms": {
        "Beginner": [
            Exercise("Bicep Curls", 2, [12, 12], [10, 10]),
            Exercise("Tricep Dips (Bench)", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Resistance Band Curls", 2, [15, 15], [0, 0]),
            Exercise("Wall Push-ups", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Overhead Extensions", 2, [12, 12], [10, 10])
        ],
        "Intermediate": [
            Exercise("Dumbbell Bicep Curls", 3, [10, 10, 8], [15, 15, 15]),
            Exercise("Skull Crushers", 3, [10, 8, 8], [20, 25, 25]),
            Exercise("Hammer Curls", 3, [10, 10, 10], [20, 20, 20]),
            Exercise("Overhead Triceps", 3, [10, 10, 10], [25, 25, 25]),
            Exercise("Incline Dumbbell Curls", 3, [8, 8, 8], [15, 15, 15])
        ],
        "Advanced": [
            Exercise("Barbell Curls", 4, [8, 8, 6, 6], [55, 65, 70, 75]),
            Exercise("Weighted Dips", 3, [10, 8, 8], [25, 25, 25]),
            Exercise("Preacher Curls", 3, [8, 8, 8], [50, 50, 50]),
            Exercise("Close Grip Bench Press", 3, [6, 6, 6], [115, 125, 135]),
            Exercise("Cable Triceps Extensions", 3, [10, 10, 10], [40, 45, 50])
        ]
    },
    "Core": {
        "Beginner": [
            Exercise("Crunches", 3, [15, 15, 15], [0, 0, 0]),
            Exercise("Leg Raises", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Plank", 3, [30, 30, 30], [0, 0, 0]),  # seconds
            Exercise("Seated Twists", 3, [20, 20, 20], [0, 0, 0]),
            Exercise("Bird-Dogs", 3, [12, 12, 12], [0, 0, 0])
        ],
        "Intermediate": [
            Exercise("Russian Twists", 3, [20, 20, 20], [10, 10, 10]),
            Exercise("Plank with Shoulder Taps", 3, [20, 20, 20], [0, 0, 0]),
            Exercise("Hanging Leg Raises", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Cable Crunches", 3, [12, 12, 12], [40, 40, 40]),
            Exercise("Side Plank with Reach", 3, [15, 15, 15], [0, 0, 0])
        ],
        "Advanced": [
            Exercise("Weighted Sit-ups", 4, [10, 10, 10, 10], [25, 25, 25, 25]),
            Exercise("Toes to Bar", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Decline Russian Twists", 3, [20, 20, 20], [20, 20, 20]),
            Exercise("Ab Rollouts", 3, [12, 12, 12], [0, 0, 0]),
            Exercise("Dragon Flags", 3, [8, 8, 8], [0, 0, 0])
        ]
    }
}

#athlete = Athlete(readData("Test Athlete.txt"))


while True:
    print("\n--- Personalized Sports Training App Menu ---")
    print("1. Create an Athlete Profile")
    print("2. Add Predefined Workout")
    print("3. View Workout Summary")
    print("4. Rate a Workout")
    print("5. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Enter athlete's name: ")
        sport = input("Enter sport: ")
        age = int(input("Enter age: "))
        skill = input("Enter skill level (Beginner/Intermediate/Advanced): ").capitalize()
        goals_input = input("Enter goal (e.g., Upper Body): ").strip().lower()
        goals = goals_input in ["upper body", "upperbody"]

        # Create new athlete instance
        athlete = Athlete((name, sport, age, skill, [], [], goals))
        print(f"\nAthlete profile for {athlete.get_name()} created successfully!")

    elif choice == "2":
        if not athlete:
            print(" Please create an athlete profile first (Option 1).")
            continue
        category = input("Choose a category (Legs/Arms/Core): ").capitalize()
        skill = athlete.get_skill_level().capitalize()
        if category in PREDEFINED_WORKOUTS and skill in PREDEFINED_WORKOUTS[category]:
            exercises = PREDEFINED_WORKOUTS[category][skill]
            workout = Workout(f"{category} Day", 1.0, 300, {ex.name: ex for ex in exercises}, category)
            print("\nWorkout created:")
            print(workout)
            athlete.add_workout(workout.name)
        else:
            print("Invalid category or skill level.")

    elif choice == "3":
        if not athlete:
            print(" Please create an athlete profile first (Option 1).")
            continue
        print(f"\nName: {athlete.get_name()}")
        print(f"Sport: {athlete.get_sport()}")
        print(f"Age: {athlete.get_age()}")
        print(f"Skill Level: {athlete.get_skill_level()}")
        print("Workouts:")
        athlete.display_workouts()

    elif choice == "4":
        if not athlete:
            print(" Please create an athlete profile first (Option 1).")
            continue
        rating = input("Rate your last workout (Easy, Moderate, Hard): ")
        athlete.log_performance(rating)
        print(f"Workout rated as: {rating}")

    elif choice == "5":
        print("Exiting app.")
        break

    else:
        print("Invalid choice.")
