# -*- coding: utf-8 -*-
"""
    Santa is trying to deliver presents in a large apartment buildingself.
    He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
    An opening parenthesis ( means he should go up one floor and a closing parenthesis ) means he should go down one floor.
    The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
    For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.
    To what floor do the instructions take Santa?
    Input : https://adventofcode.com/2015/day/1/input
"""

if __name__ == "__main__":
    at_floor = 0
    floor_design =  input("Please provide floor design:")
    for floor in floor_design:
        if floor =="(":
            at_floor = at_floor + 1
        else:
            at_floor = at_floor - 1
    print ("Floor should be :", at_floor )
