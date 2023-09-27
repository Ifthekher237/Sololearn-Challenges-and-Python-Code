def sameORdifferent(list):
	for ele in list:
		counts = list.count(ele)
		if counts == 2:
			return False
	return True

# ====take input & enter them into dicti==

print("Enter the info in this serial (number, colour, shading, shape) and keep a space between two info :")

set_of_card = {}
for i in range(3):
    print("description of card {}: ".format(i), end = " ")
    string = input()
    split_string = string.split(" ")
    set_of_card[i] = split_string
    print()
# ===============================

print(set_of_card)  
"""  
cardNo = 0
while cardNo < 3:
    for cardInfo in range(4):
        print(set_of_card[cardNo][cardInfo], end = " ")
    cardNo += 1
    print()
"""

# ===can they form a set============
for i in range(4):
	list = []
	for card in range(3):
		list.append(set_of_card[card][i])
		
	if sameORdifferent(list) == False:
		print("not a set")
		break
#================================