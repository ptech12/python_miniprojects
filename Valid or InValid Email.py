import re             #importing module "Regex"

pattern="[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|net|org|edu)"   #defining the required pattern match

user_input=input("Enter the Email_Address: ")   #user input email

if(re.search(pattern,user_input)):    #Check the given input with matching string pattern

    print("Valid Email")

else:

    print("InValid Email")