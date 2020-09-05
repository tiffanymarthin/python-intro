"""
File Name: marthint_hw3p2ext.py
Name: Tiffany Marthin
Last Modified: 5/10/2020
Summary: Individual Programming 3 Part 2 Extension
Goal: Create a program that reads a vocablist text file of which the user could input
more terms and definitions to the (dictionary) file. This extension will have additional features:
more terms and definitions to the (dictionary) file. This extension will have additional features:
    1. It will catch possible input errors for other user prompt questions (Y/N questions)
    2. It will add a feature of asking user what options to choose (save file, search for a term, or delete a term)
"""

#User-Defined Exception to catch if user inputs are not as expected
class Error(Exception):
    pass
class ValueNotRight(Error):
    pass

#Below is a while loop to make sure that the user enters a file name that exists
while True:
    try:
        fileName = input('Please enter a file name: ')
        inFile = open(fileName, 'r')
        break
    except IOError:
        print('Error, file does not exist.', end = ' ')


#Copy the content of the csv file into a list, to make sure that the original file is not modified
content = inFile.readlines()

#Counting the number of terms in the file and inform the user
termCt = len(content) - 1 #Minus the header
print('There are', termCt, 'terms in the new vocabulary list.')

inFile.close() #close the original file for best practices

vocabDict = {} #create an empty dictionary

"""
The for-loop will create a dictionary with terms as the keys and definitions as the values
"""
for term in content:
    term = term.replace('\n','')
    details = term.split('\t')
    vocabDict.update({details[0] : details[1]})

"""
This while loop is to prompt the user for adding more terms, it will keep looping until the user says 'No' 
to adding more terms
"""
addMore = 'Y'
while addMore == 'Y':
    while True:
        try:
            addMore = input('Would you like to add more terms (Y/N)? ')
            if addMore != 'Y' and addMore != 'N':
                raise ValueNotRight
            break
        except ValueNotRight:
            print("Error. Value has to be Y or N. ")

    if addMore == 'Y':
        #The try-except will error if the user input is not a positive integer
        try:
            addCt = eval(input('How many would you like to add? '))
            for i in range(1, addCt + 1):
                termIn = input('Term #'+ str(i) + ': ')
                #If statement to catch if the term has already existed in the current file
                if termIn in vocabDict:
                    while True:
                        try:
                            upDefn = input('Warning! This term is already in the vocabulary list. Update definition (Y/N)? ')
                            if upDefn != 'Y' and upDefn != 'N':
                                raise ValueNotRight
                            break
                        except ValueNotRight:
                            print("Error. Value has to be Y or N. ")
                    if upDefn == 'N':
                        continue #continue to the next term if user doesn't want to update definition
                    elif upDefn == 'Y':
                        pass
                defnIn = input('Definition #'+ str(i) + ': ')
                vocabDict.update({termIn : defnIn}) #Adding new pair value into the dictionary
        except TypeError:
            print('Error, Please enter an integer.')


#Inform the user about the updated number of terms in the dictionary
termCt = len(vocabDict) - 1 #Minus the header
print('There are', termCt, 'terms in the new vocabulary list.\n')

termLs = list(vocabDict.keys()) #create a list of the terms in the dictionary
newContent = ""

"""
New feature of asking the users which option they would like to do
"""

while True:
    option = input("Which feature would you like to perform (1,2,3,4)?\n"
                   +"\t 1. See content and save file\n"
                   +"\t 2. Search for a term and its definition\n"
                   +"\t 3. Delete a term from the dictionary\n"
                   +"\t 4. Exit program\n"
                   +"Select option: ")

    if option == '1':
        #Print out what are the current content of the dictionary
        for i in range(len(vocabDict)):
            print(termLs[i] + ' - ' + vocabDict.get(termLs[i]))
            newContent = newContent + termLs[i] + '\t' + vocabDict.get(termLs[i]) + '\n'

        #Ask the user for the desired file name
        print()
        newFile = input('What would you like to save the file as? ')
        outFile = open(newFile, 'w')
        outFile.write(newContent)
        outFile.close()
        print('File is successfully saved. ')
    elif option == '2':
        searchTerm = input('Enter term: ')
        print('Definition: ' + vocabDict.get(searchTerm))
    elif option == '3':
        delTerm = input('Enter term you want to delete: ')
        vocabDict.pop(delTerm)
        print('Term is deleted from dictionary.')
    elif option == '4':
        break

