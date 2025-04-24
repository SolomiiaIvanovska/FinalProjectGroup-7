import sys
from Athlete_Class import Athlete , readData
from Exercise_Class import Exercise
from Workout_Class import Workout
import json
athlete = None
##
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

def get_skill_level_input():
    skill_map = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}
    while True:
        level_input = input("Enter skill level (1-Beginner, 2-Intermediate, 3-Advanced): ").strip()
        level = skill_map.get(level_input) or level_input.capitalize()
        if level in ["Beginner", "Intermediate", "Advanced"]:
            return level
        print("Invalid input. Please enter 1, 2, 3 or the skill level name.")

def create_athlete():
    name = input("Enter athlete's name: ")
    age = int(input("Enter athlete's age: "))
    skill_level = get_skill_level_input()
    goals = input("What are your goals? (Upper body/Lower body/Full body): ").strip().lower() in ["upper", "upper body", "upperbody"]
    return Athlete((name, age, skill_level, [], [], goals))

def generate_workout(skill_level, category):
    if category not in PREDEFINED_WORKOUTS:
        print("Workout category not available.")
        return None

    workout_list = PREDEFINED_WORKOUTS[category].get(skill_level)
    if not workout_list:
        print("Skill level not found for this category.")
        return None

    workout_name = f"{skill_level} {category} Workout"
    total_duration = round(len(workout_list) * 0.2, 2)
    calories = round(len(workout_list) * 40, 2)
    workout = Workout(workout_name, total_duration, calories,
                      {ex.get_name(): ex for ex in workout_list}, category)
    return workout
def save_athletes(athletes, filename="athletes.json"):
    with open(filename, "w") as f:
        json.dump([a.get_all() for a in athletes], f, indent=4)

def load_athletes(filename="athletes.json"):
    try:
        with open(filename, "r") as f:
            return [Athlete(tuple(a)) for a in json.load(f)]
    except FileNotFoundError:
        return []
def main():
    athletes = load_athletes()   # ⬅️ replaces `athletes = []`
    workouts = []

    while True:
        print("\n--- Personalized Sports Training App Menu ---")
        print("1. Create an Athlete Profile")
        print("2. Add Predefined Workout")
        print("3. View Workout Summary")
        print("4.View All Athletes")
        print("5. Save and Exit")

        choice = input("Select an option: ")

        if choice == "1":
            athlete = create_athlete()
            athletes.append(athlete)
            print(f"Athlete {athlete.get_name()} created successfully!")


        elif choice == "2":
            if not athletes:
                print("Please create an athlete profile first.")
                continue
            print("Choose an athlete to assign a workout:")
            for idx, a in enumerate(athletes):
                print(f"{idx + 1}. {a.get_name()}")
            try:
                selection = int(input("Enter athlete number: ")) - 1
                athlete = athletes[selection]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue
            category = input("Choose workout category (Legs/Arms/Core): ").capitalize()
            workout = generate_workout(athlete.get_skill_level(), category)
            if workout:
                workouts.append(workout)
                athlete.add_workout(workout.name)
                print(f"'{workout.name}' added for {athlete.get_name()}.")


        elif choice == "3":
            if not athletes:
                print("No athletes created yet.")
                continue
            print("Choose an athlete to view their workout summary:")
            for idx, a in enumerate(athletes):
                print(f"{idx + 1}. {a.get_name()}")
            try:
                selection = int(input("Enter athlete number: ")) - 1
                athlete = athletes[selection]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue
            if not athlete.get_workouts():
                print(f"{athlete.get_name()} has no workouts yet.")
            else:
                print(f"\nWorkout Summary for {athlete.get_name()}:")
                for workout_name in athlete.get_workouts():
                    for workout in workouts:
                        if workout.name == workout_name:
                            print(workout)

        elif choice == "4":
            if not athletes:
                print("No athletes created yet.")
                continue
            for athlete in athletes:
                print(athlete.get_all())



        elif choice == "5":
            print("Saving progress and exiting...")
            save_athletes(athletes)  # ⬅️ ADD THIS LINE
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
        main()









