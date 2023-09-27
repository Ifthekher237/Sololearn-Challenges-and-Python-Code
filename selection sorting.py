# this program randomly creates a list of 10 elements and then sorts them in ascending order and finally prints the second largest number or whichever largest number you wants to print
import random

# this part of code randomly creats a list.
list = []
for i in range(10):
	list.append(random.randint(-10, 20))
	
print("The randomly created list is : \n {list}".format(list = list))
	
# this part of code sorts the list
for i in range(len(list)):
	min = list[i]
	for j in range(i, len(list)):
		if list[j] < min :
			min = list[j]
	for j in range(i, len(list)):
		if min == list[j] : take  = j
	temp = list[i]
	list[i] = list[take]
	list[take] = temp
	
print(list)

max = list[-1]
for i in range(-1, -len(list), -1):
	if list[i] == max:
		continue
	else:
		print("The second largest number from this list is {number}.".format(number = list[i]))
		break
