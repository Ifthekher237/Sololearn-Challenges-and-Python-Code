#this function says whether a string is palindrome or not.
def is_palindrome(string):
   string_new=""
   for alphabet in range(-1,-len(string)-1,-1):
    string_new=string_new+string[alphabet]
   if string==string_new:
    print(string)

#string=input("input a string:\n")
for year in range(2000,2100):
    for month in range(1,13):
        if month < 10:
            month= str(0)+str(month)
        for day in range(1,30):
            if day <10:
                day = str(0) + str(day)
            string= str(day)+str(month)+str(year)
            is_palindrome(string)