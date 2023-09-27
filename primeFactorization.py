def primeFactorization(number):
	for divisor in range(2, number + 1):
		if number % divisor == 0:
			number = number / divisor
			break
	if number == 1:
		return str(divisor)
	else:
		getPrime = primeFactorization(int(number))
		return getPrime + "*" + str(divisor)

number = int(input("please enter a number: "))	
primeNumbers = primeFactorization(number)
print("{number} = {prime}.".format(number = number, prime = primeNumbers))
list_of_prime = primeNumbers.split("*")
print(list_of_prime)
	
