import string
import random

# s1= list of uppercase letters, s2= list of lowercase letters, s3= list of digits, s4= list of signs 
s1= string.ascii_lowercase
s2= string.ascii_uppercase
s3= string.digits
s4= string.punctuation

while True:
    user_input= input("Enter the length of password you want to create: ")
    try:
        length= int(user_input)
        if (length <= 0):
            print("Please enter a positive integer.")
            continue
            
        char_list=[] # will add here s1, s2, s3, s4
        char_list.extend(s1) # extend list with s1, s2, s3, s4
        char_list.extend(s2)
        char_list.extend(s3)
        char_list.extend(s4)
        # why not use .append here? if we append one list to another, list will go inside another list, 
        # & we don't want that. We want to add the elements of one list to another, hence we use .extend. 
        
        random.shuffle(char_list) # will shuffle all the elements of the list 
        password = ''.join(char_list[0:length]) 
        # will join all the elements of list upto len(user_input) with "" 
        print(password)  
        break

    except ValueError:
        print("Wrong Input. Try again")
