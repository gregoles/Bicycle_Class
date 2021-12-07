Bicycle Class:

Description of Class: This class is meant to model various parts of a bike. There are several changeable attributes about this bike that the user can edit, such as the speed and color of the bike. The class itself takes in 4 separate	 arguments. These arguments are the color, the speed, whether the bike has training wheels or not, and whether the bike has gears or not. These are all mandatory for the class to work. There are also two class variables which are the number of pedals and whether the bike has a motor.

Class Variables:

pedal_num: This class variable is meant to represent the number of pedals on a bike. It is always set to two, as pretty much all bikes have two pedals.

has_motor: This class variable represents whether or not the bike has a motor. This class is meant to represent bicycles, so this is always set too False.

Data Variables:

self.__color: This data variable is used to set the color of the bike. It should always be a string.

self.__speed: This data variable is used to set the speed of the bike. It should always be an integer that is equal to or greater than zero.

self._training_wheels: This data variable is a boolean value. It is used to represent whether the bike has training wheels or not.

self._gears: This data variable is also meant to be a boolean value. It is used to represent whether the bike has gears or not to see which slopes it can climb.


Methods:

.set_speed(speed_mph): This method takes in the inputted speed of the bike. It then checks to see if the speed is greater than 0. If the speed is not greater than 0, it prints a message stating that speed can not be a negative number. If the speed is zero or greater, it assigns then speed to a variable.

.get_speed(): This returns self.__speed. It can be used to return only the speed of the bike and nothing else.

.set_color(color): This method takes in the inputted color of the bike. It then checks to see if the color entered is a string. If not, it prints a message saying that color must be a string. If it is a string, assigns then color to a variable

.get_color(): This returns self.__color. It can be used to return only the color of the bike and nothing else.

.training_wheels_check(): This method takes in no arguments. It checks to see if training_wheels has been set to True or False. If training wheels are True, it sets the number of wheels on the bike equal to 4. If it's False, sets the number of wheels equal to 2.

.gear_check(slope): This method takes in one user argument. This is meant to be an integer value, and represents the slope a possible hill. It takes this slope, and checks to see if the bike has gears. If the bike does have gears, it says the bike can go up the slope, but if the bike doesn't have gears, it says the bike can only go up slopes less than 45 degrees.

__str__(): Returns the different attributes of the bike in a string.

Demo Program:

Description: In the demo program, multiple things happen. First, 4 bikes are created using the class, all with various attributes created by the user. It displays the entire first bike, and then displays the color, and the speed of the bike. After that, it checks to see if said bike has training wheels and returns the number of wheels according to that. After that, the gear_check method is used. A slope value of 46 is entered, and because the bike has gears, to displays a message that the bike can climb the slope. Finally, the other three bikes are used with the gear_check function. They are put into a for loop, where each bike is checked too see if it can go up a slope of 50 degrees.

How to Run the Demo Program: To run the demo program, simply run the code in either the terminal or VScode itself.