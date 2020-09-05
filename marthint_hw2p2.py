"""
File Name: marthint_hw2p2.py
Name: Tiffany Marthin
Last Modified: 4/29/2020
Summary: Individual Programming 2 Part 2
Goal: Create a program that will read a roster_extended.csv file and prompt user
to enter more names with other information to be added to the file. Then save the
csv file into a text file with some formatting.
"""

print('Hello.') #saying hi to the user

#Below is a while loop to make sure that the prompt about the roster file name is entered correctly (or that the input exists)
while True:
    try:
        fileName = input('Please enter a roster file: ')
        inFile = open(fileName, 'r')
        break
    except IOError:
        print('ERROR, FILE DOES NOT EXIST.', end = ' ')

"""
Copy the content of the csv file into a list, to make sure that the original file is not modified
"""
header = inFile.readline() #this will skip the header, since the next steps is to capture the records without header
content = inFile.readlines()

"""
Counting the number of records in the file and print the information for the user 
"""
nameCount = len(content)
print('There are', nameCount, 'names in this file.', end=' ')

inFile.close() #close the original file for best practices

"""
User-defined function to convert the height from inches to feet inches format
"""
def inchToFt(lengthin):
    'returns a string value of the height in feet\'inches"'
    lengthin2 = int(lengthin)
    ft = lengthin2//12       ## 12 inches to 1 foot
    inch = lengthin2%12
    return str(ft) + "'" + str(inch) + '"'

"""
Each column is organized into a list
"""
firstName = []
lastName = []
age = []
occupation = []
height = []
weight = []
lifestyle = []

"""
The for-loop will split each of the record into different string element,
and then assign each element into the designated list defined above.
"""
for person in content:
    person = person.replace('\n','')
    details = person.split(',')
    firstName.append(details[0])
    lastName.append(details[1])
    age.append(details[2])
    occupation.append(details[3])
    htInput = inchToFt(details[4])
    height.append(htInput)
    weight.append(details[5])
    #Combining 3 lifestyle columns into one lifestyle list
    if details[6] == 'x':
        lifestyle.append('sedentary')
    elif details[7] == 'x':
        lifestyle.append('moderate')
    elif details[8] == 'x':
        lifestyle.append('active')

"""
This is the second user prompt to ask if the user wants to add additional names,
and the quantity. If the user answers yes, then the for loop is to prompt the user
to add all the information for the new records. These inputs will then be appended 
to the lists.
"""
addNameCt = 0
addName = input('Would you like to enter additional names? (Y/N)\n')
if addName == 'Y':
    addNameCt = eval(input('How many more names? ')) + 1
    for i in range(1,addNameCt):
        print('----- Person', i, '-----')
        firstName.append(input('First Name: '))
        lastName.append(input('Last Name: '))
        age.append(input('Age: '))
        occupation.append(input('Occupation: '))
        height.append(inchToFt(input('Height (in inches): ')))
        weight.append(input('Weight (in pounds): '))
        ls = eval(input('Lifestyle (1-sedentary, 2-moderate, 3-active): '))
        if ls == 1:
            lifestyle.append('sedentary')
        elif ls == 2:
            lifestyle.append('moderate')
        elif ls == 3:
            lifestyle.append('active')
print('-------------------------')

"""
Add the header line to the data
"""
firstName.insert(0,'FirstName')
lastName.insert(0,'LastName')
age.insert(0,'Age')
occupation.insert(0,'Occupation')
height.insert(0,'Ht')
weight.insert(0,'Wt')
lifestyle.insert(0,'Lifestyle')

"""
Calculate the length of the spaces needed for each column, 
it varies according to the column
"""
fnameslen = max(9,max(len(name) for name in firstName))
lnameslen = max(8,max(len(name) for name in lastName))
agelen = 3
occlen = max(10,max(len(occ) for occ in occupation))
heightlen = 5
weightlen = 3
lifestylelen = 9

"""
The last user-prompt is to ask what file name does the user want to save it as.
"""
newFileName = input('Save new roster file as: ')

newFile = open(newFileName, 'w') #ensure the file starts with blank sheet, if there is a file with same name then this will over write it
newFile.close()
newFile = open(newFileName, 'a') #append mode so the loop below will append each records

totalRecords = nameCount + addNameCt #total records equal to the beginning records in original file plus the additional names that user added
"""
This for loop will input each record with some spacing formatting
"""
for i in range(totalRecords):
    rosterprint = '{0:>{fnameslen}} {1:>{lnameslen}} {2:>{agelen}} {3:>{occlen}} {4:>{heightlen}} {5:>{weightlen}} {6:>{lifestylelen}}'.format(firstName[i],lastName[i],age[i],occupation[i],height[i],weight[i],lifestyle[i],fnameslen=fnameslen,lnameslen=lnameslen,agelen=agelen,occlen=occlen,heightlen=heightlen,weightlen=weightlen,lifestylelen=lifestylelen)
    newFile.write(rosterprint)
    newFile.write("\n") #new line after each record

newFile.close() #close file for best practices

print('File saved!')



