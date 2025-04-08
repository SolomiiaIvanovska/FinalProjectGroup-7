from typing import List
from Exercise_Class import *

class Workout:
    def __init__(self, name: str, duration: float, calories_burned: float, exercises: List[Exercise]):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned
        self.exercises = exercises

    def __str__(self):
        return self.name + "\nTime: " + str(self.duration) + "\nCalories burned: " + str(self.calories_burned)













#Testing Code
my_workout = Workout("Chest day", 1.59, 450, [benchpress, Chest_fly])
print(my_workout)