#!/usr/bin/python3

"""The Driver Code that Luanches the Console"""

# Coding Starts here 
import cmd
import datetime

from baseModels import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb)"

    def do_create(self, line):
        """Creating an instance of the BaseModel class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        className = args[0]
        if className not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = globals()[className]()
        print(new_instance)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on class name and id."""
        from __init__ import storage
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        objects = storage.all()
        print(objects)
        thekey = f"{class_name}.{instance_id}"
        if thekey not in objects:
            print("** no instance found **")
            return
        for key, value in objects.items():
            if key == thekey:
                valuee = str(value)
                print(f'{valuee}')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        from __init__ import storage
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        objects = storage.all()
        key = f"{class_name}.{instance_id}"

        if key not in objects:
            print("** no instance found **")
            return

        new_object = {key: value for key, value in objects.items() if key != instance_id}
        storage.__objects = new_object
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        The printed result must be a list of strings.
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        """
        from __init__ import storage
        args = line.split()

        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        if args:
            classname = args[0]
            filtered_objects = {k: v for k, v in objects.items() if k.startswith(classname)}
            instances = filtered_objects.values()
        else:
            instances = objects.values()

        string_representations = [str(instance) for instance in instances]
        print(string_representations)

        def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        from __init__ import storage

        args = line.split()

        # classname = args[0]
        # instance_id = args[1]
        attrname = args[0]
        attrvalue = args[1]

        objects = storage.all()
        thiskey = "BaseModel.1f087f50-05fe-4cf8-81ac-0c2e598c0d2b"
        #
        # if thiskey not in objects:
        #     print("** No instance found **")
        #     return

        result_dict = {key: value.to_dict() for key, value in objects.items()}
        print(result_dict)
        for key, value in result_dict.items():
            if key == thiskey:
                value[str(attrname)] = str(attrvalue)
                print(value)

        storage.__objects = result_dict
        storage.reload()

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
