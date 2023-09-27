import random
list = []
for i in range(10):
	list.append(random.randint(-10,10))


print("The randomly generated list : \n\t\t  {}".format(list))

for i in range(len(list)):
	min = list[i]
	
	for j in range(i, len(list)):
		if list[j] <= min:
			min = list[j]
			index = j
			
    # exchanging between the value that         we have assumed to be minimum and        the value that is actually minimim.
	temp = list[i]
	list[i] = list[index]
	list[index] = temp
	
print("\nThe sorted list (in ascending order) :   \n\t\t{}".format(list))

