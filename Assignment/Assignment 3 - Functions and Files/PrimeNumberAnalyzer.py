"""
Q2: Prime Number Analyzer
Let the user input a range of numbers. 
Use a function to check if a number is prime. 
Write all prime numbers in that range to a file, one per line.
"""
import os

def primeCheck(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


leftBoundary = int(input("Please enter your range start number: "))
rightBoundary = int(input("Please enter your range end number: "))

# make the file if exist empty and create it if not exist
open("primeNumbers.txt", "w")

for i in range (leftBoundary, rightBoundary + 1):
    if primeCheck(i) == True:
        with open("primeNumbers.txt", "a") as f:
            primeNumber = str(i) + "\n"

            f.write(primeNumber)

print("\nDone, check primeNumbers.txt to see the results\n")

