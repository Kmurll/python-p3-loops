#!/usr/bin/env python3

#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter=10
    while counter >= 1:
        print(counter)
        counter -= 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_list = [num ** 2 for num in int_list]
    return squared_list


def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
def reverseString(str):
    reversedStr=""
    for char in str:
        reversedStr=char + reversedStr
    return reversedStr
