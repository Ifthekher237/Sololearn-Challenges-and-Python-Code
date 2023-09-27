"""                                     Summations Calculator
                                    ===========================
Create a program that takes 3 inputs, a lower bound, an upper bound and the expression. Calculate the
sum of that range based on the given expression and output the result.

For Example:
Input: 2 4 *2
Output: 18 (2*2 + 3*2 + 4*2)

Input: 1 5 %2
Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)
"""


# Enter lower, upper bound and an expression separated by a space

x, y, expr = input().split(" ")

# check correct lower and upper bound
assert (int(x) < int(y)), "Lower bound should be lower than Upper bound"

string = ""
summations = 0
for i in range(int(x), int(y) + 1):
    string += str(i) + expr + " + "
    summations += eval(str(i) + expr)

print("{} = {}".format(string[-len(string): -2], summations))


# class Summations_calculator:
#     def __init__(self, x, y, expr):
#         self.x = x
#         self.y = y
#         self.expr = expr
#         self.__check_bound(self.x, self.y)
#         self.calculate_summation()
#
#     def __check_bound(self, a, b):
#         assert (int(a) < int(b)), "Lower bound should be lower than Upper bound"
#
#     def calculate_summation(self):
#         string = ""
#         summations = 0
#         for i in range(int(self.x), int(self.y) + 1):
#             string += str(i) + self.expr + " + "
#             summations += eval(str(i) + self.expr)
#
#         print("{} = {}".format(string[-len(string): -2], summations))
#
#
# # Enter lower, upper bound and an expression separated by a space
# x, y, expr = input().split(" ")
# Summations_calculator(int(x), int(y), expr)
