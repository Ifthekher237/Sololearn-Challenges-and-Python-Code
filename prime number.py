
def is_prime(count,n):
    if count ==1:
        print(n)


#no_of_divisor() functio finds the total number of divisor of "number"
# and send the total number of divisor to an another function is_prime() to determine whether the given number is prime or not.
def no_of_divisor(n):
    count=0
    i=0
    while i<=pow(n,.5):
        i = i + 1
        if n%i==0:
            count=count+1                #counts the total number of divisor
    is_prime(count,n)



number=int(input("Enter a number to check whether it is a prime or not:"))       #takes input from user and convert it to an integer

k=0                                                                              #initializing the while loop variable

while k<=number:

 if k==2:                                                                         #why i am printing 2 manually here without passing it to the function,the reason is
    print(2)                                                                      #given to the following table
 elif k==0 or k==1:
    k = k + 1                                                          #if "continue" is executed then the control returns to the begining of the while loop. The continue statement
    continue                                                           #rejects all  the remaining statements in the current iteration of the loop and moves the control back to the top of the loop
 else:                                                                 #that's why i had to add k=k+1 extra
    no_of_divisor(k)                                                               #calls the no_of_divisor() function
 k = k + 1

'''
if a number is "n", then we have listed the number of divisor checking form 1 to sqrt(n)  
number        no of divisor
======        =============
2           2
3           1
4           2
5           1
6           3
7           1
10          2
20          4
21          2
22          2
23          1
24          4

As you see here, all prime numbers have 1 divisor and all composite number have more than 1.
But the exception is 2, it is a prime number but it has 2 divisor(why is this happening? check it manually)
 '''