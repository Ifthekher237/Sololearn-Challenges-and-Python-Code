"""
                                    Gapful Numbers
                                =====================
A gapful number is a number of at least 3 digits that is divisible by the number formed by the first and
last digit of the original number.

For Example:
input: 192
Output: true ( 192 is gapful because it is divisible by 12)

Input: 583
Output: true (583 is gapful because it is divisible by 53)

Input: 210
Output: false (210 is not gapful because it is not divisible by 20)

Write a program to check it the user input is a gapful number or not
"""


number = int(input())
assert (number > 99), "please enter a 3 digits positive number"


def gapful_number(number):
    """this function checks whether a number is gapful or not"""
    if int(number) % int(number[0] + number[-1]) == 0:
        return True
    else:
        return False


# prints whether the entered number is gapful or not
if gapful_number(str(number)):
    print("{} is a gapful number".format(number))
else:
    print("{} is not gapful number".format(number))


# prints all gapful number between 100 and user's number
print("All gapful numbers between 100 and {} are: ".format(number))

# list comprehension      
print([i for i in range(100, number) if gapful_number(str(i))])