# Classes and Objects

Classes and objects are the fundamental block of OOP

## Class

check file "robot.py" for more robust example

1) created by the keyword "class"

	class myClass:

		population = 0  #This is a global Class variable

		def __init__(self, name):
		#Create object variables
			self.name = name

		@classmethod
		def how_many(cls):
			print(f"we have {cls.population} robots")

2) example above show how to create class method (use class variables)

3) you can get attribute and avoid error if attr doesn't exist by using:

getattr(x, 'energy', 100)

where 100 is the default value for x if it doesn't exist

## Encapsulation

accomplished by providing two kinds of methods for attributes:
1) Getter		2) Setter

class Robot:
    def __init__(self, name=None):
        self.name = name   
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

* This is the important piece of code

    def set_name(self, name):
	self.name = name
    def get_name(self):
	return self.name

## __str__ and __repr__

class Robot:
    def __init__(self, name, build_year):
	self.name = name
	self.build_year = build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," +  str(self.build_year) +  ")"
    def __str__(self):
	return "Name: " + self.name + ", Build Year: " +  str(self.build_year)

* To use them u need to use

c_103 = Robot("Mebo", "1970")
str(c_103)
repr(c_103)


## Public, - Protected-, and Private Attributes

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

Note for private attributes we need to set a "getter" and a "setter" for each of them if we need to make user able to adjust there values.

Note by doing this you are protecting ur code by monitoring user input for each and every attr

!!Important
There are at least two good reasons against such an approach. First of all not every private attribute needs to be accessed from outside. Second, we will create non-pythonic code this way, as you will learn soon.


## Destructor

def __del__(self):
        print ("Robot has been destroyed")

runs when the object is destroyed


## Properties vs. Getters and Setters

Unfortunately, it is widespread belief that a proper Python class should encapsulate private attributes by using getters and setters. As soon as one of these programmers introduces a new attribute, he or she will make it a private variable and creates "automatically" a getter and a setter for this attribute.

### Javasequence way (not Pythonic)

First, we demonstrate in the following example, how we can design a class in a Javaesque way with getters and setters to encapsulate the private attribute self.__x:

class P:

    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

p1.set_x(p1.get_x()+p2.get_x())


* What do you think about the expression "p1.set_x(p1.get_x()+p2.get_x())"? It's ugly, isn't it?


### Pythonic Way

class P:

    def __init__(self,x):
        self.x = x

p1.x = p1.x + p2.x

*"But there is NO data ENCAPSULATION!" 


#### assume we want to change the implementation like this: The attribute x can have values between 0 and 1000.

class P:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

Note the following:

1) We defined the variable as public

2) We added the decorator "@property" before the getter function that have the same name as the variable "x"

    @property
    def x(self):
	return self.__x

3) We refer to the variable x in the getter function with "self.__x" as it was a private varible (which it is!)

4) We added "@.setter" before the setter function_ and inside it we can define any setter conditions we want

## How to create attribute that depends on value of other private ones?


