### please enter a string 


"""
           Prime Strings
                                              ====================
A String is called prime if it can't be constructed by concatenating multiple (more than one) equal strings.

For example:
'abac' is prime, but 'xyxy' is not ('xyxy' = 'xy' + 'xy').

Implement a program which outputs whether a given string is prime.

Example:
    Input: 'xyxy'
    Output: 'not prime'

    Input: 'aaaa'
    Output: 'not prime'

    Input: 'hello'
    output: 'prime'
"""
string = input()

# checking if the string length is valid (or, greater than 1)
assert (len(string) > 1), "String length should be greater than 1"

# the flag variable will be False, if the string is once proved as 'not prime'

flag = True
a = ""
for char in string[:len(string)-1]:
    a += char
    n = string.count(a)
    
    if string == a*n:
        flag = False
        print('not prime')
        break

if flag:
    print('prime')