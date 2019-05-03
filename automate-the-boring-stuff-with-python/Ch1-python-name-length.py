
# This program asks for first and last name then prints total length of name.

print ('Hi!')
print ('What is your first name?') # asks for first name
myFName = input()
print ('What is your last name?') # asks for last name
myLName = input()
print ('Thank You, ' + myFName + " " + myLName)

NameLen = len(myFName) + len(myLName)
print ('The length of your name is, ' + str(NameLen)) # prints total length of name

