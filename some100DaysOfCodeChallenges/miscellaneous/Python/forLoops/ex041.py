"""
Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times.
"""

name = input("Enter your name: ")
n = 0

while n < 1:
    n = int(input("Now, please, enter a number: "))

if n < 10:
    print(f"{name} " * n)
else:
    print("Too high" * 3)
