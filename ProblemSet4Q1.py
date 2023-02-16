# Aryan Gidwani
# November 12, 2021
# ICS3UO - A
# This program is essentially a simple calculator! It can find the answers to
# different questions and calculations, involving operators such as addition,
# subtraction, multiplication, division, exponents, and modulus!

name = input("Hello! What is your name? ")
# asks the user for their name
print("Hello " + name + "! The purpose of this program is to do simple calculations using two user-inputted numbers! By choosing the operation and the numbers, the calculator will give an answer based on those numbers! Type in the letter that corresponds to the operation that you want to use.")
# introductory message
flag = True
# flag variable stores a boolean value of true

while flag:
    try:
        firstNumber = input("Type quit if you want to stop. Enter in your first number: ")
        # asks the user for the first number
        if firstNumber == "quit":
            break
            # stops the loop from running
            
        firstNumber = float(firstNumber)
        # allows the user to input values with decimal points
        print("a: addition " + "\n" + "b: subtraction" + "\n" + "c: multiplication" + "\n" + "d. division" + "\n" + "e. exponents" + "\n" + "f. modulus")
        # list of different operations that can be used
        chosenOperation = input("Type quit if you want to stop. Enter in the letter corresponding to the " + "\n" + "operation: ")
        # asks the user for what operation they want to use

        if chosenOperation == "quit":
            break
            # stops the loop from running

        elif chosenOperation == "a":
            secondNumber = float(input("Enter in your second number: "))
            # asks the user for the second number
            answer = firstNumber + secondNumber
            # adds the two numbers together
            print("Answer: " + str(answer) + "\n")
            # tells the user the answer
        
        elif chosenOperation == "b":
            secondNumber = float(input("Enter in your second number: "))
            # asks the user for the second number
            answer = firstNumber - secondNumber
            # subtracts the second number from the other
            print("Answer: " + str(answer) + "\n")
            # tells the user the answer

        elif chosenOperation == "c":
            secondNumber = float(input("Enter in your second number: "))
            # asks the user for the second number
            answer = firstNumber * secondNumber
            print("Answer: " + str(answer) + "\n")
            # tells the user the answer

        elif chosenOperation == "d":
            secondNumber = float(input("Enter in your second number: "))
            # asks the user for the second number
            answer = firstNumber / secondNumber
            print("Answer: " + str(answer) + "\n")
            # tells the user the answer

        elif chosenOperation == "e":
            secondNumber = float(input("Enter in your second number: "))
            # asks the user for the second number
            answer = firstNumber ** secondNumber
            print("Answer: " + str(answer) + "\n")
            # tells the user the answer

        elif chosenOperation == "f":
            secondNumber = float(input("Enter in your second number: "))
            # asks the user for the second number
            answer = firstNumber % secondNumber
            print("Answer: " + str(answer) + "\n")
            # tells the user the answer

        else :
            print("Please enter in one of the letters!" + "\n")
            # invalid input message

    except:
        print("You have inputted an invalid value!")
        # invalid input message

print("Thank you so much for using this program. Have a nice day!")
