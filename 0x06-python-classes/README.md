# Classes and Objects

Classes and objects are the fundamental block of OOP

## Class

check file "robot.py" for more robust example

1) created by the keyword "class"

```
class myClass:

	population = 0  #This is a global Class variable

	def __init__(self, name):
	#Create object variables
		self.name = name

	@classmethod
	def how_many(cls):
		print(f"we have {cls.population} robots")
```
2) example above show how to create class method (use class variables)

3) you can get attribute and avoid error if attr doesn't exist by using:

getattr(x, 'energy', 100)

where 100 is the default value for x if it doesn't exist

## Encapsulation

accomplished by providing two kinds of methods for attributes:
1) Getter
2) Setter
```
class Robot:
    def __init__(self, name=None):
        self.name = name   
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

# This is the important piece of code

    def set_name(self, name):
	self.name = name
    def get_name(self):
	return self.name
```
## `__str__` and `__repr__`

- `__str__` represent the output that will be printed when ur class is placed inside __print()__ function

- `__repr__` represent the output that will be printed when ur class is written iside interpreter without print() function

*The content of __repr__ should be the stirng that can recreate the object when eval() is called*

example:
```
def __repr__(self):
	return "Rectangle({}, {})".format(self.__width, self.__height)

rect_2 = eval(rect_1)

# will create new rect with same values
```
```
class Robot:
    def __init__(self, name, build_year):
	self.name = name
	self.build_year = build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," +  str(self.build_year) +  ")"
    def __str__(self):
	return "Name: " + self.name + ", Build Year: " +  str(self.build_year)

# To use them u need to use

c_103 = Robot("Mebo", "1970")
str(c_103)
repr(c_103)
```

## Public, - Protected-, and Private Attributes
```
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
```
*Note for private attributes we need to set a "getter" and a "setter" for each of them if we need to make user able to adjust there values.*

*Note by doing this you are protecting ur code by monitoring user input for each and every attr*

**!!Important**
There are at least two good reasons against such an approach. First of all not every private attribute needs to be accessed from outside. Second, we will create non-pythonic code this way, as you will learn soon.


## Destructor
```
def __del__(self):
        print ("Robot has been destroyed")
```
runs when the object is destroyed


## Properties vs. Getters and Setters

Unfortunately, it is widespread belief that a proper Python class should encapsulate private attributes by using getters and setters. As soon as one of these programmers introduces a new attribute, he or she will make it a private variable and creates "automatically" a getter and a setter for this attribute.

### Javasequence way (not Pythonic)

First, we demonstrate in the following example, how we can design a class in a Javaesque way with getters and setters to encapsulate the private attribute `self.__x`:
```
class P:

    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

p1.set_x(p1.get_x()+p2.get_x())

```
What do you think about the expression "`p1.set_x(p1.get_x()+p2.get_x())`"? It's ugly, isn't it?


### Pythonic Way

```
class P:

    def __init__(self,x):
        self.x = x

p1.x = p1.x + p2.x

```
*"But there is NO data ENCAPSULATION!"* 


#### assume we want to change the implementation like this: The attribute x can have values between 0 and 1000.
```
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
```
**Note the following:**

1) We defined the variable as public

2) We added the decorator "@property" before the getter function that have the same name as the variable "x"
```
    @property
    def x(self):
	return self.__x
```
3) We refer to the variable x in the getter function with "`self.__x`" as it was a private varible (which it is!)

4) We added "@.setter" before the setter function and inside it we can define any setter conditions we want

## How to create attribute that depends on value of other private ones?
```
class Robot:

	def __init__(self, name, year, lk = 0.5, lp = 0.5):
		self.name = name
		self.year = year
		self.__physical = lk
		self.__psychic = lp

	@property
	def condition(self):
		s = self.__physical + self.__psychic
		if s <= -1:
			return "I feel miserable!"
		elif s <= 0:
			return "I feel bad!"
		elif s <= 0.5:
			return "Could be worse!"
		else:
			return "I feel Great!"
```
Now we can Use the class
```
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)

```

### Why to use @property

The @property decorator in Python is a powerful tool for creating read- only attributes for your classes. It allows you to define a method that acts like a regular attribute but provides more control over how the value is accessed and calculated.

- Validation and error handling:
You can implement validation or error handling within the property method to ensure the returned value is valid and handle potential issues.

- Documentation:
Properties can be documented like regular methods, providing clear explanations of how they work and what values they return.

## When to use Public & when to use Private?


- Will the value of "OurAtt" be needed by the possible users of our class?
	- If not, we should make it a private attribute.
	- If it has to be accessed, we make it accessible as a public attribute

- We will define it as a private attribute with the corresponding property, if and only if we have to do some checks or transformation of the data. (As an example, you can have a look again at our class P, where the attribute has to be in the interval between 0 and 1000, which is ensured by the property "x")

- Alternatively, you could use a getter and a setter, but using a property is the Pythonic way to deal with it!


### Example of changing Public to Private (Pythonic Way!):

Assume we have the following attribute:
```
class OurClass:

    def __init__(self, a):
        self.OurAtt = a
```
and we can use it like this:
```
x = OurClass(10)
print(x.OurAtt)
```
and we needed to change "OurAtt" to private one, we will only have to add few lines as follows:
```
class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val
```
We can also use it like this
```
x = OurClass(10)
print(x.OurAtt)
```
**Note that the usage of "OurAtt" hasn't changed!**

## Generic Getters and Setters (`__getattr__ and __setattr__`)

Assume the following senario:
```
class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    @property
    def name(self):
        return self.__name

    @property
    def build_year(self):
        return self.__build_year

    @property
    def city(self):
        return self.__city

    @name.setter
    def name(self, value):
        self.__name = value

    @build_year.setter
    def build_year(self, value):
        self.__build_year = value

    @city.setter
    def city(self, value):
        self.__city = value
```
Example usage:
```
robot = Robot("RoboBot", 2022, "TechCity")

print(robot.name)
print(robot.build_year)
print(robot.city)
```

We can group them all together using the following:
```
class Robot:
    
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    def __getattr__(self, name):
	return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
	self.__dict__[f"__{name}"] = value
```

Also we can specify specific safety conditions for setters:

```
def __setattr__(self, name, value):
        if name == 'name':
            if value in ['Henry', 'Oscar']:
                raise ValueError('Not a decent Robot name')
        elif name == 'build_year':
            if int(value) < 2020:
                raise ValueError('Build Year has to be after 2019')
        self.__dict__[f"__{name}"] = value
```

## When to use Ordinary setter and getter methods (Non-Pythonic Way)

- Dynamic Computation or Validation:
If getting or setting an attribute involves complex computations or validation that goes beyond simple attribute access

```
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        return 3.14 * self._radius**2

    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value
```
- Additional Arguments to Attributes 
If you need to pass more arguments for setters (much more that just a value)

```
def set_height(self, value, validate=True):
        if validate and not (150 <= value <= 200):
            raise ValueError("Height must be between 150 and 200 cm.")
        self._height = value
```
