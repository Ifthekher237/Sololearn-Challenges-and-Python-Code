"""
                            Paranoia
                        ===============
ByteCorp is a famous technological company in Byteania.
The CEo of ByteCorp doesn't trust anyone and thinks that his accountant managed to move huge amounts of
money to a competitor company, MegaCorp.
He hires a computer crime investigator, and asks him to find inconsistencies in the money transfers.
Here is a sample transaction log of the company:

Feb SLR 4 M
Feb ENT 800 k
Mar SLR 4000 K
Mar ENT 800 k
Apr SLR 4010 k
apr ENT 810 k

There are four columns:
1. Month of the transaction
2. REason of the expense (SLR for "salary", ENT for "entertainment", OTR for "other")
3. Amount
4. M, K, or B (M for million, K for thousands, B for billion)

IN the example above, April expenses show an inconsistency and should be reported.

Another example:
Jul SLR  4 M
Jul ENR 800 K
Jul OTR 1200 K
Aug SLR  4000 K
Aug ENR 800 K
Aug OTR 1190 K
Sep SLR 4000 K
Sep ENR 800 K
Sep OTR 1190 K

Here, July expenses show an inconsistency and should be reported..

As the computer investigator, write a program, which reads the transaction logs, detects inconsistent expenses
and prints the exact month containing the "unusual" activities.
"""

for alpha in 'ByteCorp':
    print(alpha, end=" ")
print("\n=======================")


def find_inconsistency(cost_per_month):

    minimum_cost = min(cost_per_month.values())
    for month in cost_per_month:
        if cost_per_month[month] > minimum_cost:
            print("\n{} expenses show an inconsistency".format(month))


def total_cost_per_month(data):

    dicti = {}
    for month in data:
        if month[0] not in dicti:
            dicti[month[0]] = 0
            for amount in data:
                if amount[0] == month[0]:
                    dicti[month[0]] += int(amount[2])
    find_inconsistency(dicti)


def modify(information):
    """converting all amounts into thousands """
    modified_info = []

    for each_months_info in information:
        splitted_data = each_months_info.split(" ")

        if splitted_data[-1] == "M":
            splitted_data[-2] = str(int(splitted_data[2])*pow(10, 3))
            del splitted_data[-1]

        if splitted_data[-1] == "B":
            splitted_data[-2] = str(int(splitted_data[2]) * pow(10, 6))
            del splitted_data[-1]

        if splitted_data[-1] == "k":
            del splitted_data[-1]

        modified_info.append(splitted_data)

    total_cost_per_month(modified_info)

input1 = ["Feb SLR 4 M",
          "Feb ENT 800 k",
          "Mar SLR 4000 k",
          "Mar ENT 800 k",
          "Apr SLR 4010 k",
          "Apr ENT 810 k"]

input2 = ["Jul SLR 4 M",
          "Jul ENR 800 k",
          "Jul OTR 1200 k",
          "Aug SLR 4000 k",
          "Aug ENR 800 k",
          "Aug OTR 1190 k",
          "Sep SLR 4000 k",
          "Sep ENR 800 k",
          "Sep OTR 1190 k"]

modify(input1)
modify(input2)

"""
order of calling functions:
modify() ==> total_cost_per_month() ==> find_inconsistency()
"""
