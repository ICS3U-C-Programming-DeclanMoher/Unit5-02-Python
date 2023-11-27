#!/usr/bin/env python3
# created Nov 24th 2023 by Declan Moher
def calc_area():
    # asking for base and height in cm
    base_str = input("Enter a base in (cm) ")
    height_str = input("Enter a height in (cm)")

    try:
        # try to cast to an integer
        base_float = int(base_str)
        height_float = int(height_str)
    except ValueError:
        # if input can't go to integer this will print
        print(f"{base_str} and or {height_str} is a invalid input")
    else:
        # calculate area
        area = base_float * height_float / 2
        print(f"{area} is the area of the triangle")


def main():
    # calling function
    calc_area()


if __name__ == "__main__":
    main()
