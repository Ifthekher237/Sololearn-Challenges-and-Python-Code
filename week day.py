# enter the date in  MM.DD.YY format.

# this program tries to determine the day of the week of a given date.

"""how this program is working:

    step:1 Take the last two digits of the year.
    step:2 Divide by 4, discarding any fraction.
    step:3 Add the day of the month.
    step:4 Add the month's key value: JFM AMJ JAS OND 144 025 036 146
    step:5 Subtract 1 for January or February of a leap year.
    step:6 For a Gregorian date, add 0 for 1900's, 6 for 2000's, 4 for 1700's, 2 for 1800's;
          for other years, add or subtract multiples of 400.
    OR, For a Julian date, add 1 for 1700's, and 1 for every additional century you go back.
    step:7 Add the last two digits of the year.
    step:8 Divide by 7 and take the remainder.

Now 1 is Sunday, the first day of the week, 2 is Monday, and so on.

the algorithm is taken from this website:: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html"""

import math


def isLeapYear(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False


def checkValidity(date):
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    thirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
    thirtyDays = [4, 6, 9, 11]
    if month <= 0 or month > 12 :
        return False
    if isLeapYear(year) == False and month == 2 and day > 28:
        return False
    if isLeapYear(year) == True and month == 2 and day > 29:
        return False
    if month in thirtyDays and day > 30:
        return False
    if month in thirtyOneDays and day > 31:
        return False
    return True


def get_key(monthsName):
    key = {1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}
    return key[monthsName]


def finalDay(remainder):
    week_day = {1: "sunday", 2: "monday", 3: "tuesday", 4: "wednesday", 5: "thursday", 6: "friday",
                0: "saturday"}
    return week_day[remainder]


def getCentury(year):
    year = str(year)
    century = year[:2] + "00"
    last2digits = year[2:]
    return int(century), int(last2digits)


def centuryCode(usersCentury):
    code = {1700: 4, 1800: 2, 1900: 0, 2000: 6}
    for century in code.keys():
        if (century - usersCentury) % 400 == 0:
            return code[century]


# =======take input part========
date = input("please enter the date in MM.DD.YY format ::").split(".")
if not checkValidity(date):
    print("\nSomething is incorrect. Check your entered day and month and check whether you have"
          " used correct format.(MM.DD.YY)")
# ===========================
else:

    # ====setting up variables=====
    year = int(date[2])
    monthsName = int(date[0])
    date_of_month = int(date[1])
    usersCentury, last_2_digits = getCentury(year)
    months_key = get_key(monthsName)
    # =============================

    # ======step 1, 2, 3, 4, 5======
    y = math.floor(last_2_digits / 4) + date_of_month + months_key

    if isLeapYear(year) == True and (monthsName == 1 or monthsName == 2):
        y = y - 1
    # ==========================

    # ========step 6=======
    getCenturyCode = centuryCode(usersCentury)
    y = y + getCenturyCode
    # =====================

    # ===step 7, 8=========
    y = y + last_2_digits
    remainder = y % 7
    print("\n{} ==> {}".format(".".join(date),finalDay(remainder)))
    # ======================
    print("\nTo get the exact result use MM.DD.YY format.")
