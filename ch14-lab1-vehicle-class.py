# Tim Lucas
# Lab 14-1
# 2025-07-07

from dataclasses import dataclass

class Vehicle:

    def __init__(self, current_speed = 0):
        self.__current_speed = current_speed

    def accelerate(self):
        print("Accelerating...")
        self.__current_speed += 1
    
    def decelerate (self):
        print("Decelerating...")
        self.__current_speed -= 1

    def display_speed(self):
        print(f"The vehicle's current speed is {self.__current_speed}")

def main():
    car1 = Vehicle()

    car1.accelerate()
    car1.display_speed()

    car1.accelerate()
    car1.display_speed()

    print()

    car1.decelerate()
    car1.display_speed()

    car1.decelerate()
    car1.display_speed()

if __name__ == "__main__":
    main()