#!/usr/bin/env python3
#Jonah Lucas for Python Programming, CVTC
#Stores class objects for use in other files


from dataclasses import dataclass

@dataclass
class Workout:
    workoutDate:str = ""
    name:str = ""
    target:str = ""
    duration:int = 0
    caloriesBurned:int = 0
    workoutID:int = 0

class allWorkouts:
    def __init__(self):
        self.__list = []

    @property
    def count(self):
        return len(self.__list)

    def add(self, workout):
        return self.__list.append(workout)

    def remove(self, number):
        return self.__list.pop(number-1)

    def __iter__(self):
        for workout in self.__list:
            yield workout

def main():
    allwork = allWorkouts()

    for workout in allwork:
        print(workout.workoutDate, workout.name, workout.target, workout.duration, workout.caloriesBurned)

if __name__ == "__main__":
    main()
