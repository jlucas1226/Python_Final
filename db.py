#!/usr/bin/python3
#Jonah Lucas for Python Programming, CVTC
#Stores functions necessary for database interaction

import sqlite3
from contextlib import closing

from business import Workout, allWorkouts

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "workouts_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_workout(row):
    return Workout(row["workoutDate"], row["name"], row["target"], row["duration"], row["caloriesBurned"], row["workoutID"])

def get_workouts():
    query = '''SELECT workoutID, workoutDate, name, target, duration, caloriesBurned
               FROM Workout ORDER BY workoutDate'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    workouts = allWorkouts()
    for row in results:
        workout = make_workout(row)
        workouts.add(workout)
    return workouts

def add_workout(workout):
    sql = '''INSERT INTO Workout
                (workoutDate, name, target, duration, caloriesBurned)
             VALUES
                (?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (workout.workoutDate, workout.name, workout.target, workout.duration, workout.caloriesBurned))
        conn.commit()

def delete_workout(workout):
    sql = '''DELETE FROM Workout WHERE workoutID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (workout.workoutID,))
        conn.commit()

def main():
    connect()
    workouts = get_workouts()
    for workout in workouts:
        print(workout.workoutDate, workout.name, workout.target, workout.duration, workout.caloriesBurned)

if __name__ == "__main__":
    main()
