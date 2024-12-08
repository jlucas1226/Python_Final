#!/usr/bin/python3
#Jonah Lucas for Python Programming, CVTC
#Stores functions necessary for user interaction, program is run from this file

import db
from business import Workout, allWorkouts

def set_goal():
    global goal
    while True:
        try:
            goal = int(input("Enter your goal for daily calories burned: "))
        except ValueError:
            print("Invalid entry. Please enter a valid integer.")
            
        if goal < 0:
            print("Goal must be a positive integer!")
        else:
            print(f"Daily calories burned goal set to {goal} calories.")
            return goal

def compare_goal(workouts, goal):
    goal_met = " "
    if workouts == None:
        print("There are no current workouts recorded.")
    else:
        print(f"\tWorkout Date\tName\tTarget\tDuration Calories Burned  Goal Met")
        print("-" * 100)
        for workout in workouts:
            if goal > workout.caloriesBurned:
                print(f"{workout.workoutID}\t{workout.workoutDate}\t{workout.name}\t{workout.target}\t   {workout.duration}\t\t{workout.caloriesBurned}\t\tY")
            else:
                print(f"{workout.workoutID}\t{workout.workoutDate}\t{workout.name}\t{workout.target}\t   {workout.duration}\t\t{workout.caloriesBurned}\t\tN")
    print()

def add_workout(workouts):
    workoutDate = input("Date (YYYY-MM-DD): ")
    name = input("Name: ")
    target = input("Muscle group target: ")
    duration = get_duration()
    caloriesBurned = get_calories()

    workout = Workout(workoutDate, name, target, duration, caloriesBurned)
    workouts.add(workout)
    db.add_workout(workout)
    print(f"Workout was added.\n")

def get_duration():
    while True:
        try:
            duration = int(input("Workout duration (in minutes): "))
        except ValueError:
            print("Invalid duration integer. Please try again.")
            continue

        if duration < 0:
            print("Invalid duration. Must be a positive integer.")
        else:
            return duration

def get_calories():
    while True:
        try:
            caloriesBurned = int(input("Calories burned during workout: "))
        except ValueError:
            print("Invalid entry. Please enter an integer.")
            continue

        if caloriesBurned < 0:
            print("Invalid calories burned entry. Must be a positive integer.")
        else:
            return caloriesBurned

def get_workout_number(workouts, prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if number < 1:
            print("Invalid number. Try again.")
        else:
            return number

def delete_workout(workouts):
    number = get_workout_number(workouts, "Number: ")
    workout = workouts.remove(number)
    db.delete_workout(workout)
    print("Workout deleted.")

def display_workouts(workouts):
    if workouts == None:
        print("There are no current workouts recorded.")
    else:
        print(f"\tWorkout Date\tName\tTarget\tDuration Calories Burned")
        print("-" * 100)
        for workout in workouts:
            print(f"{workout.workoutID}\t{workout.workoutDate}\t{workout.name}\t{workout.target}\t   {workout.duration}\t  {workout.caloriesBurned}")
    print()

def display_separator():
    print("-" * 100)

def display_title():
    print("                  Jonah's Workout Tracker")

def display_menu():
    print("Menu Options")
    print("1 - Display Recorded Workouts")
    print("2 - Record a Workout")
    print("3 - Remove a Workout")
    print("4 - Set Daily Calorie Goal")
    print("5 - Compare Workouts to Goal")
    print("6 - Display Menu Options")
    print("7 - Exit")

def main():
    display_separator()
    display_title()
    display_menu()

    db.connect()
    workouts = db.get_workouts()
    if workouts == None:
        workouts = AllWorkouts()

    display_separator()

    while True:
        try:
            option = int(input("Menu Option: "))
        except ValueError:
            option = -1

        if option == 1:
            display_workouts(workouts)
        elif option == 2:
            add_workout(workouts)
            workouts = db.get_workouts()
        elif option == 3:
            delete_workout(workouts)
        elif option == 4:
            set_goal()
        elif option == 5:
            compare_goal(workouts, goal)
        elif option == 6:
            display_menu()
        elif option == 7:
            db.close
            print("Thank you, goodbye!")
            break
        else:
            print("Not a valid menu option. Please try again.")
            display_menu()

if __name__ == "__main__":
    main()
