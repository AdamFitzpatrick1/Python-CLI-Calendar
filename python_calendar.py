from datetime import date
import os
import sys
import calendar


width = os.get_terminal_size().columns
def newDate():
    print("Please enter a new date")
    
print()
print("-------------------------------".center(width))
print("Welcome to the calendar program".center(width))
print("-------------------------------".center(width))
todayDate = date.today()
print("Today's date is:", todayDate)
print()

c = calendar.TextCalendar(calendar.FRIDAY)
display = c.formatmonth(2019,11)
print(display)


print()
print("Please select an option from the list below:")
print()
print("1. Add an event to the calendar")
print("2. Remove an existing event")
print("3. Assign a note to a date within the calendar")
print("4. Exit the program")

print()
user = int(input("Select an option "))



if user == 1:

    newDate = input("Please enter a new date ")
    print()
    Date = newDate
    print("Your newly entered date is: ", Date)
    print()

if user == 2:
    Delete = input("Would you like to delete the stored date? ")
    if Delete == "Yes" or "yes":
        Date = None
        print()
        print("The date is now", Date)
    
if user == 3:
    Note = input("Please enter a note to add to your selected date")
    print("Your note is", Note, "The Date Is: ", Date)


if user == 4:
    sys.exit()



