
import tkinter as tk
from tkinter import OptionMenu, StringVar

#Video used to learn how to use Tkinter https://youtu.be/ibf5cx221hk?si=6HI2Jnv6uQNmOW4T and https://youtu.be/3E_fK5hCUnI?feature=shared

from Athlete_Class import Athlete
from Excercise_Class import Exercise
from Workout_Class import Workout

athlete = None
workouts = []


PREDEFINED_WORKOUTS = {
    "Legs": {
        "Beginner": [
            Exercise("Bodyweight Squats", 3, [12, 12, 12], [0, 0, 0]),
            Exercise("Glute Bridges", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Step-ups", 2, [10, 10], [0, 0]),
            Exercise("Wall Sit", 3, [30, 30, 30], [0, 0, 0]),
            Exercise("Calf Raises", 2, [15, 15], [0, 0])
        ],
        "Intermediate": [
            Exercise("Goblet Squats", 3, [10, 10, 8], [30, 35, 40]),
            Exercise("Lunges", 3, [10, 10, 10], [15, 15, 15]),
            Exercise("Romanian Deadlifts", 3, [8, 8, 8], [40, 40, 40]),
            Exercise("Bulgarian Split Squat", 3, [8, 8, 8], [20, 20, 20]),
            Exercise("Calf Raises (Weighted)", 3, [15, 15, 15], [20, 20, 20])
        ],
        "Advanced": [
            Exercise("Barbell Squats", 4, [6, 6, 5, 5], [135, 145, 155, 165]),
            Exercise("Deadlifts", 3, [5, 5, 5], [185, 195, 205]),
            Exercise("Walking Lunges", 3, [12, 12, 12], [25, 25, 25]),
            Exercise("Jump Squats", 3, [15, 15, 15], [0, 0, 0]),
            Exercise("Sled Push", 3, [30, 30, 30], [90, 90, 90])
        ]
    },
    "Arms": {
        "Beginner": [
            Exercise("Bicep Curls", 2, [12, 12], [10, 10]),
            Exercise("Tricep Dips (Bench)", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Resistance Band Curls", 2, [15, 15], [0, 0]),
            Exercise("Wall Push-ups", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Overhead Extensions", 2, [12, 12], [10, 10])
        ],
        "Intermediate": [
            Exercise("Dumbbell Bicep Curls", 3, [10, 10, 8], [15, 15, 15]),
            Exercise("Skull Crushers", 3, [10, 8, 8], [20, 25, 25]),
            Exercise("Hammer Curls", 3, [10, 10, 10], [20, 20, 20]),
            Exercise("Overhead Triceps", 3, [10, 10, 10], [25, 25, 25]),
            Exercise("Incline Dumbbell Curls", 3, [8, 8, 8], [15, 15, 15])
        ],
        "Advanced": [
            Exercise("Barbell Curls", 4, [8, 8, 6, 6], [55, 65, 70, 75]),
            Exercise("Weighted Dips", 3, [10, 8, 8], [25, 25, 25]),
            Exercise("Preacher Curls", 3, [8, 8, 8], [50, 50, 50]),
            Exercise("Close Grip Bench Press", 3, [6, 6, 6], [115, 125, 135]),
            Exercise("Cable Triceps Extensions", 3, [10, 10, 10], [40, 45, 50])
        ]
    },
    "Core": {
        "Beginner": [
            Exercise("Crunches", 3, [15, 15, 15], [0, 0, 0]),
            Exercise("Leg Raises", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Plank", 3, [30, 30, 30], [0, 0, 0]),  # seconds
            Exercise("Seated Twists", 3, [20, 20, 20], [0, 0, 0]),
            Exercise("Bird-Dogs", 3, [12, 12, 12], [0, 0, 0])
        ],
        "Intermediate": [
            Exercise("Russian Twists", 3, [20, 20, 20], [10, 10, 10]),
            Exercise("Plank with Shoulder Taps", 3, [20, 20, 20], [0, 0, 0]),
            Exercise("Hanging Leg Raises", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Cable Crunches", 3, [12, 12, 12], [40, 40, 40]),
            Exercise("Side Plank with Reach", 3, [15, 15, 15], [0, 0, 0])
        ],
        "Advanced": [
            Exercise("Weighted Sit-ups", 4, [10, 10, 10, 10], [25, 25, 25, 25]),
            Exercise("Toes to Bar", 3, [10, 10, 10], [0, 0, 0]),
            Exercise("Decline Russian Twists", 3, [20, 20, 20], [20, 20, 20]),
            Exercise("Ab Rollouts", 3, [12, 12, 12], [0, 0, 0]),
            Exercise("Dragon Flags", 3, [8, 8, 8], [0, 0, 0])
        ]
    }
}

screen = tk.Tk()
main_window = tk.Toplevel()
create_profile = tk.Toplevel()
difficulty_rating = tk.Toplevel()
view_athlete = tk.Toplevel()
add_workout = tk.Toplevel()
difficulty_rating.withdraw()
main_window.withdraw()
create_profile.withdraw()
view_athlete.withdraw()
add_workout.withdraw()



def add_preset_workout()->None:
    if athlete != None:
        add_workout.geometry("800x500")
        add_workout.configure(bg="#CD7F32")
        workouts_variable = StringVar()
        screen.withdraw()
        main_window.withdraw()
        difficulty_rating.withdraw()
        view_athlete.withdraw()
        create_profile.withdraw()
        welcome_message = tk.Label(add_workout, text="Choose a category (Legs/Arms/Core): ", font=('Arial', 15), bg="#CD7F32")
        welcome_message.grid()

        workouts_variable.set("Select your muscle here!")
        entered_muscles = tk.OptionMenu(add_workout, workouts_variable,"Legs", "Arms", "Core")
        entered_muscles.grid()


        def fetch_workout():
            category = workouts_variable.get()
            skill = athlete.get_skill_level()
            skill_map = {1: "Beginner", 2: "Intermediate", 3: "Advanced"}
            skill_level = skill if isinstance(skill, str) else skill_map.get(skill, "Beginner")
            exercises = PREDEFINED_WORKOUTS[category.strip()][skill_level]

            workout = Workout(f"{category}Day", 1.0, 300, {ex.name: ex for ex in exercises}, category)
            workouts.append(workout)
            printed_workouts = tk.Label(add_workout, text=f"{workout}", font=('Arial', 18))
            printed_workouts.grid()
            athlete.add_workout(workout.name)
            go_home = tk.Button(add_workout, text="Return to main screen", height=1, width=30, font=('Arial', 18), command=open_main)
            go_home.grid()
            #open_main()

        enter_button = tk.Button(add_workout, text="See suggested workout", width=30, height=1, font=('Arial', 18), command=fetch_workout)
        enter_button.grid()

        add_workout.deiconify()
    else:
        open_main()




def display_athlete()->None:
    if athlete != None:
        view_athlete.geometry("800x500")
        view_athlete.configure(bg="Green")
        main_window.withdraw()
        screen.withdraw()
        create_profile.withdraw()
        difficulty_rating.withdraw()
        add_workout.withdraw()
        welcome_message = tk.Label(view_athlete, text="Your Athelte information is displayed here!", font=('Arial', 15), bg='Green')
        welcome_message.grid()

        athelte_name = tk.Label(view_athlete, text="Name: ", font=('Arial', 15), bg='Green')
        athelte_name.grid(row=1, column=0, pady=20)

        name = athlete.get_name()
        athelte_name = tk.Label(view_athlete, text=f"{name}", font=('Arial', 18), bg='Green')
        athelte_name.grid(row=1, column=1, pady=20)

        #sport = athlete.get_sport()
        #sport_printer = tk.Label(view_athlete, text="Sport: ", font=('Arial', 18), bg='Green')
        #sport_printer.grid(row=4, column=0,pady=20)
        #sport_name = tk.Label(view_athlete, text=f"{sport}", font=('Arial', 18), bg='Green')

        age = athlete.get_age()
        sport_printer = tk.Label(view_athlete, text="Age: ", font=('Arial', 18), bg='Green')
        sport_printer.grid(row=7, column=0, pady=20)
        athlete_age = tk.Label(view_athlete, text=f"{age}", font=('Arial', 18), bg='Green')
        athlete_age.grid(row=7, column=1, pady=20)

        skill_level = athlete.get_skill_level()
        skill_level_printer = tk.Label(view_athlete, text="Skill level: ", font=('Arial', 18), bg='Green')
        skill_level_printer.grid(row=9, column=0, pady=20)
        display_level = tk.Label(view_athlete, text=f"{skill_level}", font=('Arial', 18), bg='Green')
        display_level.grid(row=9, column=1, pady=20)

        workouts_name = tk.Label(view_athlete, text="Workouts", font=('Arial', 18, 'bold'), bg='Green')
        workouts_name.grid(row=15, column=0, pady=10)

        row_offset = 16
        for i, workout_name in enumerate(athlete.get_workouts()):
            workout_rating = athlete.get_performance()[i] if i < len(athlete.get_performance()) else "Not Rated"
            for w in workouts:
                if w.name == workout_name:
                    workout_text = f"{str(w)}\nRating: {workout_rating.strip()}"  # <-- Add rating nicely under workout
                    workout_display = tk.Label(view_athlete, text=workout_text, font=('Arial', 12), bg='lightgreen',
                                           justify='left', anchor='w')
                workout_display.grid(row=row_offset + i, column=0, columnspan=2, sticky='w', padx=10, pady=5)
                break



        return_home = tk.Button(view_athlete, text="Return to menu", width=30, height=1, command=open_main)
        return_home.grid(padx=125,row=20)


        view_athlete.deiconify()
    else:
        open_main()


def rate_workout()->None:
    if athlete != None:
        difficulty_rating.geometry("450x225")
        difficulty_rating.configure(bg="Red")
        main_window.withdraw()
        screen.withdraw()
        create_profile.withdraw()
        view_athlete.withdraw()
        add_workout.withdraw()
        welcome_message = tk.Label(difficulty_rating, text="Rate your last workout (Easy, Moderate, Hard): ", font=('Arial', 15), bg='Red')
        welcome_message.grid(row=0, column=0, columnspan=200,rowspan=50, pady=20, padx=10)

        input_rating = tk.Text(difficulty_rating, height=1, width=30, font=('Arial', 15))
        input_rating.grid(pady=20, padx=40)

        def add_difficulty():
            input_message = input_rating.get("1.0", tk.END)
            athlete.log_performance(input_message)
            open_main()


        create_button = tk.Button(difficulty_rating, height=1, width=30, text="Add Difficulty", font=('Arial', 15), command=add_difficulty)
        create_button.grid(pady=20, padx=40)

        difficulty_rating.deiconify()
    else:
        open_main()


def open_Creator()->None:
    create_profile.geometry("375x550")
    create_profile.configure(bg="Aqua")
    sports = StringVar()
    difficulty = StringVar()
    personal_goals = StringVar()
    main_window.withdraw()
    screen.withdraw()
    difficulty_rating.withdraw()
    view_athlete.withdraw()
    add_workout.withdraw()
    welcome_message = tk.Label(create_profile, text="Please input the following information", font=('Arial', 15), bg="Aqua")
    welcome_message.grid(row=0, column=0, columnspan=200,rowspan=50, pady=20)



    name_message = tk.Label(create_profile, text="Name: ", font=('Arial', 18), bg="Aqua")
    name_message.grid(pady=10)

    name_input = tk.Text(create_profile, height=1, width=30, font=('Arial', 15))
    name_input.grid()

    #sport_message = tk.Label(create_profile, text="Enter your sport: ", font=('Arial, 18'), bg="Aqua")
    #sport_message.grid(pady=10)

   # sports.set("Click here to select sport!")
    #sport_input = OptionMenu(create_profile, sports, "Baseball","Basketball", "Football", "Soccer", "Hockey", "Golf", "Rugby", "Frisbee", "Corn Hole")
   # sport_input.grid()

    age_message = tk.Label(create_profile, text="Age: ", font=('Arial', 18), bg="Aqua")
    age_message.grid(pady=10)

    age_input = tk.Text(create_profile, height=1, width=30, font=('Arial', 15))
    age_input.grid()

    skill_message = tk.Label(create_profile, text="Enter skill level (Beginner/Intermediate/Advanced): ", font=('Arial', 12), bg="Aqua")
    skill_message.grid(pady=10)

    difficulty.set("Select your skill level!")
    skill_input = OptionMenu(create_profile, difficulty, "Beginner", "Intermediate", "Advanced")
    skill_input.grid()

    goals_message = tk.Label(create_profile, text="Goals (e.g., Upper Body): ", font=('Arial', 15), bg="Aqua")
    goals_message.grid(pady=10)

    personal_goals.set("Select a Workout Goal!")
    goals_message = OptionMenu(create_profile, personal_goals, "Upper Body", "Lower Body", "Core")
    goals_message.grid()

    def create_athelte()->None:
        global athlete
        name_message = name_input.get("1.0", tk.END)
        sport_message = sports.get()
        age_message = int(age_input.get("1.0", tk.END))
        skill_message = difficulty.get()
        goal_message = personal_goals.get()
        try:
            athlete = Athlete((name_message.strip(), int(age_message), skill_message.strip(), [], [], goal_message.strip()))
            open_main()
            print(athlete.get_all())
        except IndexError:
            print("Not all inputs were put in!")
        except ValueError:
            print("Entered Age is not an integer!")

    create_button = tk.Button(create_profile, height=1, width=30, text="Create Athlete!", font=('Arial', 15), command=create_athelte)
    create_button.grid(pady=10)


    create_profile.deiconify()


def open_main()->None:
    global athlete
    name_message = input_message.get("1.0", tk.END)
    main_window.geometry("625x575")
    main_window.configure(bg='Blue')
    screen.withdraw()
    create_profile.withdraw()
    difficulty_rating.withdraw()
    view_athlete.withdraw()
    add_workout.withdraw()
    welcome_message = tk.Label(main_window, text=f"{name_message} Please select an action!", font=('Arial', 25), bg='Blue', fg='White')
    welcome_message.grid(pady=20, padx=125)
    if athlete == None:
        useable_message = "You must create an Athlete before you do anything else!"
    else:
        useable_message = "You may now select other actions on your athlete!"

    user_message = tk.Label(main_window, text=f"", font=('Arial', 18), bg='Blue', fg='White')
    user_message.config(text=useable_message)
    user_message.grid()

    option_1 = tk.Button(main_window, height=1, width=30, text="Create an Athlete Profile", font=('Arial', 15), command=open_Creator)
    option_1.grid(pady=20, padx=125)

    option_2 = tk.Button(main_window, height=1, width=30, text="Add Predefined Workout", font=('Arial', 15), command=add_preset_workout)
    option_2.grid(pady=20, padx=125)

    option_3 = tk.Button(main_window, height=1, width=30, text="View Athlete Summary", font=('Arial', 15), command=display_athlete)
    option_3.grid(pady=20, padx=125)

    option_4 = tk.Button(main_window, height=1, width=30, text="Rate a Workout", font=('Arial', 15), command=rate_workout)
    option_4.grid(pady=20, padx=125)

    option_5 = tk.Button(main_window, height=1, width=30, text="Exit program", font=('Arial', 15), command=main_window.destroy)
    option_5.grid(pady=20, padx=125)

    main_window.deiconify()

def get_input()->bool:
    name_message = input_message.get("1.0", tk.END)
    print(name_message)
    open_main()
    welcome_screen = False
    return welcome_screen


#if(welcome_screen == True):

screen.geometry("800x500")
welcome_message = tk.Label(screen, text="Welcome to the Personalized Sports Training App", font = ('Arial', 25), bg='#CBC3E3')
welcome_message.pack(padx = 20, pady = 20)
screen.configure(bg = '#CBC3E3')

name_message = tk.Label(screen, text="Input your name below", font = ('Arial', 18), bg='#CBC3E3')
name_message.pack(padx = 0, pady=75)

input_message = tk.Text(screen, height= 1, width= 30, font = ('Arial', 15))
input_message.pack()

enter_button = tk.Button(screen, height=1, width=30, text="Enter App", font = ('Arial', 15), command=get_input)
enter_button.pack(padx = 0, pady = 65)

screen.mainloop()



#Maybe turn the excersise class into a data class all methods will still work only thing we will have to change is the constructor
#
