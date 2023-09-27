"""
            collatz conjecture
                                ==========================
the collatz conjecture (also known as the Ulam conjecture or the Syracuse problem) is an unsolved mathematical
problem, which is very easy to formulate.

1. Take any natural number
2. If it's even, half it, otherwise triple it and add one
3. Repeat step 2. Untill you reach 4, 2, 1 sequence
4. You will ALWAYS reach 1, eventually.

Example:

    x = 17

    17 * 3 + 1=51
    52 / 2 = 26
    26 / 2 = 13
    13 * 3 + 1 = 40
    40 / 2 = 20
    20 / 2 = 10
    10 / 2 = 5
    5 * 3 + 1 = 16
    16 / 2 = 8
    8 / 2 = 4
    4 / 2 = 2
    2 / 2 = 1
    .. .. ..

That last sequence: 4, 2, 1 is an infinitely repeating loop. The formulated conjecture is that for any x the sequence
will always reach 4, 2, 1 ultimately.

While the problem cannot be proved, the assignment is tor write a code that will produce and print
out the whole sequence for an input number.
"""


class Collatz_conjecture:
    
    def __init__(self, n):
        self.n = n

        assert (self.n > 0), "please enter a number greater than 0"

        self.count = 0 
        self.is_collatz_number(self.n, self.count)

    def is_collatz_number(self, num, counter):
        """this is the main part of the program. Here I've used recursion."""

        counter += 1
        if num == 1:
            print("{} took {} iterations to converge to 1".format(self.n, counter - 1))
            
        elif num % 2 == 0:
            print("{}/2 = {}".format(int(num), int(num/2)))
            self.is_collatz_number(num / 2, counter)
            
        else:
            print("{} * 3 + 1 = {}".format(int(num), int(num * 3 + 1)))
            self.is_collatz_number(num * 3 + 1, counter)


number = int(input("please enter a number: "))
Collatz_conjecture(number)



















