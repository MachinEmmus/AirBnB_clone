![](https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)
<h1 align ="center"> AIR BNB CLONE </h1><br>
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
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
    git clone https://github.com/shincap8/simple_shell.git
    ```
### Interactive Mode:
```sh
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
### Non-Interactive Mode:
```sh
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
