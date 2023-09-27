
title="\n               WORD COUNTER"
for alphabet in title:
    print(alphabet,end=" ")


def count_word(name_new):
    count = 1                     # "i am a lazy person" in this word, there are 4 spaces and 5 words. That's why count starts from 1.
    for character in name_new:
        if character == " ":
            count = count + 1
    print(count)

def user_feedback(ask_user):
    if ask_user == "yes":
        print("\nUsage::")
        print("        1.If you use space both side of a punctuation mark, then the punctuation mark")
        print("          will be counted as a word. Use space on any one side of the")
        print("          punctuation mark to avoid this situation.")
        print("        2.If you don't use space on any one side of punctuation mark at all, then you may")
        print("          get wrong answer.")
        print("Example::")
        print('         "ABC , abc" (WRONG WAY)')
        print('         "ABC,abc"   (WRONG WAY)')
        print('         "ABC, abc"  (RIGHT WAY)\n\n')
        name=input("Write a paragraph to count total number of word in that paragraph.\n")
        name_new=name.strip()      #after taking input from users, first of all it removes spaces (if present) from before the very first word and after the very last word
        count_word(name_new)       #count_word() function counts how many words are in the given paragraph. I need to call the count_word() function from both if block and else block because
    else:                                   #if user responds with "yes", then after showing the usages part i have to again ask user for giving the input. If user responds with "no", then directly else block will be executed.
        name = input("Write a paragraph to count total number of word in that paragraph.\n")
        name_new = name.strip()
        count_word(name_new)

ask_user=((input("\n\nDo you like to know how to use this script in a proper way?(yes/no):")).lower()).strip()     #take opinion from user and convert that string into all lowercase alphabet string and then remove space(if present) from both side of the string
user_feedback(ask_user)             #call user_feedback() function to show usages or to take input from user based on users opinion.

print("\n                                                      author of this script ==> <ifthekher.du@gmail.com>")