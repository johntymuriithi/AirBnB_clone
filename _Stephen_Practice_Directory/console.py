#!/usr/bin/python3

"""The Driver Code that Luanches the Console"""

# Coding Starts here 
import cmd
from baseModels import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb)"

    def do_create(self, line):
        """Creating an instance of the BaseModel class"""
        print(self)
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        className = args[0]
        if className not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{className}()")
        new_instance.save()
        print(new_instance.id)

    def emtyline(self):
        """emty line or enter pressed"""
        return

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


    def do_EOF(self, line):
        """end of file marker is here"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
