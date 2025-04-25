#from http.client import IncompleteRead
#

class Athlete:
    def __init__(self, input_tuple):
        """
        Creates an Athlete object. A tuple of default values is also provided in case an athlete is missing an attribute.
        :param input_tuple: A tuple with attributes of an athlete
            - input_tuple[0] (str) name: The name of the athlete
            - input_tuple[1] (int) age: The age of the athlete
            - input_tuple[2] (str) skill_level: Skill level of the athlete (Must be Beginner, Intermediate, or Advanced)
            - input_tuple[3] (list[str]) workouts: The list of workouts the athlete uses
            - input_tuple[4] (list[str]) performance: The list of performances associated with each workout of the athlete
            - input_tuple[5] (list[str]) goals: The goals the athlete has
        """

        default_values = ("No Name", 0, "Beginner", [], [], "No Goals")

        self.name = input_tuple[0] if len(input_tuple) >= 1 else default_values[0]
        self.age = input_tuple[1] if len(input_tuple) >= 2 else default_values[1]
        self.skill_level = input_tuple[2] if len(input_tuple) >= 3 else default_values[2]

        self.workouts = (
            input_tuple[3].split(" ") if len(input_tuple) >= 4 and isinstance(input_tuple[3], str)
            else input_tuple[3] if len(input_tuple) >= 4 else default_values[3]
        )
        self.performance = (
            input_tuple[4].split(" ") if len(input_tuple) >= 5 and isinstance(input_tuple[4], str)
            else input_tuple[4] if len(input_tuple) >= 5 else default_values[4]
        )

        self.goals = input_tuple[5] if len(input_tuple) >= 6 else default_values[5]

    def get_name(self):
        """
        Returns the name of the athlete
        :return: (str) The name of the athlete
        """
        return self.name

    def get_age(self):
        """
        Returns the age of the athlete
        :return: (int) The age of the athlete
        """
        return self.age

    def get_skill_level(self):
        """
        Returns the skill level of the athlete
        :return: (str) The skill level of the athlete
        """
        return self.skill_level

    def get_workouts(self):
        """
        Returns the list of workouts the athlete uses
        :return: (list[str]) The list of workouts the athlete uses
        """
        return self.workouts

    def get_performance(self):
        """
        Returns the list of performances associated with each workout of the athlete
        :return: (list[str]) The list of performances.
        """
        return self.performance

    def get_goals(self):
        """
        Returns the goals of the athlete
        :return: (str) The goals of the athlete
        """
        return self.goals

    def display_workouts(self):
        """
        Prints the workouts of the athlete
        """
        print(", ".join(self.workouts))

    def get_all(self):
        """
        Returns a tuple with all the attributes of the athlete. Used to help store athlete data in the json for later use.
        :return: (tuple) A tuple with all the attributes of the athlete
        """
        return self.name, self.age, self.skill_level, self.workouts, self.performance, self.goals

    def add_workout(self, new_workout: str):
        """
        Adds a new workout to the athlete
        :param new_workout: (str) The workout to add to the athlete's profile
        """
        self.workouts.append(new_workout)

    def log_performance(self, new_performance: str):
        """
        Logs the performance of the athlete
        :param new_performance: (str) The new performance of the athlete associated with the new workout
        """
        self.performance.append(new_performance)

    def workout_performance_dict(self):
        """
        Prints a dictionary with each workout and its associated performance
        """
        pairs = zip(self.performance, self.workouts)
        for perf, work in pairs:
            print(f"Performance: {perf.upper()}, Workout: {work.upper()}")


def readData(file_path) -> tuple:
    """
    Opens the json file storing the athletes and reads it into the program
    :param file_path: The path to the json file storing the athletes
    :return: A tuple with athlete data
    """
    with open(file_path) as file:
        info = file.read()
    value = info.split(",")
    if (len(value) == 6):
        name = value[0].strip()

        age = int(value[1])
        skill_level = value[2].strip()
        workouts = value[3].strip()
        performance_log = value[4].strip()
        goals = value[5].strip().lower() in ["upper body", "upperbody"]
        return name, age, skill_level, workouts, performance_log, goals
    else:
        print("Input is missing arguments, please fix file and try again")
        raise ValueError("Incomplete Data")

#Big_Connor = Athlete(readData("C:\\Users\\Miles\\PycharmProjects\\Final MAD2502 project\\Test Athlete.txt"))

#
