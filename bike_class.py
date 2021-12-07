"""
Name: Gregory Olesinski
Assignment 10.1: Your Own Class
bike_class.py

This program:
Contains a class meant to modela bicycle
A demo program to run said class
"""

class Bicycle:
    # Class variables that all bicycles have
    pedal_num = 2
    has_motor = False

    def __init__(self, color, speed_mph=0, training_wheels=False, gears=None):
        # Sets the color, speed, whether the bike has training wheels, and the gears on the constructor arguments
        self.__color = color
        self.__speed = speed_mph
        self._training_wheels = training_wheels
        self._gears = gears

    def set_speed(self, speed_mph):
        # Checks to see if the speed if below zero
        if speed_mph < 0:
            print("Speed can not be a negative number")
        # If it isn't, sets the speed
        else:
            speed = speed_mph
            self.__speed = speed
    
    # Returns the set speed
    def get_speed(self):
        return (self.__speed)

    def set_color(self, color):
        # Checks to see that color was inputted properly and then sets color
        if type(color) != type(""):
            print("Must enter a valid color as a string")
        else:
            self.__color = color

    # Returns the set color
    def get_color(self):
        return self.__color

    # Checks to see if training wheels are set to Tue or False
    def training_wheels_check(self):
        training_wheels = self._training_wheels
        # If the bike does have training wheels, says that there are four wheels, otherwise there are two
        if training_wheels == True:
            num_wheels = 4
            return num_wheels
        elif training_wheels == False:
            num_wheels = 2
            return num_wheels
        else:
            print("Enter True or False for Training Wheels")           

    def gear_check(self, slope):
        # Checks to see if the bike has gears or not.
        # Checks inputted slope as well, and sees if the bike can go up said slope with or without gears
        gears = self._gears
        if gears == True:
            slope_success = ("You can bike up the slope!")
        elif gears == False and slope >= 45:
            slope_success = ("You can't bike up the slope slope!")
        elif gears == False and slope < 45:
            slope_success = ("You can bike up the slope!")
        self._gears = slope_success
        return slope_success

    # String magic method         
    def __str__(self):
        return (f"Your Bike: Color = {self.__color}, Speed = {self.__speed}, Training Wheels = {self._training_wheels}, Gears = {self._gears}")

# Main
def main():
    # Creates 4 bikes with varying attributes
    green_bike = Bicycle("green", 8, True, True)
    bike1 = Bicycle("yellow", 0, True, True)
    bike2 = Bicycle("yellow", 0, False, False)
    bike3 = Bicycle("yellow", 0, False, True)

    # Returns a string of all the attributes of the created bike
    print(green_bike)

    # Accesses the get.color method and returns just the color of the bike and nothing else
    print(green_bike.get_color())

    # Accesses the get.speed method and returns just the speed of the bike and nothing else
    print(green_bike.get_speed())

    # Accesses the training_wheels_check method and returns just how many wheels the bike has based off whether training wheels is set to True or False
    print(green_bike.training_wheels_check())

    # Takes in a slope angle value, then checks to see if the bike has gears and returns whether said bike can go up the given slope
    print(green_bike.gear_check(46))
    x = 1
    for i in [bike1, bike2, bike3]:
        print(f"Bike {x}:{i.gear_check(50)}")
        x += 1

if __name__ == "__main__":
    main()
