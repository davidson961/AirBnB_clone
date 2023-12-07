#!/usr/bin/python3
"""
Module containing the HBNBCommand class for the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implementing the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, User, save it, and print the id.
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                print(FileStorage.all().get(key, "** no instance found **"))
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                all_objs = FileStorage.all()
                if key in all_objs:
                    del all_objs[key]
                    FileStorage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
        """
        args = arg.split()
        all_objs = FileStorage.all()
        if not args:
            print([str(v) for v in all_objs.values()])
        else:
            try:
                class_name = args[0]
                if class_name in FileStorage.classes():
                    print([str(v) for k, v in all_objs.items() if class_name in k])
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                all_objs = FileStorage.all()
                if key not in all_objs:
                    print("** no instance found **")
                    return
                if len(args) < 3:
                    print("** instance id missing **")
                    return
                attr_name = args[2]
                if len(args) < 4:
                    print("** value missing **")
                    return
                attr_value = args[3]
                obj_instance = all_objs[key]
                setattr(obj_instance, attr_name, eval(attr_value))
                FileStorage.save()
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
