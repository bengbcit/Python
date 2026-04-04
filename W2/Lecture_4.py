# this course is about libraries, so we will be using a lot of libraries in this course.
def main():

    user_select = input('''Enter a number to select a function: \n
                        1.  import random functions\n
                        2. Sys Exit\n
                        3. Sys Exit with for loop\n
                        4. Packages and Modules\n
                        5. APIs\n
                        6. Importing my_functions\n
                        ''')

    match user_select:
        case '1':
            random_fn()
        case '2':
            sys_exit()
        case '3':
            sys_exit_for_loop()
        case '4':
            packages_fn()
        case '5':
            APIs_fn()
        case '6':
            import_my_functions()
        case _:
            print("Invalid input. Please enter a number between 1 and 6.")


def random_fn():
    ''' 
    #1 import random: downsides: 
    # we have to import the library every time we want to use it,
    # and we have to remember the name of the library and the functions we want to use.

    #2 from random import choice: 
    # we only import the function we want to use, 
    # but we still have to remember the name of the library and the function.

    #3 from random import *: 
    # we import all the functions from the library, 
    # but we still have to remember the name of the library and the function.

    #4 import random as r: 
    # we import the library and give it a shorter name,
    # but we still have to remember the name of the library and the function.
    '''
    import random
    print(random.choice(["heads", "tails"]))


def sys_exit():
    # sys.argv is a list of TERMINAL or COMMAND LINE arguments passed to the script.
    # The first argument is the name of the script, and the rest are the arguments passed to the script.
    import sys

    input_str = input("Enter a name: ").split()
    mock_argv = ["Lecture_4.py"] + input_str
    sys.argv = mock_argv

    if len(sys.argv) < 2:
        # way 1: to exit the if else statement:
        print(
            "Too few Arguments. "
            "Usage: python Lecture_4.py <name>"
        )
        sys.exit(1)
    elif len(sys.argv) > 2:
        # way 2: to exit the if else statement:
        sys.exit(
            "Too many Arguments. "
            "Usage: python Lecture_4.py <name>"
        )

    # sys.argv[0] is the name of the script, sys.argv[1] is the first argument, and so on.
    print(f"Hello, {sys.argv[1]}!")


def sys_exit_for_loop():
    import sys

    input_str = input("Enter a name: ")
    mock_argv = ["Lecture_4.py"] + input_str.split()
    sys.argv = mock_argv

    if len(sys.argv) < 2:
        # way 1: to exit the if else statement:
        print(
            "Too few Arguments. "
            "Usage: python Lecture_4.py <name>"
        )
    for name in sys.argv[1:]:
        print(f"Hello, {name}!")

def packages_fn():
    '''
    # 1. pip install package_name(cowsay): to install a package from the command line.
    # 2. import package_name: to import the package in the script.
    # 3. from package_name import function_name: to import a specific function from the package.
    # 4. from package_name import *: to import all functions from the package.
    # 5. import package_name as alias: to import the package and give it an alias.
    '''
    cowsay = __import__("cowsay")
    input_figure = input("Enter a figure (cow, dragon, ghost, etc.): ")
    if hasattr(cowsay, input_figure):
        figure_fn = getattr(cowsay, input_figure)
        figure_fn("Hello, World!")
    
def APIs_fn():
    '''
    # 1. API stands for Application Programming Interface, 
    #    which is a set of rules and protocols for building and interacting with software applications.
    # 2. APIs allow different software applications to communicate with each other, 
    #    and they can be used to access data and functionality from other applications.
    # 3. APIs can be accessed through HTTP requests, 
    #    and they can return data in various formats such as JSON, XML, etc.
    # 4. To use an API, you typically need to sign up for an API key, 
    #    which is a unique identifier that allows you to access the API.
    '''
    import requests
    import sys
    import json
    
    # turn str to a list of str, and then 
    # mock the sys.argv to be the same as if we run the script from the command line with arguments.
    input_str = input("Enter a name: ").split()
    mock_argv = ["Lecture_4.py"] + input_str
    sys.argv = mock_argv
    
    # if user does not provide the things, exit the program
    if len(sys.argv)!=2:
        sys.exit()

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
    # print(response.json())
    # print(json.dumps(response.json(), indent=2))
    
    o = response.json()
    for result in o["results"]:
        print(result["trackName"])
        
def import_my_functions():
    import sys
    
    input_str = input("Enter a name: ").split()
    mock_argv = ["Lecture_4.py"] + input_str
    sys.argv = mock_argv
    
    from my_functions import hello 

    if len(sys.argv) == 2:
        hello(sys.argv[1])

main()
