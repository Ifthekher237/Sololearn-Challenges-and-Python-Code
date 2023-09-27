number = int(input("please enter a number greater than zero to sum up all the digits: "))
temp = number
sum = 0
number_of_digits = 0
while number >= 10:
	sum = sum + number % 10
	number = number//10
	number_of_digits += 1
else:
	sum += number
	number_of_digits += 1
print("There are {} digits in the number {} and the sum of all digits is {}".format(number_of_digits, temp, sum))
	