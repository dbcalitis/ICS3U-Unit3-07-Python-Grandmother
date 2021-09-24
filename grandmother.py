#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program is the grandmother's blessing giver program


def main():
    # This function checks if the user is rich or handsome
    is_rich = input("Are you rich?: ").lower()
    is_handsome = input("Are you good looking?: ").lower()

    if is_rich == "yes" and is_handsome == "yes":
        print("You can absolutely date my grandchild!")
    elif is_rich == "yes":
        print("You can date my grandchild with your riches!")
    elif is_handsome == "yes":
        print("You and my grandchild can make a beautiful pair!")
    elif is_rich == "no" and is_handsome == "no":
        print("Then, you can not date my grandchild!")
    else:
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
