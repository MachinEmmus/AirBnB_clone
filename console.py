#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""
    This file contains the entry point of the command interpreter.
    We use the module cmd and the class is HBNBCommand.
"""


class HBNBCommand(cmd.Cmd):
    """
        This is the main class, its methods allow us to interact
        with all another classes like BaseModel, User, etcetera.
    """

    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "City", "Amenity",
                  "Place", "Review", ]

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit with a signal EOF"""
        print("")
        return True

    def emptyline(self):
        """This method allow us to ignore the empty line"""
        pass

    def do_create(self, args):
        """Creates a new instance of any existing class.\n
        Usage: create <class name>"""
        if args == "":
            print("** class name missing **")
            return
        try:
            cmmd = args.split()
            instance = eval(cmmd[0])()
            instance.save()
            print(instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance.\n
        Usage: show <class name> <id>"""
        if args == "":
            print("** class name missing **")
            return
        cmmd = args.split()
        if not (cmmd[0] in HBNBCommand.class_list):
            print("** class doesn't exist **")
            return
        if len(cmmd) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if (obj.id == cmmd[1] and obj.__class__.__name__ == cmmd[0]):
                print(obj)
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance.\n
        Usage: destroy <class name> <id>"""
        if args == "":
            print("** class name missing **")
            return
        cmmd = args.split()
        if not (cmmd[0] in HBNBCommand.class_list):
            print("** class doesn't exist **")
            return
        if len(cmmd) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id, value in all_objs.items():
            obj = all_objs[obj_id]
            if (obj.id == cmmd[1] and obj.__class__.__name__ == cmmd[0]):
                del all_objs[obj_id]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all or some
specific class among the saved instances.\n
        Usage: all
               all <class name>"""
        try:
            cmmd = args.split()
            if len(cmmd) == 0:
                lis = []
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    lis.append(obj.__str__())
                print(lis)
            elif len(cmmd) == 1:
                all_objs = storage.all()
                lis = []
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    if (obj.__class__.__name__ == cmmd[0]):
                        lis.append(obj.__str__())
                if len(lis) == 0:
                    print("** class doesn't exist **")
                    return
                print(lis)
        except Exception:
            pass

    def do_update(self, args):
        """Updates an instance.\n
        Usage: update <class name> <id> <attribute name> "<value>\" """
        if args == "":
            print("** class name missing **")
            return
        cmmd = args.split()
        if not (cmmd[0] in HBNBCommand.class_list):
            print("** class doesn't exist **")
            return
        if len(cmmd) < 2:
            print("** instance id missing **")
            return
        elif len(cmmd) < 3:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if (obj.id == cmmd[1]):
                    print("** attribute name missing **")
                    return
            print("** no instance found **")
            return
        elif len(cmmd) < 4:
            print("** value missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if (obj.id == cmmd[1] and obj.__class__.__name__ == cmmd[0]):
                if cmmd[3][0] == '\"':
                    txt = ""
                    for i in range(3, len(cmmd)):
                        txt += cmmd[i]
                        txt += " "
                        if (cmmd[i][len(cmmd[i])-1] == "\""):
                            break
                    new = txt[1:len(txt)-2]
                    setattr(all_objs[obj_id], cmmd[2], new)
                else:
                    if ("." in cmmd[3]):
                        setattr(all_objs[obj_id], cmmd[2], float(cmmd[3]))
                    else:
                        setattr(all_objs[obj_id], cmmd[2], int(cmmd[3]))
                storage.save()
                return
        print("** no instance found **")

    def default(self, args):
        args = args.replace(".", "*-*", 1)
        args = args.replace("(", "*-*")
        args = args.replace(")", "*-*")
        args = args.replace("\"", "*-*")
        args = args.replace(", ", "*-*")
        cmmd = args.split("*-*")

        if (len(cmmd) < 2):
            print("*** Unknown syntax:", cmmd[0])
            return

        if (cmmd[1] == "all"):
            args = cmmd[0]
            HBNBCommand.do_all(None, args)
            return

        if (cmmd[1] == "count"):
            if (cmmd[0] in HBNBCommand.class_list):
                all_objs = storage.all()
                count = 0
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    if (obj.__class__.__name__ == cmmd[0]):
                        count += 1
                print(count)
                return
            else:
                print("** class doesn't exist **")
                return

        if (cmmd[1] == "show"):
            args = cmmd[0] + " " + cmmd[3]
            HBNBCommand.do_show(None, args)
            return

        if (cmmd[1] == "destroy"):
            args = cmmd[0] + " " + cmmd[3]
            HBNBCommand.do_destroy(None, args)
            return

        if (cmmd[1] == "update"):
            if (len(cmmd) == 12):
                args = cmmd[0] + " " + cmmd[3] + " " + cmmd[6] + " \"" +\
                        cmmd[9] + "\""
            elif (len(cmmd) == 10):
                args = cmmd[0] + " " + cmmd[3] + " " + cmmd[6] + " " + cmmd[8]
            HBNBCommand.do_update(None, args)
            return

        print("*** Unknown syntax:", cmmd[0])


if __name__ == '__main__':
    """
        Call The Shell
    """
    HBNBCommand().cmdloop()
