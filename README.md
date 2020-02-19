![](https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)
<h1 align ="center"> AIR BNB CLONE </h1><br>

## What is the Objective?
* ##### THE CONSOLE
    create your data model
    manage (create, update, destroy, etc) objects via a console / command interpreter
    store and persist objects to a file (JSON file)
    The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

    This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
    
    The console will be a tool to validate this storage engine
    
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200219%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200219T212128Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=49edde242ccf7f03b32cb335a5a76f7132c47348938f1d86d0f704d641e60cca)

## Installation 🚀
---
In order to run the shell command interpreter, you must install it in your repository by cloning the following (shown below) in your machine running:
    ```
    git clone https://github.com/Doouh/AirBnB_clone.git
    ```

### Interactive Mode:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit create update show all destroy
(hbnb) all
[]
(hbnb) create User
2015c9b2-d17e-41ab-8355-2bb256eac544
(hbnb) show User 2015c9b2-d17e-41ab-8355-2bb256eac544
[User] (2015c9b2-d17e-41ab-8355-2bb256eac544) {'id': '2015c9b2-d17e-41ab-8355-2bb256eac544', 'created_at': datetime.datetime(2020, 2, 19, 17, 7, 37, 854963), 'updated_at': datetime.datetime(2020, 2, 19, 17, 7, 37, 854989)}
(hbnb) create Place
dc886eec-fe3a-4c06-b161-f90a4d78e0a1
(hbnb) create BaseModel
ba9c5086-de53-4832-a180-7e51cb201e66
(hbnb) all
["[User] (2015c9b2-d17e-41ab-8355-2bb256eac544) {'id': '2015c9b2-d17e-41ab-8355-2bb256eac544', 'created_at': datetime.datetime(2020, 2, 19, 17, 7, 37, 854963), 'updated_at': datetime.datetime(2020, 2, 19, 17, 7, 37, 854989)}", "[Place] (dc886eec-fe3a-4c06-b161-f90a4d78e0a1) {'id': 'dc886eec-fe3a-4c06-b161-f90a4d78e0a1', 'created_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120768), 'updated_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120793)}", "[BaseModel] (ba9c5086-de53-4832-a180-7e51cb201e66) {'id': 'ba9c5086-de53-4832-a180-7e51cb201e66', 'created_at': datetime.datetime(2020, 2, 19, 17, 8, 40, 859003), 'updated_at': datetime.datetime(2020, 2, 19, 17, 8, 40, 859027)}"]
(hbnb) show Place dc886eec-fe3a-4c06-b161-f90a4d78e0a1
[Place] (dc886eec-fe3a-4c06-b161-f90a4d78e0a1) {'id': 'dc886eec-fe3a-4c06-b161-f90a4d78e0a1', 'created_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120768), 'updated_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120793)}
(hbnb) destroy BaseModel ba9c5086-de53-4832-a180-7e51cb201e66
(hbnb) all
["[User] (2015c9b2-d17e-41ab-8355-2bb256eac544) {'id': '2015c9b2-d17e-41ab-8355-2bb256eac544', 'created_at': datetime.datetime(2020, 2, 19, 17, 7, 37, 854963), 'updated_at': datetime.datetime(2020, 2, 19, 17, 7, 37, 854989)}", "[Place] (dc886eec-fe3a-4c06-b161-f90a4d78e0a1) {'id': 'dc886eec-fe3a-4c06-b161-f90a4d78e0a1', 'created_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120768), 'updated_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120793)}"]
(hbnb) destroy User 2015c9b2-d17e-41ab-8355-2bb256eac544
(hbnb) update Place dc886eec-fe3a-4c06-b161-f90a4d78e0a1 City "Medellin"
(hbnb) all Place
["[Place] (dc886eec-fe3a-4c06-b161-f90a4d78e0a1) {'id': 'dc886eec-fe3a-4c06-b161-f90a4d78e0a1', 'created_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120768), 'updated_at': datetime.datetime(2020, 2, 19, 17, 8, 35, 120793), 'City': 'Medellin'}"]
(hbnb) 
(hbnb) quit
$
```
### Non-Interactive Mode:
```sh
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
---
- To read the manual you man run:
```man ./[FILE]``` taking into account the structure, for our case it would be ```man ./man_1_simple_shell```

| File Name | Description and contents |
| --- | --- |
| [models](models) | This is the manpage for the shell command, this will help us know how to use the shell and the many uses of it, in here we can find examples and the correct sintaxis of the commands.|
| [tests](tests) |This is the headers file where we can find all the prototypes of our functions and the structures used.|
| [console](console.py) |In here we have the puts and putchar function it is used to print characters.|
| [Authors](AUTHORS) |In here we have the atoi function it is used to make integers into characters, the alloc funcction to allocate memory and the freeall function to free the memory allocated when it is not needed anymore.|
#### In the future we will go to imporved this project thanks for look
#### Tecnology with we work 🛠️:
* [python3.4](https://docs.python.org/3.4/)
* [bash](https://www.gnu.org/software/bash/)

## ⌨️  with ❤️  By :
* **Kevin Giraldo**
  * [@KevinGiraldo89](https://twitter.com/KevinGiraldo89)
* **Emmanuel Monsalve**
  * [@MonsalveEmmus](https://twitter.com/MonsalveEmmus)
