#!/usr/bin/python3

"""The Driver Code that Launches the Console"""

# Coding Starts here, alright
import cmd
import sys
import datetime

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creating an instance of the BaseModel class"""

        args = line.split()
        if not args:
            print("** class name missing **")
            return

        classname = args[0]
        if classname not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{classname}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance b
        ased on class name and id."""

        from models import storage

        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        objects = storage.all()

        thekey = f"{class_name}.{instance_id}"

        if thekey not in objects.keys():
            print("** no instance found **")
            return

        for key, value in objects.items():
            if key == thekey:
                print(value)
                break

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""

        from models import storage

        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        objects = storage.all()
        key_check = f"{class_name}.{instance_id}"

        if key_check not in objects:
            print("** no instance found **")
            return

        # The dictionary returned by storage.all are still linked by reference
        # So modifying the objects on the new variable still affects the
        # original
        # Creating a new object with object-comprehension breaks that link to
        # the storage.__objects

        # Note: Doing storage.__objects for a private class attribute
        # outside the Class, you'll end up getting something like
        # storage.HBNBCommand__objects/ This is name mangling that
        # prevents accessing a private attribute from
        # outside a class
        

        del objects[key_check]

        storage.save()
        # storage.reload()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the
        class name. The printed result must be a list of strings.
        If the class name doesn’t exist, print ** class doesn't exist
        ** (ex: $ all MyModel)
        """
        from models import storage

        args = line.split()

        if args and args[0] not in ["BaseModel", "User", "State",
                                    "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        if args:
            classname = args[0]
            filtered_objects = {k: v for k, v in objects.items()
                                if k.startswith(classname)}
            instances = filtered_objects.values()
        else:
            instances = objects.values()

        string_representations = [str(instance) for instance in instances]
        print(string_representations)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute."""

        from models import storage

        args = line.split()

        # TO DO
        # We need to find a way to split string so that values in double
        # quotes are not split
        # How do we cast values to appropriate type?
        # Do we combine try except and them int() and float()?

        # Check if Class name not provided in argument i.e update
        if not args or len(args) < 1:
            print("** class name missing **")
            return

        # Check if Classname provided doesn't exist i.e not BaseModel
        if args and args[0] not in ["BaseModel", "User", "State", "City",
                                    "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        # Check if instance id is not provided as argument
        if len(args) < 2:
            print("** instance id missing **")
            return

        # Ensure there's key value pair on the arguments
        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        classname = args[0]
        instance_id = args[1]
        attrname = args[2]
        attrvalue = args[3]

        retrieved_objects = storage.all()

        thiskey = f"{classname}.{instance_id}"

        # Check if the key exits
        if thiskey not in retrieved_objects:
            print("** no instance found **")
            return
        else:

            # These objects are already pointing to the original
            # objects in the storage.all()
            # So no need to reassign the object of those objects
            # to storage.__objects
            # Just set the key and save + reload
            foundkeyobj = retrieved_objects[thiskey]
            setattr(foundkeyobj, attrname, attrvalue)

        storage.save()
        # storage.reload()
        
    # supports empty lines or Enter key
    def emptyline(self):
        """emty line or enter pressed"""
        return
    
    # quit command to wuit the program
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    # quit the program due to interuppts
    def do_EOF(self, line):
        """end of file marker is here"""
        return True

    # if sys.stdin.isatty():
    #     HBNBCommand().cmdloop()
    # else:
    #     interpreter = HBNBCommand()
    #     for line in sys.stdin:
    #         command = line.strip()  # Remove any trailing newline characters
    #         interpreter.onecmd(command)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
