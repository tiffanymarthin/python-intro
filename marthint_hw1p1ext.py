"""
File Name: marthint_hw1p1ext.py
Name: Tiffany Marthin
Last Modified: 4/11/2020
Summary: Individual Programming 1 Part 1 Extension
Goal: Create a program that ask for two numbers from user and prompt the user
      to choose which mathematical functions the user wants to execute
"""

"""
Asking the user for 2 numbers which the user would like to compare, and then
prompt the user to select mathematical function to perform
"""
num1 = input('First value: ')
num2 = input('Second value: ')
func = eval(input('Choose between these following mathematical options:\n'
             '  1. Sum of the two values\n'
             '  2. Subtract value2 from value1\n'
             '  3. Compare if the two values are equal\n'
             '  4. Compare if the two values are unequal\n'
             'Please choose between number 1 to 4: '))

# Ensure that the user gives valid input, it'll give error message if input is invalid
validList = [1,2,3,4]
while func not in validList:
    func = eval(input('Invalid input. Please enter 1 to 4: '))

"""
Below are storing the 4 different calculations:
First calculation is to sum up the two values and then printing out the summation 
Second calculation is to find the difference between the two values and then printing out the subtraction
Third calculation is to evaluate whether the two values are equal to each other and then printing out the result (True/False)
Fourth calculation is to evaluate whether the two values are unequal to each other and then printing out the result (True/False)
"""

total = eval(num1) + eval(num2)
diff = eval(num1) - eval(num2)
equality = eval(num1) == eval(num2)
inequality = eval(num1) != eval(num2)

"""
Following if statements are to output the calculation that was selected by the user
"""
if func == 1:
    print(num1 + ' + ' + num2 + ' = ', total)
elif func == 2:
    print(num1 + ' - ' + num2 + ' = ', diff)
elif func == 3:
    print(num1 + ' = ' + num2 + ' ', equality)
elif func == 4:
    print(num1 + ' is not equal to ' + num2, inequality)
