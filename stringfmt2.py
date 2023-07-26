#//python code to accept user first name and last name from the user and print them using string formatting

import sys
#import stdio

def print_full_name(a, b):
    print("Hello " + a + " " + b + "! Welcome to Be10x program.")

    return

def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    print_full_name(first_name, last_name)
    return

if __name__ == "__main__":
    main()

