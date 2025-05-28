# Write a Python code for checking if a year is a leap year.

wrongInput = True

#try and except better for non integer input
#Handle negative input problem
while wrongInput == True:
    year = int(input("Please enter a year to check: "))
    
    if year > 0:
        wrongInput = False
    
    else:
        print("\nInvalid year input, try again\n")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year", year, "is a leap year.")
        
        else:
            print("The year", year, "is not a leap year.")
            
    else:
        print("The year", year, "is a leap year.")

else:
    print("The year", year, "is not a leap year.")
