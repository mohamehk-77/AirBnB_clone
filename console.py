#!/usr/bin/python3
import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


"""Define HBNB class"""
"""
HBNB Command Line Interface.
"""
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "place": Place,
    "Review": Review
    # Add other classes here
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    """ Help center"""
    def do_help(self, arg):
        super().do_help(arg)

    """Method to quit the program"""
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
        """Create New Instance\n"""
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in classes:
            print("** class doesn't exist **")
            return
        instance = classes[class_name]()
        instance.save()
        print(instance.id)

    """Shows the string representation of an instance."""
    def do_show(self, line):
        """Shows the string representation of an instance.\n"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            key = class_name + "." + instance_id
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    """Destroy Instance"""
    def do_destroy(self, line):
        """Destroy Instance.\n"""
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = arg[0], arg[1]
            key = class_name + "." + instance_id
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

    """
    Print all  all string representation of all
    instances based or not on the class name
    """
    def do_all(self, line):
        """
        Print all  all string representation of all
        instances based or not on the class name\n
        """
        arg = line.split()
        if len(arg) == 0:
            all_objs = models.storage.all()
            for obj_id, obj in all_objs.items():
                print(str(obj))
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            all_objs = models.storage.all()
            for obj_id, obj in all_objs.items():
                class_name = obj.__class__.__name__
                if class_name == arg[0]:
                    print(str(obj))

    """
    Updates an instance based on the class name
    and id by adding or updating attribute.
    """
    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute.\n
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            class_name = arg[0]
            instance_id = arg[1]
            attr_name = arg[2]
            attr_value = arg[3].strip('"')
            key = class_name + "." + instance_id
            all_objs = models.storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                inst = all_objs[key]
                if attr_name not in ("id", "create_at", "update_at"):
                    if hasattr(inst, attr_name):
                        attr_type = type(getattr(inst, attr_name))
                    else:
                        attr_type = str
                        setattr(inst, attr_name, attr_type(attr_value))
                        inst.save()

    """Exit from the program by pressing Ctrl+D."""
    def do_EOF(self, arg):
        print("\n", end="")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
