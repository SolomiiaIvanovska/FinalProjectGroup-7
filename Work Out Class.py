class Workout:
    def __init__(self, name: str, duration: float, calories_burned: float, exercises: dict):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned
        self.exercises = exercises

    def __str__(self):
        return self.name + "\nTime: " + str(self.duration) + "\nCalories burned: " + str(self.calories_burned)













#Testing Code
my_workout = Workout("Chest day", 1.59, 450, {"Benchpress": 5, "Chest Fly": 3, "Incline DB Bench": 2, "Pushups": 3})
print(my_workout)