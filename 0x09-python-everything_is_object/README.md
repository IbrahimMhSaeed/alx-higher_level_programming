# Everything is an Object

**Object:** An object is something a variable can refer to.

## Objects and values

If we execute these assignment statements,
```
a = "banana"
b = "banana"
```
we know that a and b will refer to a string with the letters "banana".
*There are two possible states:*

|a => "banana"		|a =>
|			|	=> "banana"
|b => "banana"		|b =>

**Since strings are immutable, Python optimizes resources by making two names that refer to the same string value refer to the same object.**

```
>>> a == b
True

>>> a is b
True
```

But at this case:
```
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]

>>> a == b
True

>>> a is b
False
```
a and b have the same value but do not refer to the same object.

## Aliasing

Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:
```
>>> a = [1, 2, 3]
>>> b = a
>>> a is b
True
```
This is called **Aliasing**

Changes made with one alias affect the other:
```
>>> b[0] = 5
>>> print a
[5, 2, 3]
```
## Immutable vs Mutable types

You have to understand that Python represents all its data as objects. Some of these objects like lists and dictionaries are mutable, meaning you can change their content without changing their identity. Other objects like integers, floats, strings and tuples are objects that can not be changed. An easy way to understand that is if you have a look at an objects ID.

**Common immutable type:**
- numbers: int(), float(), complex()
- immutable sequences: str(), tuple(), frozenset(), bytes()

**Common mutable type (almost everything else):**
- mutable sequences: list(), bytearray()
- set type: set()
- mapping type: dict()
- classes, class instances
- etc.

```
>>> s = "abc"
>>> id(s)
4702124
>>> s[0] 
'a'
>>> s[0] = "o"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s = "xyz"
>>> id(s)
4800100
>>> s += "uvw"
>>> id(s)
4800500
```
You can do that with a list and it will not change the objects identity
```
>>> i = [1,2,3]
>>> id(i)
2146718700
>>> i[0] 
1
>>> i[0] = 7
>>> id(i)
2146718700
```
## Mutable Data

### Sequence Objects
#### Lists
Referto shallow and deepcopy of lists (Python Tricks)

This produce shallow copies of y
```
y = [1, 2, 3]
x = list(y)	#[1, 2, 3] any change in one of these will appear in x & y
x = y[:]
```
List comprehension produce Deepcopy
```
x = [1, 2, 3]
y = [ele for ele in x]
```

#### Tuples
Is an immutable sequence. Tuples are created using a tuple literal that separates element expressions by commas. Parentheses are optional but used commonly in practice. 
```
>>> 1, 2 + 3
(1, 5)
>>> ("the", 1, ("and", "only"))
('the', 1, ('and', 'only'))
>>> type( (10, 20) )
<class 'tuple'>
```
Empty and one-element tuples have special literal syntax.
```
>>> ()    # 0 elements
()
>>> (10,) # 1 element
(10,)
```
While it is not possible to change which elements are in a tuple, it is possible to change the value of a mutable element contained within a tuple.

*Think of a variable as a label and the value inside the box. the variabel equals the label => reference of list, you can't assign it a new list, but you can change the list that holds the same reference*
```
nest = (10, 20, [30, 40])
nest[2].pop()
```

#### Dictionaries
**Dictionaries do have some restrictions:**
- A key of a dictionary cannot be or contain a mutable value.
- There can be at most one value for a given key.

A useful method implemented by dictionaries is `get`, which returns either the value for a key, if the key is present, or a default value. The arguments to `get` are the key and the default value.
```
>>> numerals.get('A', 0)
0
>>> numerals.get('V', 0)
5
```

