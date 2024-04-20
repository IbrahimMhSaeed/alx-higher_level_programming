# Inheritance

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Derived classes may override methods of their base classes.

##  built-in functions that work with inheritance:
- `isinstance()`:
to check an instance’s type: `isinstance(obj, int)` will be True only if `obj.__class__` is int or some class derived from int.

- `issubclass()`:
to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.


### `isinstance()` vs `issubclass()`

`isinstance()`:
asks whether an object is an instance of a class (or a tuple of classes)

`issubclass()`: asks whether one class is a subclass of another class (or other classes)

```
class Foo:
	pass

class Bar(Foo):
	pass

issubclass(Bar, Foo)
#>True
isinstance(Bar, Foo)
#>False
```

Bar is a subclass of Foo, not an instance of it.
Bar is an instance of type which is a subclass of object

Bar (instance) => type (subclass) => object

Bar (instance) => object

```
isinstance(Bar, type)
#>True
issubclass(type, object)
#>True
isinstance(Bar, object)
#>True
```

## Multiple Inheritance

Python supports a form of multiple inheritance as well.
```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

### How Search is Done

you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

## Example of inheritance

Assume parent class named Person:
```
# A Python program to demonstrate inheritance
class Person:

# Constructor
def __init__(self, name, id):
	self.name = name
	self.id = id

# To check if this person is an employee
def Display(self):
	print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()
```
**OUTPUT**:
```
Satyam 102
```

-----
Creating a Child Class

```
class Emp(Person):

def Print(self):
	print("Emp class called")
	
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()
```

**OUTPUT**:
```
Mayank 103
Emp class called
```

### Subclassing (Calling constructor of parent class)
```
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
```

**OUTPUT**:
```
Rahul
886012
```

Python program to demonstrate error if we forget to invoke __init__() of the parent

If you forget to invoke the __init__() of the parent class then its instance variables would not be available to the child class.

### The super() Function

The super() function is a built-in function that returns the objects that represent the parent class. It allows to access the parent class’s methods and attributes in the child class.

```
# parent class
class Person():
def __init__(self, name, age):
	self.name = name
	self.age = age

def display(self):
	print(self.name, self.age)

# child class
class Student(Person):
def __init__(self, name, age):
	self.sName = name
	self.sAge = age
	# inheriting the properties of parent class
	super().__init__("Rahul", age)

def displayInfo(self):
	print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
```

**OUTPUT**:
```
Rahul 23
Mayank 23
```
