import random
list = [random.randint(1, 20) for i in range(5)]

max = list[0]
for i in range(len(list)):
	if list[i] > max : max = list[i]
print(list)
print(max)

second = list[0]
i = 0
while i <= len(list):
	if second < max and list[i] > second:
		second = list[i]
	print(second)
	i += 1
		
print(second)