class Athlete:
    def __init__(self, name = "", sport = "", age = 0, skill_level = "", workouts = [], performance_log = [], goals = ""):
        self.name = name
        self.sport = sport
        self.age = age
        self.skill_level = skill_level
        self.workouts = workouts
        self.performance = performance_log
        self.goals = goals

    def get_name(self):
        return self.name

    def get_sport(self):
        return self.sport

    def get_age(self):
        return self.age

    def get_skill_level(self):
        return self.skill_level

    def get_workouts(self):
        return self.workouts

    def display_workouts(self):
        for i in range(len(self.workouts)):
            print(self.workouts[i], end = ", ")

    def get_performance(self):
        return self.performance

    def get_goals(self):
        return self.goals

    def get_all(self):
        return self.name, self.sport, self.age, self.skill_level, self.workouts, self.performance, self.goals

    def add_workout(self, new_workout: str):
        self.workouts.append(new_workout)

    def log_performance(self, new_performance: str):
        self.performance.append(new_performance)

    def workout_performance_dict(self):
        workout_performance_dict = zip(self.performance, self.workouts)
        for key, val in workout_performance_dict:
            print(f"Performance feeling: {key.upper()}, Workout Done: {val.upper()}")



tester = Athlete("COnnor", "is", workouts=["hello", "I", "am", "testing"], performance_log=["good", "bad", "sad", "mad"])
#tester2 = Athlete(performance_log=["good", "bad", "sad", "mad"])
print(tester.workout_performance_dict())
print(tester.get_all())

