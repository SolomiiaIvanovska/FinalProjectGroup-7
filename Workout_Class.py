class Workout:
    def __init__(self, name: str, duration: float, calories_burned: float, exercises: dict, workout_type:str):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned
        self.exercises = exercises  # dict of {exercise_name: Exercise}
        self.workout_type = workout_type  # Type of workout (Strength, Cardio, etc.)
        self.rating = "Not Rated"  # Default workout rating

    def __str__(self):
        result = f"{self.name}\nTime: {self.duration} hrs\nCalories burned: {self.calories_burned}\nType: {self.workout_type}\n"
        for ex in self.exercises.values():
            result += str(ex) + "\n"
        return result

    def add_exercise(self, name: str,exercise_obj ):
        """
         Adds a new exercise to the workout or updates the number of sets if it already exists.
        """
        self.exercises[name] = exercise_obj
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
        return sum(ex.sets for ex in self.exercises.values())

    def update_sets(self, name: str, new_sets: int):
        """
        Updates the number of sets for a specific exercise.
        """
        if name in self.exercises:
            self.exercises[name].sets  = new_sets

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
            "Total Sets": self.total_sets(),
            "Rating": self.rating
        }

    def rate_workout(self, rating: str):
        """
        Allows the user to rate the workout based on how they felt (e.g., 'Easy', 'Moderate', 'Hard').
        """
        self.rating = rating

    def get_exercise_names(self):
        return list(self.exercises.keys())

    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "calories_burned": self.calories_burned,
            "workout_type": self.workout_type,
            "rating": self.rating,
            "exercises": {name: {
                "sets": ex.sets,
                "reps": ex.reps,
                "weight": ex.weight
            } for name, ex in self.exercises.items()}
        }









