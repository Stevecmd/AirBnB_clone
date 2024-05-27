# AirBnB_clone
## 0x00. AirBnB clone - The console
This is the first instalment of the AirBnB project in collaboration with Steve.

## General
- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Solutions to the Questions Above

1. Creating a Python Package:

    Structure: <br/>
    Create a directory for your package (e.g., mypackage).
    Inside, create Python modules (.py files) containing your code.
    An empty __init__.py file is essential in the package directory to mark it as a package.
    Optional setup.py for installation:
    Use setuptools to create a setup.py file defining metadata and build instructions for sharing/installing your package.

2. Command Interpreter with cmd Module:

    Import the cmd module. <br/>
    Create a subclass of cmd.Cmd.
    Override methods like do_exit(), do_help(), and define custom command methods (e.g., do_greet(self, args)).
    Use cmdloop() to start the interpreter.

3. Unit Testing:

    Unit testing verifies the correctness of individual functions or modules.
    Use a testing framework like unittest or pytest.
    Write test cases as functions that:
    Set up the test environment.
    Call the function to be tested.
    Assert expected results using assertEqual, assertTrue, etc.

4. Serialization and Deserialization of a Class:

    Serialization converts an object into a byte stream for storage or transmission.
    Deserialization reconstructs the object from the byte stream.
    Use modules like pickle or json for basic use cases.
    Consider more robust solutions like dataclasses and marshmallow for complex scenarios.

5. Reading and Writing JSON Files:

    Import the json module 
    Use json.dump(data, file) to write a dictionary or list to a JSON file.
    Use json.load(file) to read JSON data from a file and convert it back to a Python object.

6. Managing Datetime:

    Import the datetime module.
    Use datetime.now() to get the current date and time.
    Create datetime objects with specific dates and times.
    Apply methods for formatting, arithmetic, and time zone handling.

7. UUID (Universally Unique Identifier):

    A unique identifier generated to ensure no collisions.
    Use the uuid module to generate UUIDs (e.g., uuid.uuid4()).
    Useful for database IDs, tracking objects, etc.

8. *args and **kwargs:

    *args captures an arbitrary number of positional arguments as a tuple.
    Use it in function definitions (e.g., def my_function(*args):).
    Access arguments within the function using indexing (e.g., args[0], args[1:]).
    **kwargs captures an arbitrary number of keyword arguments as a dictionary.
    Use it in function definitions (e.g., def my_function(**kwargs):).
    Access arguments within the function using dictionary keys (e.g., kwargs['name']).

9. Named Arguments in Functions:

    Pass arguments by name using keyword syntax (e.g., my_function(name="Alice")).
    Enforces clarity and avoids positional errors.

## Requirements
### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the `unittest module`
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
    > e.g., For models/base_model.py, unit tests must be in: `tests/test_models/test_base_model.py`
    > e.g., For models/user.py, unit tests must be in: `tests/test_models/test_user.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## W3C validator
[W3C validator for Holberton School](https://github.com/alx-tools/W3C-Validator)

Sample use:

Quickstart

Clone this repo: 
`
git clone https://github.com/holbertonschool/W3C-Validator.git`

> Run the validator command from within

>> Single file:

```sh
./w3c_validator.py index.html

./w3c_validator.py css/styles.css
```

>> Multiple files:

```sh
./w3c_validator.py index.html article.html css/styles.css
```

All errors are printed in STDERR; `Exit status = # of errors (0 on success)`


Running the W3C validator:
```sh
root@356e29ffef03:/# ls
AirBnB_clone
```
Assuming the folder structure below:

```sh
root@356e29ffef03:/AirBnB_clone# cd web_static/
root@356e29ffef03:/AirBnB_clone/web_static# ls
0-index.html  1-index.html  2-index.html  3-index.html  images  styles

```
Run the following command:

```sh
root@356e29ffef03:/AirBnB_clone# ../W3C-Validator/w3c_validator.py web_static/0-index.html
'web_static/0-index.html' => OK

```

To check all the html files at once:

```sh
root@356e29ffef03:/AirBnB_clone$ ../W3C-Validator/w3c_validator.py web_static/*.html
'web_static/4-index.html' => Section lacks heading. Consider using “h2”-“h6” elements to add identifying headings to all sections, or else use a “div” element instead for any cases where no heading is needed.
'web_static/0-index.html' => OK
'web_static/1-index.html' => OK
'web_static/2-index.html' => OK
'web_static/3-index.html' => OK
'web_static/5-index.html' => OK
'web_static/6-index.html' => OK
'web_static/7-index.html' => OK
'web_static/8-index.html' => OK
```

Check the css files as shown below:
```sh

AirBnB_clone$ ../W3C-Validator/w3c_validator.py web_static/styles/*.css
'web_static/styles/2-common.css' => OK
'web_static/styles/2-footer.css' => OK
'web_static/styles/2-header.css' => OK
'web_static/styles/3-common.css' => OK
'web_static/styles/3-footer.css' => OK
'web_static/styles/3-header.css' => OK
'web_static/styles/4-common.css' => OK
'web_static/styles/4-filters.css' => OK
'web_static/styles/5-filters.css' => OK
'web_static/styles/6-filters.css' => OK
'web_static/styles/7-places.css' => OK
'web_static/styles/8-places.css' => OK

```