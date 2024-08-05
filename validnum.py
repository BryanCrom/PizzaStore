def validnum(low,high):
    '''
    purpose: make sure number is valid
    parameters: low and high
    return: the valid number/num
    '''
    while True:#start while loop
        try:
            num = int(input())#num is equal to the input that is being validated
            if num >= low and num <= high:#test if the number is within our max and min
                return num#return valid number
                break#end loop
            else:#num is a valid number else run this code
                print("Please enter a number between",low,"and", high)#print command if number is not within our min and max
        except ValueError:#check if input has a value error then print command
            print("Please enter a valid number")#ask to input a valid number if number is not valid


#####################################################################################
        
def validnum2(low,high):
    '''
    purpose: make sure float is valid
    parameters: low and high
    return: the valid number/num
    '''
    while True:#start while loop
        try:
            num = float(input())#num is equal to the input that is being validated
            if num >= low and num <= high:#test if the number is within our max and min
                return num#return valid number
                break#end loop
            else:#num is a valid number else run this code
                print("Please enter a number between",low,"and", high)#print command if number is not within our min and max
        except ValueError:#check if input has a value error then print command
            print("Please enter a valid number")#ask to input a valid number if number is not valid




#########################################################################################

def validnum3():
    '''
    purpose: make sure string is valid
    parameters: low and high
    return: the input/entry
    '''
    while True:#start while loop
        entry = str.title(input())#entry is the input that is being validated
        if (any(x.isalpha() for x in entry)and all(x.isalpha() or x.isspace() for x in entry)):#if any of the characters of the input are a letter and the charcter in the input are only letters and spaces/[space] run this code
            return entry#return the validated entry
            break#break from loop
        else:#if not valid run this code
            print("Entry must not contain numbers or special characters excluding spaces")#print statement telling the user not to input any special charcters or numbers excluding space

###########################################################################################

def validnum4():
    '''
    purpose: make sure string is valid
    parameters: low and high
    return: the input/entry
    '''
    while True:#start while loop
        entry = str.title(input())#entry is the input that is being validated
        x = entry.isalpha()#x equals entry.isalpha which becomes false if any of the characters in the input are not letters
        if x == False:#if x if false
            print("Entry must not contain numbers, special characters or spaces")#print statement telling the user not to input any special charcters or numbers invluding [space]
        else:#if valid run this code
            return entry#return the validated entry
            break#break from loop
       
 
        
