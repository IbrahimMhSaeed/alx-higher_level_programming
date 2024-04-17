# Classes

## Static Methods

if you create a private class attribute `__counter` and you want to display vaule fo user.
*You can't use regular methods*
```
class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    def RobotInstances(self):
        return Robot.__counter
        

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
```
```
Robot.RobotInstances()
```
we will encounter this error:
```
TypeError: RobotInstances() missing 1 required positional argument: 'self'
```

The solution is to use the decorator `@staticmethod`

```


class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @staticmethod
    def RobotInstances():
        return Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
```

Output:
```
0
1
2
2
```
This way we cann access it from Both object and class

## Class Methods

Like static methods class methods are not bound to instances, but unlike static methods class methods are bound to a class. The first parameter of a class method is a reference to a class, i.e. a class object. They can be called via an instance or the class name.

**Uses the decorator `@classmethod`**
```
class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
```
Output:
```
(<class '__main__.Robot'>, 0)
(<class '__main__.Robot'>, 1)
(<class '__main__.Robot'>, 2)
(<class '__main__.Robot'>, 2)
```
### How to use classmethods as alternative constructors
we have a class
```
class Employee:
```
The user always pass the user info in string separated by hyphen (-) `John-Doe-7000'
```
# we create class method
emp_str_1 = 'John-Doe-7000'

@classmethod
def from_string(cls, emp_str):
	first, last, pay = emp_str.split('-')
	return cls(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)
```
**That is similar to what is done in time class**

where when you call
```
time.localtime()
time.today()
```
Each one of these give you different structure of time object
## Class Methods vs. Static Methods and Instance Methods

**Instance Methods**: Can only be called by an instance
```
a = Robot()
a.Instance_Method()
Robot(a).Instance_Method #will giv the same output
```


**Static Methods**: Can be called by both instance and class But its reference will always return to the BIG FATHER
*it has nothing to do with Class nor the isntance so we make it static*
*Doesn't return anything*
```
a = Robot()
a.Static_Method()
Robot.Static_Method()
```

**Class Methods**: Can only be called by both class and instance, Its reference is to the CHILD

### Example shows the difference
We define a class Pet with a method about. This method should give some general class information. The class Cat will be inherited both in the subclass Dog and Cat. The method about will be inherited as well. We will demonstrate that we will encounter problems.

#### Option 1) Instance Method
```


class Pet:
    _class_info = "pet animals"

    def about(self):
        print("This class is about " + self._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()
```
OUTPUT:
```
This class is about pet animals!
This class is about man's best friends!
This class is about all kinds of cats!

```
It would be a lot better, if we could just write Pet.about(), Dog.about() and Cat.about() to get the previous result. We cannot do this. We will have to write Pet.about(p), Dog.about(d) and Cat.about(c) instead.

#### Option 2) Static Method:
```
class Pet:
    _class_info = "pet animals"

    @staticmethod
    def about():
        print("This class is about " + Pet._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

Pet.about()
Dog.about()
Cat.about()
```
OUTPUT:
```
This class is about pet animals!
This class is about pet animals!
This class is about pet animals!
```

we have no way of differenciating between the class Pet and its subclasses Dog and Cat. The problem is that the method about does not know that it has been called via the Pet the Dog or the Cat class.

#### Option 3) For The WIN Class Method:
```


class Pet:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

Pet.about()
Dog.about()
Cat.about()
```
OUTPUT:
```
This class is about pet animals!
This class is about man's best friends!
This class is about all kinds of cats!
```
## More

### str and repr

|str() 	|repr()|
|-------|------|
|make object readable |need code that reproduces object|
|generate output for end user |generate output for developer|
