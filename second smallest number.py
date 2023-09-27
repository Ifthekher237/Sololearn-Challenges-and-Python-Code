list =[6, 0, 8, -5, 2]
for i in range(len(list)):
	min = list[i]
	for j in range(i, len(list)):
		if list[j] < min:
			min = list[j]
			