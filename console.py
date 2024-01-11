#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel

"""Define HBNB class"""
"""
HBNB Command Line Interface.
"""
classes = {
    "BaseModel": BaseModel
    # Add other classes here
}
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    """ Help center"""
    def do_help(self, arg):
        super().do_help(arg)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    """if the user typed quit as a command it will exit"""
    def precmd(self, line):
        if line == "quit":
            sys.exit()
        return line

    """ if user hit enter it executes no thing"""
    def emptyline(self):
        pass

    """Help The User"""
    def help_help(self):
        print("Type Help With The Name Of The Command\n")

    """Help EOF"""
    def help_EOF(self):
        print("Type EOF Or Ctrl + D As Command Will Exit\n")

    """Create New Instance"""
    def do_create(self, class_name):
        """Create New Instance"""
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in classes:
            print("** class doesn't exist **")
            return
        instance = classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Showing Class Id"""
        arg = line.split()
        if len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            key = arg[0] + "-" + arg[1]
            if key in classes:
                print(classes[key])
            else:
                print("** no instance found **")

    """Exit from the program by pressing Ctrl+D."""
    def do_EOF(self, arg):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
