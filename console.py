#!/usr/bin/python3
"""
Console module for HBNB project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using EOF (Ctrl+D)
        """
        print()
        return True

    def help_quit(self):
        """
        Display help for the quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help for the EOF command (Ctrl+D)
        """
        print("Exit the program using EOF (Ctrl+D)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
