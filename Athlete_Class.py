#from http.client import IncompleteRead


class Athlete:
    def __init__(self, input_tuple):
        self.name = input_tuple[0]
        self.sport = input_tuple[1]
        self.age = input_tuple[2]
        self.skill_level = input_tuple[3]
        self.workouts = input_tuple[4].split(" ") if isinstance(input_tuple[4], str) else input_tuple[4]
        self.performance = input_tuple[5].split(" ") if isinstance(input_tuple[5], str) else input_tuple[5]
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

    def get_performance(self):
        return self.performance

    def get_goals(self):
        return self.goals

    def display_workouts(self):
        print(", ".join(self.workouts))

    def get_all(self):
        return self.name, self.sport, self.age, self.skill_level, self.workouts, self.performance, self.goals

    def add_workout(self, new_workout: str):
        self.workouts.append(new_workout)

    def log_performance(self, new_performance: str):
        self.performance.append(new_performance)

    def workout_performance_dict(self):
        pairs = zip(self.performance, self.workouts)
        for perf, work in pairs:
            print(f"Performance: {perf.upper()}, Workout: {work.upper()}")

def readData(file_path)->tuple:
   with open(file_path) as file:
       info = file.read()
   value = info.split(",")
   if(len(value) == 7):
       name = value[0].strip()
       sport = value[1].strip()
       age = int(value[2])
       skill_level = value[3].strip()
       workouts = value[4].strip()
       performance_log = value[5].strip()
       goals = value[6].strip().lower() in ["upper body", "upperbody"]
       return name, sport, age, skill_level, workouts, performance_log, goals
   else:
       print("Input is missing arguments, please fix file and try again")
       raise IncompleteRead


#Big_Connor = Athlete(readData("C:\\Users\\Miles\\PycharmProjects\\Final MAD2502 project\\Test Athlete.txt"))




