#!/usr/bin/python3

"""test file storage"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """test class"""

    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.console = None
        self.mock_stdout.close()

    def test_quit_command(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.assertTrue(self.console.onecmd('quit'))
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_help_command(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.assertFalse(self.console.onecmd('help'))
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("Undocumented commands:", output)

    def test_non_interactive_mode(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd('create BaseModel')
            self.console.onecmd('all BaseModel')
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)
        self.assertIn("created", output)


if __name__ == '__main__':
    unittest.main()
