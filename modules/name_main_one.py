# Since there is no main() function in Python, when the command to run a
# python program is given to the interpreter, the code that is at level 0
# indentation is to be executed. However, before doing that, it will define a
# few special variables. __name__ is one such special variable. If the source
# file is executed as the main program, the interpreter sets the __name__
# variable to have a value “__main__”. If this file is being imported from
# another module, __name__ will be set to the module’s name.

# __name__ is a built-in variable which evaluates to the name of the current
# module.


def my_func():
    print("Function in Module One.")


print("Module one - Indentation Level 0")

if __name__ == "__main__":
    print("Module one is being called directly.")
else:
    print("Module one has been imported.")
