#!/bin/usr/python3
"""
Unittests for console
"""
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test for console
    """
    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cli = None
        pass

    def test_create(self):
        # Test create cmd for BaseModel
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create BaseModel")
            result = output.getvalue().strip()
            self.assertTrue(result)

        # Test create cmd for User with params
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd('create User name="John Wick" age=37')
            result = output.getvalue().strip()
            self.assertTrue(result)

        # Test create command w/invalid class name
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create InvalidClass")
            result = output.getvalue().strip()
            self.assertEqual(result, "** class doesn't exist **")

        # Test create command w/invalid parameters
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create BaseModel invalid_param")
            result = output.getvalue().strip()
            self.assertEqual(result, "** attribute name missing **")

        # Test create command w/invalid value for an attribute
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create BaseModel name=JohnDoe age=thirty")
            result = output.getvalue().strip()
            self.assertEqual(result, "** Invalid integer value: thirty **")


if __name__ == "__main__":
    unittest.main()
