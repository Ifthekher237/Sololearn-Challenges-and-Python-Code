"""
                     Cube Root
            ================
A cube root of a number x is a number y such that y*y*y = x.
Example: 2 * 2 * 2 = 8, so the cube root of 8 is 2.

Write a code to find the cube root of a number N to a precision of 0.0001 without using any standard functions.

For example:
Input: 729
Output: 9

Input: 41
Output: 3.4482

Input: 2
Output: 1.2599
"""

# i have used Newton's method to evaluate cubic root of a number
# https://en.wikipedia.org/wiki/Newton%27s_method

#please input a value to find cubic root
value = float(input())
tolerance = 0.0001


def f(x):
    return (x**3) - value


def g(x):
    """derivative of f(x)"""
    return 3*(x**2)

# defining initial value
p = value

# if the difference between Xi+1 and Xi is less or equal to tolerance, then the flag will be True otherwise False
flag = False

while not flag:
    # Newton's method's formula
    q = p - (f(p)/g(p))

    if value > 0 and (p - q) <= tolerance:
        print("cubic root of {} is {:7.6f}".format(value, q))
        flag = True

    elif value < 0 and (q - p) <= tolerance:
        print("cubic root of {} is {:7.6f}".format(value, q))
        flag = True

    else:
        p = q
        flag = False