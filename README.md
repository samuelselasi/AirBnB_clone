# 0x00. AirBnB clone - The console
### `Group project` `Python` `OOP`

## Background Context
Welcome to the **AirBnB** clone project!

The aim of the project is to deploy on one's own server
a simple copy of the [AirBnB website](https://www.airbnb.com/).

## Resources
**Read or watch**:

* [cmd module]()
* [cmd module in depth]()
* **packages concept page**
* [uuid module]()
* [datetime]()
* [unittest module]()
* [args/kwargs]()
* [Python test cheatsheet]()
* [cmd module wiki page]()
* [python unittest]()

## General
# Command Line Interpreter for Airbnb Clone - The Console
This command line interpreter is designed for an Airbnb clone application. It allows users to interact with the application's backend through a console, where they can create and manage instances of the application's classes.

## How to Use
To start the console, run the script `console.py`. This will start the command line interpreter, and the prompt `(hbnb)` will be displayed. This prompt indicates that the console is ready to accept user input.

The following commands are available:

* `create`: Creates a new instance of a class.
* `show`: Prints the string representation of an instance.
* `destroy`: Deletes an instance based on the class name and ID.
* `all`: Prints all string representations of all instances, or all instances of a particular class.
* `update`: Updates an instance based on the class name and ID.
* `count`: Counts the instances of a class.
* `EOF`: Exits the console.
* `quit`: Exits the console.

The syntax for each command is as follows:

* `create <class name>`: Creates a new instance of the specified class.
* `show <class name> <instance id>`: Prints the string representation of the specified instance.
* `destroy <class name> <instance id>`: Deletes the specified instance.
* `all`: Prints the string representations of all instances.
* `all <class name>`: Prints the string representations of all instances of the specified class.
* `update <class name> <instance id> <attribute name> "<attribute value>"`: Updates the specified instance with the specified attribute value.
* `count <class name>`: Counts the instances of the specified class.

## Requirements
### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder [tests](./tests)
* You have to use the [unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest) module
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start by `test_`
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
*  All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## More Info
### Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`



## Tasks
0.[README](./README.md), [AUTHORS](./AUTHORS)

* Write a `README.md`:
	* description of the project
	* description of the command interpreter:
		* how to start it
		* how to use it
		* examples
* You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format,
reference [Docker’s AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS)

[1. Be pycodestyle compliant!](./AirBnB_clone)

Write beautiful code that passes the `pycodestyle` checks.

[2. Unittests](./tests)

All files, classes, functions must be tested with unit tests.
```
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
*Note that this is just an example, the number of tests you create can be different from the above example.*

**Warning**:

Unit tests must also pass in non-interactive mode:
```
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

[3. BaseModel](./models/base_model.py)

Write a class `BaseModel` that defines all common attributes/methods for other classes:

* `models/base_model.py`
* Public instance attributes:
	* `id`: string - assign with an `uuid` when an instance is created:
		* you can use `uuid.uuid4()` to generate unique `id` but don’t forget to convert to a string
		* the goal is to have unique `id` for each `BaseModel`
	* `created_at`: datetime - assign with the current datetime when an instance is created
	* `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
* `__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`
* Public instance methods:
	* save(self): updates the public instance attribute `updated_at` with the current datetime
	* to_dict(self): returns a dictionary containing all `keys/values` of `__dict__` of the instance:
		* by using `self.__dict__`, only instance attributes set will be returned
		* a key `__class__` must be added to this dictionary with the class name of the object
		* `created_at` and `updated_at` must be converted to string object in ISO format:
			* format: `%Y-%m-%dT%H:%M:%S.%f` (`ex: 2017-06-14T22:31:03.285259`)
			* you can use `isoformat()` of `datetime` object
		* This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$
```

[4. Create BaseModel from dictionary](./models/base_model.py)

Previously we created a method to generate a dictionary representation of an instance (method `to_dict()`).

Now it’s time to re-create an instance with this dictionary representation.
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
Update `models/base_model.py`:

* `__init__(self, *args, **kwargs)`:
	* Use `*args, **kwargs` arguments for the constructor of a `BaseModel`.
	* `*args` won’t be used
	* if `kwargs` is not empty:
		* each key of this dictionary is an attribute name (**Note** `__class__` from `kwargs` is the only one that should not be added as an attribute. See the example output, below)
		* each value of this dictionary is the value of this attribute name
		* **Warning**: `created_at` and `updated_at` are strings in this dictionary, but inside the `BaseModel` instance is working with `datetime` object. Convert these strings into `datetime` object. Tip: you know the string format of these datetime
	* otherwise:
		* create `id` and `created_at` as you did previously (new instance)
```
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$
```

[5. Store first object](./models/engine/file_storage.py)

Now recreate a `BaseModel` from another one by using a dictionary representation:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

* Python doesn’t know how to convert a string to a dictionary (easily)
* It’s not human readable
* Using this file with another program in Python or other language will be hard.

So, convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
Magic right?

Terms:

* **simple Python data structure**: Dictionaries, arrays, number and string. ex: `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`
* **JSON string representation**: String representing a simple data structure in JSON format. ex: `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`

Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:

* `models/engine/file_storage.py`
* Private class attributes:
	* `__file_path`: string - path to the JSON file (ex: `file.json`)
	* `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)
* Public instance methods:
	* `all(self)`: returns the dictionary `__objects`
	* `new(self, obj)`: sets in `__objects` the obj with key `<obj class name>.id`
	* `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`)
	* `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Update `models/__init__.py`: to create a unique `FileStorage` instance for your application

* import `file_storage.py`
* create the variable storage, an instance of `FileStorage`
* call `reload()` method on this variable

Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`

* import the variable `storage`
* in the method `save(self)`:
	* call `save(self)` method of storage
* `__init__(self, *args, **kwargs)`:
	* if it’s a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`
```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$
```

[6. Console 0.0.1](./console.py)

Write a program called `console.py` that contains the entry point of the command interpreter:

* You must use the module `cmd`
* Your class definition must be: `class HBNBCommand(cmd.Cmd):`
* Your command interpreter should implement:
	* `quit` and `EOF` to exit the program
	* `help` (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
	* a custom prompt: `(hbnb)`
	* an empty line + `ENTER` shouldn’t execute anything
* Your code should not be executed when imported

**Warning**:

You should end your file with:
```
if __name__ == '__main__':
    HBNBCommand().cmdloop()
```
to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$
```
**No unittests needed**

[7. Console 0.1](./console.py)

Update command interpreter (`console.py`) to have these commands:

* `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
	* If the class name is missing, print ** class name missing ** (ex: $ create)
	* If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ create MyModel`)
* `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234.`
	* If the class name is missing, print `** class name missing **` (ex: `$ show`)
	* If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ show MyModel`)
	* If the `id` is missing, print `** instance id missing **` (ex: `$ show BaseModel`)
	* If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ show BaseModel 121212`)
* `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234.`
	* If the class name is missing, print `** class name missing **` (ex: `$ destroy`)
	* If the class name doesn’t exist, print `** class doesn't exist **` (ex:`$ destroy MyModel`)
	* If the `id` is missing, print `** instance id missing **` (ex: `$ destroy BaseModel`)
	* If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ destroy BaseModel 121212`)
* `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` or `$ all`.
	* The printed result must be a list of strings
	* If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ all MyModel`)
