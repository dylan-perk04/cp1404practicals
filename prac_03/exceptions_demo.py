"""
CP1404 - Practical
Demos of exceptions.
"""

# 1. When will a ValueError occur?
# A value error will occur when the user enters a non-integer for the numerator/denominator, such as a string
#
# 2. When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur when the user tries to divide by 0 by entering 0 as the denominator
#
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, see fixed code below

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
