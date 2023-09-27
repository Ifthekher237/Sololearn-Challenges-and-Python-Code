"""
                                    Strange Root
                                ====================
A number has a strange root if its sqare and square root share any digit. For example, 2 has a strange root because the
square root of 2 equals 1.414 (consider the first three digits after the dot) and it contains 4 (which is
the square of 2)

Examples:
    Input: 24
    Output: false
    (the square root of 24 (4.889) and square (576) do not share any digits)

    Input: 11
    Output: true
    (the square root of 11 is 3.317, the square of 11 is 121. They share the same digit.)
"""


class Strange_root:
    def __init__(self, n):
        self.n = n
        self.__isStrangRoot(self.n)

    def __isStrangRoot(self, p):
        # first of all finding square and square root of the number then converting the number into string
        squarestring = str(p**2)
        squareRoot = str("{:.3f}".format(p**(1 / 2)))

        # printing the root and square of the number
        print("{}^2 = {}".format(p, squarestring))
        print("√{} = {}".format(p, squareRoot))

        common_digit = set()
        # now checking if any digit is shared by both square and square root
        flag = False
        for digit in squarestring:
            if digit == ".":
                continue
            if digit in squareRoot:
                flag = True
                common_digit.add(digit)

        # finally printing whether the number has strange root or not
        if flag:
            print("{} has a strange Root.\nThe square and square root have {} in common".format(p, common_digit))
        else:
            print("{} has not a strange root".format(p))

number = float(input())
Strange_root(number)