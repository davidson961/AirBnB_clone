#!/usr/bin/python3
"""
Module containing the HBNBCommand class for the command interpreter
"""

import cmd
import re
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of all instances."""
        class_name = line.split()[0] if line else None
        if class_name and class_name not in storage.classes():
            print("** class doesn't exist **")
            return
            
            instances = storage.all()
            if class_name:
                filtered_instances = [str(obj) for obj in instances.values() if isinstance(obj, eval(class_name))]
                print(filtered_instances)
            else:
                all_instances = [str(obj) for obj in instances.values()]
                print(all_instances)


    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], eval(args[3]))
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
