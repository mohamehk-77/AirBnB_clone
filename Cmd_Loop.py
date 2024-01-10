#!/usr/bin/python3
# that code to make uniq commands using python cmd
# as we can see we have two commands in that file: Hello & EOF
# after executing that file we expect from user to  enter the command
# we can see the word cmd if you pressed enter it will be printed again
# it is a loop waiting for a command like simple_shell
import cmd
import string
import sys


class Hello_world(cmd.Cmd):
    use_rawinput = False
    identchars = string.ascii_letters + string.digits + "_-"
    ruler = "#"
    doc_header = "Documented commands (type help <command>):"
    undoc_header = "Commands without help:"
    misc_header = "Miscellaneous help topics:"
    intro = "Welcome to the Pro\n"
    prompt = "$ "

    # if the user input "?" or help that will print that is customer help!
    def do_help(self, arg):
        # check if arg is greet
        if arg == "greet":
            # calling the helper function for greet
            self.help_greet()
        # if there is no match it just print that
        else:
            # it will show every thing in help
            super().do_help(arg)

    # if the user input "!" or shell it will print that is shell command
    def do_shell(self, arg):
        print("That Is A Shell Command")

    # After Executing a command it will print Command Executed!
    def postcmd(self, stop, line):
        print("Command Executed!")
        return stop

    # function to print hello with !
    def do_greet(self, line):
        if not line:
            line = input("please input ur username ")
        if line.startswith("-"):
            print("u used -greet command")
        print("Hello, " + line + "!")

    # incase the user wanted help for greet command he can use the help function
    def help_greet(self):
        print("Usage: greet [name]\nSay hello to [name]")

    # function to complete commands
    def complete_greet(self, text, line, begidx, endidx):
        names = ["Alice", "Bob", "Charlie"]
        if text:
            return [name for name in names if name.startswith(text)]
        else:
            return names

    # if you typed hello as command it will print Hello_World!
    def do_hello(self, line):
        if line:
            print("Hello", line)
        print("Hello_World!")

    # To Handel Error Message
    def default(self, line):
        print("{} is not recognized as a command try again".format(line))

    # wait for user to input his user_name
    def do_user_input(self, line):
        user_name = input("what 's your user_name? ")
        print("Hello, {}".format(user_name))

    # every time the loop will work it wil print a welcome message
    def preloop(self):
        print("Welcome To My_World")

    # if u pressed enter without entering a command it will print no command to repeat
    def emptyline(self):
        if self.lastcmd:
            print("repeating last command {}".format(self.lastcmd))
            self.onecmd(self.lastcmd)
        else:
            print("No Command To Repeat")

    # if user input valid command it will print the command he entered
    def precmd(self, line):
        print("you have entered: {}".format(line))
        return line

    def postcmd(self, stop, line):
        print("The Command Executed Successfully")
        return stop

    # to start the program with greeting without typing commands
    # def __init__(self):
    #     super().__init__()
    #     self.cmdqueue = ["greet John", "greet Jane"]

    # def do_sreet(self, line):
    #     print(f"Hello, {line}!")

    def precmd(self, line):
        if line == "quite":
            print("goodbye!")
            sys.exit()
        return line

    def do_help_misc(self, line):
        print("This is a miscellaneous help topic.")

    # if you typed EOF or ctrl + d it will exit
    def do_EOF(self, arg):
        return True


if __name__ == "__main__":
    Hello_world().cmdloop()
