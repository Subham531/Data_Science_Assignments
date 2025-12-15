# Exercise 1: Age Calculator
# This program calculates the user's age based on their birth date and convert it into 
# European format

# Task 1: Asks the user to input their birth date in mm/dd/yyyy format

# imports neccessary modules
from datetime import datetime


# a function that does the calculation
def calculate():
    try:
        
        # its asks for the input from the user about their birth date 
        birth_input = input("Enter your birth date in mm/dd/yyyy format: ")

# Task 2: Validates the input format and ensures it’s a valid date
        
        # converting the string input in date-time format
        birth_date = datetime.strptime(birth_input,"%m/%d/%Y")

        # taking the current time 
        today = datetime.today()

# Task 3: Calculates and displays their current age in years
        
        # calculating the age by subtracting the birth_date from today
        age = today.year - birth_date.year

        # Adjust age if birthday has not occurred yet this year
        if (today.month,today.day) < (birth_date.month,birth_date.day):
            age -=1
        
        # printing the current age
        print(f'Your are {age} years old') 

# Task 4: Converts and displays the birthdate in European format (dd/mm/yyyy)
        
        # Convert date to European format (dd/mm/yyyy) and printing the result
        european_format = birth_date.strftime("%d/%m/%Y")
        print(f'Your birth_date in european format: {european_format}')

# Task 5: Handles all possible errors gracefully with appropriate messages
    except ValueError:
        # Handle invalid date format or invalid dates
        print("Invalid input, please follow (mm/dd/yyyy) format ")

    except Exception:
        # Handle any unexpected errors
        print('An unexpected error occured.')


# Call the function
calculate()