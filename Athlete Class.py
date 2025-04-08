class Athlete:
    def __init__(self, name, sport, age, skill_level, workouts, performance_log, goals):
        self.name = name
        self.sport = sport
        self.age = age
        self.skill_level = skill_level
        self.workouts = workouts
        self.performance = performance_log
        self.goals = goals
        
        
    def display_name(self):
        return self.name
    
    def display_sport(self):
        return self.sport
    
    def display_age(self):
        return self.age
    
    def display_skill_level(self):
        return self.skill_level
    
    def display_workouts(self):
        return self.workouts
    
    def display_performance(self):
        return self.performance
    
    def display_goals(self):
        return self.goals
    
    def display_all(self):
        return self.name, self.sport, self.age, self.skill_level, self.workouts, self.performance, self.goals
    
    
    
