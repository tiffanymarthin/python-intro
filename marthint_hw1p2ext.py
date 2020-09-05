"""
File Name: marthint_hw1p2ext.py
Name: Tiffany Marthin
Last Modified: 4/10/2020
Summary: Individual Programming 1 Part 2
Goal: Create a program that prompts user for a category of things and things to put
in the list. It will then perform various interactive questions and responses. This extension
will have additional prompts for the users to select how many items the user wants in the list.
It will also prompt if the user wants to sort the list ASC/DESC.
"""

# Prompt for the user to input the category of things, and number of things to input
category = input('Let\'s create a list of things. Think of a general category.\n'
                 'What category of things should we store? ')
numOfThings = eval(input('How many numbers of things do you want to store in your list? '))

# Prompt the user to input n things in the category using a loop statement, then store inputs in a list
itemList = []
i = 0
for i in range(numOfThings):
    item = input(category + ' ' + str(i + 1) + ': ')
    itemList.append(item)


# Prompt the user to ask what kind of sorting the user wants
sortType = input('Please enter your sorting preference(ASC/DESC): ')

# Sort the list using default sorting function
if sortType == 'ASC':
    itemList.sort()
elif sortType == 'DESC':
    itemList.sort(reverse = True)

# Prompt the user to pick a number between 1-n, and output the nth item in the list
number = eval(input('Pick a number between 1 and ' + str(numOfThings) + ': '))
print('You picked ' + itemList[number - 1] + '!')

# Print the items in sorted list
print('The sorted list is: ')
print(itemList)

# Prompt the user to pick a character
anyChar = input('Pick a character: ')

# This loop will create a list of Boolean values (true/false) of whether or not the item on the prior list contains the character that was picked by the user
containList = []
for j in range(numOfThings):
    result = anyChar in itemList[j]
    containList.append(result)

# Print the list of whether or not each item in the list contains the character inputted by user
print(containList)
