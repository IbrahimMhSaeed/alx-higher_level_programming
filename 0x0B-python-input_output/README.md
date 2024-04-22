# Input/Output

open() returns a file object, and is most commonly used with two positional arguments and one keyword argument:

`open(filename, mode, encoding=None)`

```
f = open('workfile', 'w', encoding="utf-8")
```

## File Object
Every file contains three main parts:

1. Header: This contains information about the file i.e. file name, file type, file size etc.
2. Data: This is the actual information/content stored in the file.
3. End of file: This is a special character that marks the end of the file.

```
>>> a_file = open('file.txt', encoding='utf-9)
>>> a_file.name
file.txt
>>> a_file.encoding
'utf-8'
>>> a_file.mode
'r'
```

### How to Read File:
using `with` statement`
```
with open('workfile', encoding="utf-8") as f:
	read_data = f.read()

# We can check that the file has been automatically closed.

>>> f.closed
True
```

**Close manually:**
```
f.close()
```
### Access Modes

|Mode 	|Function
|-------|----------
|r 	|Reading. This is the default mode.
|w 	|Writing. If the file already exists, overwrite its contents. Create a new file if the file does not exist.
|a 	|Appending. Preserve the file’s contents, add new data to the end of the file.
|r+ 	|reading/writing
|w+ 	|write/read
|a+ 	|appending/reading
|b	|Binary Mode

### different File Object Methods

|Method	|What it does
|-------|--------------
|read(size=-1)	|read whole file --> if EOF returns (empty string)
|read(size)	|read specific num of chars
|readline(size = -1)	|This reads size number of bytes from the line. If we pass no argument value, it reads the entire line.
|readlines()	|Reads all the lines from a file and returns a list of the lines, separating them from one another with commas.
|write(string)	|takes a string as an argument and writes it into the file. This function returns the number of characters written into the file.
|writelines(list_of_strings)	|takes a list of strings as an argument and writes those strings into the file. Be sure to append a “\n” at the end of a string to make it act as a line.
|seek(offset, whence)	|move cursor to specific location,  offset – The number of positions(bytes) to move forward, whence - the position from where you want to move forward.
|tell()		|location of cursor

*Example for writelines(list_of_strings)*
```
>>> lines = ["Second line\n", "Third line\n", "Fourth line\n"]
>>> f.writelines(lines)
>>> f.close()
```
*General Example:*
```
>>> a_file.read()
>>> a_file.seek(0)
0
>>> a_file.read(16)
'Dive into Python'
>>> a_file.read(1)
' '
>>> a_file.read(1)
'd'
>>> a_file.tell()
20
```
## Open a File and Read Lines

```
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

## JSON encoder and decoder
JSON (JavaScript Object Notation) is useful to know because many websites offer JSON content as a way for programs interact with website.

Accessing an API is the same as accessing any web page via URL.


Encoding basic Python object hierarchies:
```
>>> import json
>>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
```

Pretty printing:
```
>>> import json

>>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}
```

Decoding JSON:
```
>>> import json

>>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
['foo', {'bar': ['baz', None, 1.0, 2]}]
```

### JSON Methods

- json.dump(obj, fp)
Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object)

- json.dumps(obj)
Serialize obj to a JSON formatted str using this conversion table.

- json.load(fp)
Deserialize fp (a .read()-supporting text file or binary file containing a JSON document) to a Python object using this conversion table.

- json.loads(s)
Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object using this conversion table.

### JSON Decoder

|JSON	|Python|
|-------|-------
|object	|dict|
|array	|list|
|string	|str|
|number (int)	|int|
|number (real)	|float|
|true	|True|
|false	|False|
|null	|None|

### JSON encoder for Python data structures

|Python	|JSON|
|-------|------|
|dict	|object|
|list, tuple	|array|
|str	|string|
|int, float, int- & float-derived Enums	|number|
|True	|true|
|False	|false|
|None	|null|

### Project: Fetching Current Weather Data

Functionality of program:
1) reads requested location from Command Line
2) Downloads JSON weather data from OpenWeatherMap.org
3) Converts string of JSON to Python Data structure
4) Print weather for today and next two days

Algorithm:
1) Join strings in sys.argv to get location
2) Call requests.get() to download weather data
3) Call json.loads() to convert JSON to Python
4) Print the weather forcast

```
#!/usr/bin/python3

import sys, json, requests

# Get the location
if len(sys.argv) < 2:
	print("Usage: quickWeather.py location")
	sys.exit()
location = "".join(sys.argv[1:])

# Download JSON data

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3" % (location)
response = requests.get(url)
response.raise_for_status()

# Load Json data into Python

weatherData = json.loads(response)

# Display Data to User
```

## Other File Methods

|Method 	|What it does
|---------------|--------------------
|close() 	|Closes the file.
|flush() 	|Flushes the internal buffer.
|fileno() 	|Returns the file descriptor of the file.
|next() 	|Returns the next line from the file.
|read(size) 	|Reads size number of bytes from the file. Reads the entire file if you don’t pass any argument value.
|readline(size) |Reads one line from a file. 
|readlines() 	|Reads the entire file and returns a list of the lines.
|seek(offset, whence) 	|Lets us control the position of the file pointer.
|tell() 	|Returns the current position of the file pointer.
|truncate(size) |It truncates the file to the specified size.
|writable() 	|Returns True if we can write into the file.
|write(string) 	|Writes string into the file.
|writelines(list_of_strings) 	|Writes each element of the list_of_strings into the file.
