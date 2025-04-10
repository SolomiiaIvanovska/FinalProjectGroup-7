class Athlete:
    def __init__(self, input_tuple):
        self.name = input_tuple[0]
        self.sport = input_tuple[1]
        self.age = input_tuple[2]
        self.skill_level = input_tuple[3]
        self.workouts = input_tuple[4].split(" ")
        self.performance = input_tuple[5].split(" ")
        self.goals = input_tuple[6]

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

def readData(file_path)->tuple:
    file = open(file_path)
    info = file.read()
    value = info.split(",")
    name = value[0]
    sport = value[1]
    age = value[2]
    skill_level = value[3]
    workouts = value[4]
    performance_log = value[5]
    goals = value[6]
    return name, sport, age, skill_level, workouts, performance_log, goals

Big_Connor = Athlete(readData("C:\\Users\\Miles\\PycharmProjects\\Final MAD2502 project\\Test Athlete.txt"))
print(Big_Connor.workout_performance_dict())


