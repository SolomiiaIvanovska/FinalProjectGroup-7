class Workout:
    def __init__(self, name: str, duration: float, calories_burned: float, exercises: dict, workout_type:str):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned
        self.exercises = exercises
        self.workout_type = workout_type  # Type of workout (Strength, Cardio, etc.)
        self.rating = "Not Rated"  # Default workout rating

    def __str__(self):
        return self.name + "\nTime: " + str(self.duration) + "\nCalories burned: " + str(self.calories_burned)

    def add_exercise(self, name: str, sets: int):
        """
         Adds a new exercise to the workout or updates the number of sets if it already exists.
        """
        if name in self.exercises:
            self.exercises[name] += sets
        else:
            self.exercises[name] = sets

    def remove_exercise(self, name: str):
        """
        Removes an exercise from the workout by its name.
        """
        if name in self.exercises:
            del self.exercises[name]

    def total_sets(self):
        """
         Returns the total number of sets across all exercises in the workout.
        """
        return sum(self.exercises.values())

    def update_sets(self, name: str, new_sets: int):
        """
        Updates the number of sets for a specific exercise.
        """
        if name in self.exercises:
            self.exercises[name] = new_sets

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

    def rate_workout(self, rating: str):
        """
        Allows the user to rate the workout based on how they felt (e.g., 'Easy', 'Moderate', 'Hard').
        """
        self.rating = rating











#Testing Code
my_workout = Workout("Chest day", 1.59, 450, {"Benchpress": 5, "Chest Fly": 3, "Incline DB Bench": 2, "Pushups": 3}, "Strength") #added workout_type
print(my_workout)
my_workout.add_exercise("Pushups", 3)
my_workout.update_sets("Chest Fly", 4)
my_workout.remove_exercise("Benchpress")


print("\nUpdated Workout:")
print(my_workout)


print("\nWorkout Summary:")
print(my_workout.get_summary())

my_workout.rate_workout("Hard")
print("\nRated Workout:")
print(my_workout)