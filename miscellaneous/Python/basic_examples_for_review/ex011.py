'''
Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into larger
number in a user-friendly format.
'''

number_over = int(input("Enter a number over 100: "))

while number_under <= 0:
  number_under = int(input("Enter a number under 10: "))
  
  if number_under == 0:
    print("Cannot divide by zero. Try again!")
  else:
    times = number_over/number_under
    print(f"{number_under} goes around {times:.2f} times inside {number_over}!")
