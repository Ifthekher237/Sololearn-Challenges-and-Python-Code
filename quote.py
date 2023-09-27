# this program prints a quote randomly.

# flowchart is at the bottom of the page.

import random


def cut_half_and_print(list, n):
    """this function adds first half elements of received list and then prints the line """
    the_quote = []
    if len(list) != 4 and len(list) != 3 and len(list) != 2 and len(list) != 1:
        if len(list) % 2 == 0:
            end_point = int(len(list) / 2)

            for i in range(end_point):
                the_quote.append(list[i])

            print("{:^{}s}".format(" ".join(the_quote), n))

            del list[:end_point]
            cut_half_and_print(list, n)

        else:
            end_point = int((len(list) + 1) / 2)

            for i in range(end_point):
                the_quote.append(list[i])

            print("{:^{}s}".format(" ".join(the_quote), n))

            del list[:end_point]
            cut_half_and_print(list, n)

    else:

        if len(list) == 4:
            # print(1, list)
            for i in range(len(list) - 1):
                the_quote.append(list[i])

            print("{:^{}s}".format(" ".join(the_quote), n))

            del list[0:3]

            print("{:^{}s}".format(list[0], n))

        elif len(list) == 3:
            # print(2, list)

            for i in range(len(list) - 1):
                the_quote.append(list[i])

            print("{:^{}s}".format(" ".join(the_quote), n))

            del list[0:2]

            print("{:^{}s}".format(list[0], n))

        else:
            # print(3, list)

            for ele in list:
                the_quote.append(ele)

            print("{:^{}s}".format(" ".join(the_quote), n))


quote_dictionary = {
    1: "DONT'T TAKE REST AFTER YOUR FIRST VICTORY BECAUSE IF YOU FAIL IN SECOND, MORE LIPS ARE WAITING TO SAY THAT"
       " YOUR FIRST VICTORY WAS JUST LUCK.",
    2: "ONE DAY, THE PEOPLE THAT DIDN'T BELIEVE IN YOU WILL TELL EVERYONE HOW THEY MET YOU.",
    3: "SOMETIMES A DELAY IN YOUR PLAN Is GOD'S PROTECTION.",
    4: "WHEN YOU FOCUS ON YOU,  YOU GROW. WHEN YOU FOCUS ON SHIT, SHIT GROWS.",
    5: "IF THEY STAND BEHIND YOU, PROTECT THEM. IF THEY STAND BESIDE YOU, RESPECT THEM. IF THEY STAND AGAINST YOU, "
       "DEFEAT THEM.",
    6: "DON'T BE TOO HONEST IN THIS WORLD. BECAUSE STRAIGHT TREES ARE ALWAYS CHOSEN FIRST FOR CUTTING.",
    7: "WHEN YOUR GOALS AND DREAMS ARE MORE IMPORTANT THAN YOUR DISTRACTIONS.. WELCOME TO THE 1% CLUB.",
    8: "5AM IS WHEN LEGENDS EITHER WAKING UP OR GOING TO SLEEP.",
    9: "WHEN YOU GO FOR SOMETHING DON'T COME BACK UNTIL YOU GET IT.",
    10: "IF YOU DON'T CONTROL YOUR MIND, YOUR MIND WILL CONTROL YOU."}

quote_no = random.randint(1, len(quote_dictionary))  # produce a random integer from 1 to length of the dictionary.
string = quote_dictionary[quote_no]  # assigning the quote to variable.
n = int(len(string) // 2)  # finding the half length of the quote which is later used as the
# total width of every line.
splitted_string = string.split(" ")  # splitting the quote and assigning each word into list.

print()
cut_half_and_print(splitted_string, n)  # calling the half() function which prints the half of sent list.
print()

"""
                                    =============================
                                               FLOWCHART
                                    =============================
1. take a quote.
2. find length of quote
3. if length is an even number then prints first length/2 elements 
   else prints first(length + 1)/2 elements
4. now delete these elements from the list and take rest of the elements and repeat 1, 2, 3
 untill length == 2 or length == 1.
"""
