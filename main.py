# A simple program that prints a welcome message

def main():
    print("Welcome to the world of programming with Python!")
    a = "   Welcome to the world of programming with Python!     "
    print(a.strip())

    print(a.replace("Python", "Java"))
    

if __name__ == "__main__":
    main()