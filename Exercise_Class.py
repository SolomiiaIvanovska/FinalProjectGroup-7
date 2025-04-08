class Exercise:
    def __init__(self, name: str, sets: int, reps: list , weight: list):
        """
        Creates an exercise, specifying number of sets, amount of reps for each set, and the weight used on each set
        :param name (string): What you call the exercise
        :param sets (int): How many sets were done
        :param reps (list): The amount of reps for each set. Should have length equal to the number of sets.
        :param weight (list): The amount of weight lifted on each set. Should have length equal to the number of sets.
        """
        self.name = name
        self.sets = sets
        self.reps = reps if reps is not None and len(reps)  == sets else [0] * sets
        self.weight = weight if weight is not None and len(weight) == sets else [0] * sets

        if reps and len(reps) != sets:
            raise ValueError(f"Length of reps list not equal to number of sets provided. Expected {sets} but got {len(reps)}")
        if weight and len(weight) != sets:
            raise ValueError(f"Length of weight list not equal to number of sets provided. Expected {sets} but got {len(weight)}")


    def __str__(self):
        return self.name + "\n" + str(self.sets) + " Sets\nReps each set: " + str(self.reps) + "\nWeight each set: " + str(self.weight) + "\n"


benchpress = Exercise("Benchpress", 3, [8, 6, 4], [145, 165, 185])
Chest_fly = Exercise("Chest Fly", 2, [10, 10], [180, 180])

print(benchpress)
print(Chest_fly)