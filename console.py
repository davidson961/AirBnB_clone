#!/usr/bin/python3
"""This module defines HBNBCommand, the entry
point of the command interpreter."""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, User, State, City, Amenity, Place, or Review, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            class_name, obj_id = args[0], args[1]
            obj_key = "{}.{}".format(class_name, obj_id)
            obj_instance = storage.all().get(obj_key)
            if obj_instance:
                print(obj_instance)
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name, obj_id = arg.split()
            obj_key = "{}.{}".format(class_name, obj_id)
            obj_instance = storage.all().get(obj_key)
            if obj_instance:
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances based on the class name."""
        if arg:
            try:
                class_name = eval(arg).__name__
                filtered_objs = {k: v for k, v in storage.all().items() if class_name in k}
            except NameError:
                print("** class doesn't exist **")
                return
        else:
            filtered_objs = storage.all()

        print([str(obj) for obj in filtered_objs.values()])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        try:
            class_name = eval(args[0]).__name__
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        obj_instance = storage.all().get(obj_key)

        if obj_instance is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        if hasattr(obj_instance, attribute_name):
            attribute_type = type(getattr(obj_instance, attribute_name))
            try:
                casted_value = attribute_type(attribute_value)
                setattr(obj_instance, attribute_name, casted_value)
                obj_instance.save()
            except ValueError:
                pass
        else:
            print("** no instance found **")

    def default(self, arg):
        """Handle default behavior for unrecognized commands."""
        try:
            class_name, command = arg.split('.')
            if command == 'all()':
                self.do_all(class_name)
            elif command == 'count()':
                self.do_count(class_name)
            elif command.startswith('show(') and command.endswith(')'):
                obj_id = command.split('(')[1][:-1]
                self.do_show("{} {}".format(class_name, obj_id))
            elif command.startswith('destroy(') and command.endswith(')'):
                obj_id = command.split('(')[1][:-1]
                self.do_destroy("{} {}".format(class_name, obj_id))
            elif command.startswith('update(') and command.endswith(')'):
                if '{' in command and '}' in command:
                    obj_id, update_dict = command.split('(')[1][:-1].split(', ')
                    update_dict = json.loads(update_dict)
                    for k, v in update_dict.items():
                        self.do_update("{} {} {} {}".format(class_name, obj_id, k, v))
                else:
                    print("** invalid syntax: {} **".format(arg))
            else:
                print("*** Unknown syntax: {}".format(arg))
        except ValueError:
            print("*** Unknown syntax: {}".format(arg))

    def do_count(self, arg):
        """Print the number of instances of a class."""
        try:
            class_name = eval(arg).__name__
            filtered_objs = {k: v for k, v in storage.all().items() if class_name in k}
            print(len(filtered_objs))
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
