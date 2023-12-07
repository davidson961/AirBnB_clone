#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is the HBNBCommand class."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel and print its id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()

    def do_count(self, arg):
        """Count the number of instances of a class."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        count = 0
        for key, obj in storage.all().items():
            if key.startswith(class_name + "."):
                count += 1
        print(count)

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = shlex.split(arg)
        obj_list = []
        if not args or args[0] not in globals():
            print("** class doesn't exist **")
            return
        class_name == args[0]:
            all_instances = eval(class_name).all()
            for obj in all_instances:
                obj_list.append(str(obj))
                print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** dictionary  missing **")
            else:
                obj = storage.all()[key]
                try:
                    attr_dict = eval(args[2])
                    if not isinstance(attr_dict, dict):
                        raise SyntaxError
                    except (SyntaxError, NameError):
                        print("** invalid dictionary representation **")
                        return
                    for k, v in attr_dict.items():
                        if hasattr(obj, k):
                            attr_type = type(getattr(obj, k))
                            setattr(obj, k, attr_type(v))
                            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
