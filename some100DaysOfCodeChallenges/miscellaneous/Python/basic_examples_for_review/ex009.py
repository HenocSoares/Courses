'''
Write a program that will ask for a number of days and then will
show how many hours, minutes and seconds are in that number of days.
'''

num_of_days = int(input("Enter the number of days for calculation: "))

# Calculate hours, minutes, and seconds
hours = num_of_days * 24
minutes = hours * 60
seconds = minutes * 60

# Results
print(f"In {num_of_days} days, there are: ")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")
