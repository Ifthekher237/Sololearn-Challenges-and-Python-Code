class Pyramid:

    def upper(self, row):
        """prints a regular pyramid"""
        space = row
        j = 0
        while space >= 0:
            for i in range(space):
                print(" ", end="")

            for k in range(2 * j + 1):
                print("*", end="")
            print()
            space -= 1
            j += 1

    def lower(self, row):
        """prints a pyramid with upside down"""
        space = 0
        j = row
        while space <= row:
            for i in range(space):
                print(" ", end="")

            for k in range(2 * j + 1):
                print("*", end="")
            print()
            space += 1
            j -= 1

test = Pyramid() # declaring an instance of Pyramid() class
test.upper(4)  # calling a method of Pyramid() class
print()
test.lower(4) # calling another method of Pyramid() class.

print("\n\n If you have any suggestion regarding my code please let me know in the comment section. Thank You for viewing my code.")







