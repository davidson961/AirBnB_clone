#!/usr/bin/python3
""" Test functions for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test the HBNBCommand class."""

    def setUp(self):
        """Set up for the test cases."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up for the test cases."""
        del self.console

    def capture_stdout(self, command):
        """Capture the output of the console."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(command)
            return f.getvalue()

    def test_quit(self):
        """Test the quit command."""
        output = self.capture_stdout("quit")
        self.assertEqual(output, "")

    def test_EOF(self):
        """Test the EOF command."""
        output = self.capture_stdout("EOF")
        self.assertEqual(output, "")

    def test_emptyline(self):
        """Test the emptyline method."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """Test the create command."""
        output = self.capture_stdout("create BaseModel")
        self.assertTrue(len(output) > 0)

    def test_show(self):
        """Test the show command."""
        output = self.capture_stdout("show BaseModel")
        self.assertEqual(output, "** instance id missing **\n")

        output = self.capture_stdout("show BaseModel 1234")
        self.assertEqual(output, "** no instance found **\n")

    def test_destroy(self):
        """Test the destroy command."""
        output = self.capture_stdout("destroy BaseModel")
        self.assertEqual(output, "** class name missing **\n")

        output = self.capture_stdout("destroy BaseModel 1234")
        self.assertEqual(output, "** no instance found **\n")

    def test_all(self):
        """Test the all command."""
        output = self.capture_stdout("all")
        self.assertTrue(output.startswith("["))

        output = self.capture_stdout("all BaseModel")
        self.assertTrue(output.startswith("[]"))

    def test_update(self):
        """Test the update command."""
        output = self.capture_stdout("update")
        self.assertEqual(output, "** class name missing **\n")

        output = self.capture_stdout("update BaseModel")
        self.assertEqual(output, "** instance id missing **\n")

        output = self.capture_stdout("update BaseModel 1234")
        self.assertEqual(output, "** attribute name missing **\n")

        output = self.capture_stdout("update BaseModel 1234 name")
        self.assertEqual(output, "** value missing **\n")

        output = self.capture_stdout("update BaseModel 1234 name 'New Name'")
        self.assertEqual(output, "** no instance found **\n")

    def test_default(self):
        """Test the default method."""
        output = self.capture_stdout("unknown_command")
        self.assertEqual(output, "*** Unknown syntax: unknown_command\n")

    def test_count(self):
        """Test the count command."""
        output = self.capture_stdout("count")
        self.assertEqual(output, "** class name missing **\n")

        output = self.capture_stdout("count BaseModel")
        self.assertTrue(output.isdigit())

    def test_update_with_dict(self):
        """Test the update command with dictionary representation."""
        output = self.capture_stdout("update BaseModel")
        self.assertEqual(output, "** class name missing **\n")

        output = self.capture_stdout("update BaseModel 1234")
        self.assertEqual(output, "** instance id missing **\n")

        output = self.capture_stdout("update BaseModel 1234 {'name': 'New Name'}")
        self.assertEqual(output, "** attribute name missing **\n")

        output = self.capture_stdout("update BaseModel 1234 name")
        self.assertEqual(output, "** value missing **\n")

        output = self.capture_stdout("update BaseModel 1234 name 'New Name'")
        self.assertEqual(output, "** no instance found **\n")

    def test_custom_commands(self):
        """Test the custom commands."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show(1234)")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

            self.console.onecmd("BaseModel.destroy(1234)")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

            self.console.onecmd("BaseModel.update(1234, name, 'New Name')")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

            self.console.onecmd("BaseModel.update(1234, {'name': 'New Name'})")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_custom_commands_with_existing_instance(self):
        """Test the custom commands with an existing instance."""
        output = self.capture_stdout("create BaseModel")
        obj_id = output.strip()

        output = self.capture_stdout(f"BaseModel.show({obj_id})")
        self.assertTrue(len(output) > 0)

        output = self.capture_stdout(f"BaseModel.destroy({obj_id})")
        self.assertEqual(output, "")

        output = self.capture_stdout(f"BaseModel.update({obj_id}, name, 'New Name')")
        self.assertEqual(output, "")

        output = self.capture_stdout(f"BaseModel.update({obj_id}, {'name': 'New Name'})")
        self.assertEqual(output, "")

    def test_custom_commands_invalid_syntax(self):
        """Test the custom commands with invalid syntax."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: BaseModel.show()\n")

            self.console.onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: BaseModel.destroy()\n")

            self.console.onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: BaseModel.update()\n")

            self.console.onecmd("BaseModel.update(1234)")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: BaseModel.update(1234)\n")

            self.console.onecmd("BaseModel.update(1234, {'name': 'New Name'}, invalid)")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: BaseModel.update(1234, {'name': 'New Name'}, invalid)\n")

    def test_custom_commands_invalid_instance(self):
        """Test the custom commands with invalid instance."""
        output = self.capture_stdout("BaseModel.destroy(1234)")
        self.assertEqual(output, "** no instance found **\n")

        output = self.capture_stdout("BaseModel.update(1234, name, 'New Name')")
        self.assertEqual(output, "** no instance found **\n")

        output = self.capture_stdout("BaseModel.update(1234, {'name': 'New Name'})")
        self.assertEqual(output, "** no instance found **\n")


if __name__ == '__main__':
    unittest.main()
