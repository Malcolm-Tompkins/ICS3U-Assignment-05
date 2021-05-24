#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 24, 2021
# Reverses user input numbers


def main():
    # Input
    user_input = (input("Enter you number to be reversed: "))

    try:
        user_number = int(user_input)
        reversed_number = 0
        while user_number > 0:
            remainder = user_number % 10
            reversed_number = (reversed_number * 10) + remainder
            user_number = user_number // 10
        print("The reverse of {0} is: {1}".format(user_input, reversed_number))
    except Exception:
        print("{} is not a positive integer".format(user_input))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
