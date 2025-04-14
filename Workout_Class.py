from typing import List
from Exercise_Class import Exercise

class Workout:
    def __init__(self, name: str, duration: float, calories_burned: float, exercises: List[Exercise], workout_type:str):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned
        self.exercises = exercises
        self.workout_type = workout_type  # Type of workout (Strength, Cardio, etc.)
        self.rating = "Not Rated"  # Default workout rating

    def __str__(self):
        return self.name + "\nTime: " + str(self.duration) + "\nCalories burned: " + str(self.calories_burned) + "\n"


    def add_exercise(self, exercise: Exercise):
        """
         Adds a new exercise to the workout. If a workout with the same name already exists, adds a number to the end of the exercise name
         to differentiate it from other exercises of the same name.
        """
        is_in_already = 1
        for ex in self.exercises:
            if ex.name == exercise.name:
                is_in_already += 1

        if is_in_already > 1:
            exercise.name = exercise.name + "(" + str(is_in_already) + ")"
            self.exercises.append(exercise)
        else:
            self.exercises.append(exercise)



    def remove_exercise(self, exercise: Exercise):
        """
        Removes an exercise from the workout by its name.
        """
        for ex in self.exercises:
            if ex.name == exercise.name:
                self.exercises.remove(ex)
                return
        print("Exercise " + exercise.name + " does not exist in the workout")


    def remove_exercise_str(self, exercise: str):
        for ex in self.exercises:
            if ex.name == exercise:
                self.exercises.remove(ex)
                return
        print("Exercise " + exercise + " does not exist in the workout")



    def total_sets(self):
        """
         Returns the total number of sets across all exercises in the workout.
        """
        total = 0
        for ex in self.exercises:
            total += ex.sets
        return total


# Commented out for now because functionality doesn't make sense with exercise class implementation
#    def update_sets(self, name: str, new_sets: int):
#        """
#        Updates the number of sets for a specific exercise.
#        """
#        if name in self.exercises:
#            self.exercises[name] = new_sets

    def get_summary(self):
        """
        Returns a summary dictionary with key details about the workout: name, duration, calories burned,
        total exercises, and total sets.
        """
        return {
            "Workout": self.name,
            "Duration (hr)": self.duration,
            "Calories Burned": self.calories_burned,
            "Total Exercises": len(self.exercises),
            "Total Sets": self.total_sets()
        }

    def display_summary(self):
        print("Workout: " + self.name
              + "\nDuration: " + str(self.duration)
              + "\nCalories burned: " + str(self.calories_burned)
              + "\nTotal Exercises: " + str(len(self.exercises))
              + "\nTotal Sets: " + str(self.total_sets())
              + "\nRating: " + self.rating
              + "\n")
    
    def display_exercises(self):
        for ex in self.exercises:
            print(ex)

    def rate_workout(self, rating: str):
        """
        Allows the user to rate the workout based on how they felt (e.g., 'Easy', 'Moderate', 'Hard').
        """
        self.rating = rating











# Testing Code
# Remove and add comments to displays to check different methods

# Create exercises for workout
bench = Exercise("Benchpress", 3, [10, 8, 6], [185, 205, 225])
chest_fly = Exercise("Chest Fly", 3, [10, 10, 10], [140, 150, 150])
my_workout = Workout("Chest day", 1.59, 450, [bench, chest_fly], "Chest") #added workout_type

#my_workout.display_summary()
#my_workout.display_exercises()


# Add an exercise to the workout
pushups = Exercise("Pushups", 5, [30, 27, 21, 21, 18], [0,0,0,0,0])
my_workout.add_exercise(pushups)

#my_workout.display_summary()
#my_workout.display_exercises()


# Adds workout with same name to ensure naming differentiation works
pushups_again = Exercise("Pushups", 2, [50, 50], [0,0])
my_workout.add_exercise(pushups_again)

#my_workout.display_summary()
#my_workout.display_exercises()


# Deletes an exercise from the workout
my_workout.remove_exercise(pushups)

#my_workout.display_summary()
#my_workout.display_exercises()

######################################################
# Need to fix the fact that the "(2)" is still printed even though there is now only 1 instance of pushups workout
#######################################################


# Rate workout
my_workout.rate_workout("Easy")
my_workout.display_summary()
#
