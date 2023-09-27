# enter a decimal value to convert it to binary.

import math

number = float(input())
assert (math.floor(number) == number), "Enter a Value Without Fraction!"
number = int(number)

# ======method 1=============
def binary(n):
	if n == 1:
		return str(1)
	else:
		rem = n % 2
		n = n // 2
		get = binary(n)
		return get + str(rem)


print("using method 1 ==> {}".format(binary(number)))
# ============================

# ========method 2=============
print("using method 2 ==> {}".format(bin(number)[2:])) # bin() is a built-in function
# =============================