#this program demonstrates how to find the sum of divisors of a given number
#using while loop and function


def no_divisor_message(count,list):
    if count==0:
        print("No Divisor is found! Try a value other than 0.")
    else:
        print(list)




def find_divisor_and_sum(n):
  print("Positive Divisors of " + str(n) + " are:")
  sum=0
  i=0
  count=0
  list=[]
  if n>=0:          #if entered number is a positive number, then if block will be executed
    while n!=0 and i<=n:
        i = i + 1
        if n%i==0:
            #print(i)
            list.append(i)
            sum=sum+i
            count+=1
        else:
            continue
  else:             #if entered number is a negative number, then else bolck will be executed.
    while  i<= -n:
        i = i + 1
        if n%i==0:
            list.append(i)
            #print(i)
            sum=sum+i
            count+=1
        else:
            continue
  no_divisor_message(count,list)
  return sum







print("\n\tThis script finds the divisors of a given number\n\n")
number=int(input("\nPlease enter a number::"))
print("Sum of all positive divisors of " +str(number)+ " is: "+str(find_divisor_and_sum(number)))
