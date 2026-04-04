def main():
    hello("world")
    gooodbye("world")
    
def hello(name):
    print("Hello, " + name + "!")

def gooodbye(name):
    print("Goodbye, " + name + "!")

if __name__ == "__main__":
    # shouldn't call the functions when we import this file as a module in another file, 
    # but should call the functions when we run this file as a script.
    main()