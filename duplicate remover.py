list=["ifthekher","zidan","jobayed","ifthekher","touha","zidan"]
total_entry=len(list)
for member in list:
    while list.count(member) > 1:          # "if" also can be used instead of while.
        list.remove(member)


print(list)

'''
# this script will do the same work(remove duplicat) 
#but this time it will ask user which duplicate element he/she wants to remove(still in progress)
def  index_of_duplicate_member(list,entry):
    print(entry + " is found at index number:")
    for i in range(len(list)):
        if entry == list[i]:
            print(i)
    input("which one do you want to remove ?")



def detect_duplicate(list,entry):
    count=list.count(entry)
    if count > 1:
        index_of_duplicate_member(list,entry)



list=["ifthekher","zidan","jobayed","ifthekher","touha","zidan"]
total_entry=len(list)

for i in range(total_entry):
    entry=list[i]
    detect_duplicate(list,entry)

'''