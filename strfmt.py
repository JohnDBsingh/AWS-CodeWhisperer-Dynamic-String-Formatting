#// python string formatting to accept user first name and last name and print it in a single line using string formatting

import sys

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))

def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    print_full_name(first_name, last_name)

if __name__ == "__main__":
    main()