* `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
	* Usage: `update <class name> <id> <attribute name> "<attribute value>"`
	* Only one attribute can be updated at the time
	* You can assume the attribute name is valid (exists for this model)
	* The attribute value must be casted to the attribute type
	* If the class name is missing, print `** class name missing **` (ex: `$ update`)
	* If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ update MyModel`)
	* If the `id` is missing, print `** instance id missing **` (ex: `$ update BaseModel`)
	* If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ update BaseModel 121212`)
	* If the attribute name is missing, print `** attribute name missing **` (ex: `$ update BaseModel existing-id`)
	* If the value for the attribute name doesn’t exist, print `** value missing **` (ex: `$ update BaseModel existing-id first_name`)
	* All other arguments should not be used (Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)
	* `id`, `created_at` and `updated_at` cant’ be updated. You can assume they won’t be passed in the update command
	* Only “simple” arguments can be updated: `string`, `integer` and `float`. You can assume nobody will try to update list of ids or `datetime`

Let’s add some rules:

* You can assume arguments are always in the right order
* Each arguments are separated by a space
* A string argument with a space must be between double quote
* The error management starts from the first argument to the last one
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```
**No unittests needed**

8. First User

Write a class User that inherits from BaseModel:

models/user.py
Public class attributes:
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string
Update FileStorage to manage correctly serialization and deserialization
of User.

Update command interpreter (console.py) to allow show, create, destroy, 
update and all used with User.

9. More classes!

Write all those classes that inherit from BaseModel:

State (models/state.py):
Public class attributes:
name: string - empty string
City (models/city.py):
Public class attributes:
state_id: string - empty string: it will be the State.id
name: string - empty string
Amenity (models/amenity.py):
Public class attributes:
name: string - empty string
Place (models/place.py):
Public class attributes:
city_id: string - empty string: it will be the City.id
user_id: string - empty string: it will be the User.id
name: string - empty string
description: string - empty string
number_rooms: integer - 0
number_bathrooms: integer - 0
max_guest: integer - 0
price_by_night: integer - 0
latitude: float - 0.0
longitude: float - 0.0
amenity_ids: list of string - empty list: will be the list of Amenity.id later
Review (models/review.py):
Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string

10. Console 1.0

Update FileStorage to manage correctly serialization and deserialization of
all our new classes: Place, State, City, Amenity and Review

Update command interpreter (console.py) to allow those actions: show, create,
destroy, update and all with all classes created previously.

11. All instances by class name

Update command interpreter (console.py) to retrieve all instances of a class
by using: <class name>.all().

12. Count instances

Update command interpreter (console.py) to retrieve the number of instances
of a class: <class name>.count().

13. Show

Update command interpreter (console.py) to retrieve an instance based on
its ID: <class name>.show(<id>).

Errors management must be the same as previously.

14. Destroy

Update your command interpreter (console.py) to destroy an instance based
on his ID: <class name>.destroy(<id>).

Errors management must be the same as previously.

15. Update

Update command interpreter (console.py) to update an instance based on
his ID: <class name>.update(<id>, <attribute name>, <attribute value>).

Errors management must be the same as previously.

16. Update from dictionary

Update command interpreter (console.py) to update an instance based on
his ID with a dictionary:
<class name>.update(<id>, <dictionary representation>).

Errors management must be the same as previously.

17. Unittests for the Console!

Write all unittests for console.py, all features!

For testing the console, you should “intercept” STDOUT of it.
