def checkValidFormat(userFormat):
    if "name" in userFormat and "<name>" not in userFormat:
        return False
    if "year" in userFormat and "<year>" not in userFormat:
        return False
    if "rank" in userFormat and "<rank>" not in userFormat:
        return False
    if "name" not in userFormat and "year" not in userFormat and "rank" not in userFormat:
        return False
    return True


def printDatabase(format, data):
    new = format
    for movie_name, year, rank in database:
        new = format.replace("<name>", movie_name)
        new = new.replace("<year>", str(year))
        new = new.replace("<rank>", str(rank))
        print(new)


database = [("The Lord of the Rings", 2001, 8.7), ("Tootsie", 1829, 3.5), ("Aynabaji", 2016, 9.1), ("Dhaka Attack", 2017, 7.8)]
userFormat = input()
defaultFormat = '<rank>  <year>  <name>'
print()

if checkValidFormat(userFormat) == True:
    printDatabase(userFormat, database)
else:
    printDatabase(defaultFormat, database)
    print("\nyou have entered an invalid format.That's why information is printed"
          " in  default way (<rank>  <year>  <name>).To enter a valid"
          " format the variables name should be given within angle brackets.e.g. ***<name>***<rank>"
          "***<year>***")
