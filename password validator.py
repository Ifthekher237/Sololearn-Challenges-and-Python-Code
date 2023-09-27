def checkSC(passwd):
    """this function checks whether the password contains any special character. if a character is neither an alphabet nor a number nor a spce, then the character will be assumed as a special character"""
    for chars in passwd:
        if chars.isalpha() == False and chars.isnumeric() == False and not chars == " ":
            return True
    return False
	

def passwdValidator(passwd):
    checkLength = 5 <= len(passwd) <= 10
    is_contain_number = passwd.isalpha() 
	# should be False, it returns True when the string is completely consisted of alphabet.
    space = " " in passwd # the valid password should not contains any space
    specialCharacter = checkSC(passwd)
    if checkLength == True and is_contain_number == False and space == False and specialCharacter == True :
        print("\nyour password is valid")
    else:
        print("\nyour password is invalid")
        print("\n\nA valid password is the one that confirms to the following rules:\n-minumum length is 5;\n-maximum length is 10;\n-should contain at least one number;\n-should contain at least one special character(such as &, #, @, *, % etc);\n-should not contain spaces")
		


passwdValidator(input())
