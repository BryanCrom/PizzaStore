'''
pizza ordering program
purpose: to record and display customers pizza orders
programer: Bryan Crombach
Requirements: python 3.8

Version 3
Change log:
01/05/2020- imported validation functions
01/05/2020- created boundaries for the validations
01/05/2020- validated all of the inputs apart from the house number input because house numbers arent only numbers but can contain slashes or letters.
01/05/2020- made gathering the customers phonenumber and name into its own routine instead of having it written out twice in get_contact() to make the code more efficent
01/05/2020- removed some codethat was useless such as  the isempty() in the stack and the total = 0 line before the calculation
01/05/2020- removed the question asking for the street type because my improved validation can recieve more than one word as an input
01/05/2020- improved the vocabulary in the questions being asked to make the program easier to understand for the user

Issues:
None
'''

#############################################################################################################################################
###Lists###
###########

pizzalist = []  #empty list for the pizzas file to read into and fill with the different pizza options
pricelist = []  #empty list for the prices file to read into and fill with the different price options
orderlist = []  #empty list for the ordered pizzas and their prices to append into to use in the receipt
boughtlist = []  #empty list for the ordered pizza prices to append into to use for the calculation for the total cost
addresslist = []  #empty list for the customers address to append into to then useit for the receipt

############################################################################################################################################
###Imports###
#############

from datetime import datetime  #imports datetime to be used later
from Function1 import function_one  #imports the routine function_one from the file Function1 to be used later
from validnum import validnum, validnum3, validnum4  #imports my validation routines from the file validnum

############################################################################################################################################
###Constants###
###############

MAXA = 2  #upper boundary for the delivery/pick up option or 'a'
MINA = 1  #lower boundary for the delivery/pick up option or 'a'
MAXPHO = 10000000000000  #upper boundary for the customers phone number/'phone'
MINPHO = 1000  #lower boundary for the customers phone number/'phone'
MAXPIZZA = 5  #upper boundary for the amount of pizzas a customer can order or 'amount'
MINPIZZA = 1  #lower boundary for the amount of pizzas a customer can order or 'amount'
MAXCHO = 12  #upper boundary for the code of the pizza the customer wants to order 'order'
MINCHO = 1  #lower boundary for the code of the pizza the customer wants to order 'order'


#########################################################################################################################################

def read_file():
    '''
    Purpose:this routine reads the prices and pizzas files and puts them into the pizza and price lists.
    Parameters:None
    Return:None
    '''
    pizzafile = "pizzas.txt"  #name of file
    filetoopen = open(pizzafile, "r")  #open file in read mode
    line_read = filetoopen.readline()  #makes line_read equal to filetoopen.readlin()
    while line_read != "":  #ends on first blank line
        line_read = line_read[:-1]  #strip out new line character
        pizzalist.append(line_read)  #append line to pizzalist
        line_read = filetoopen.readline()  #makes line_read equal to filetoopen.readlin()
    pricefile = "prices.txt"  #name of file
    filetoopen = open(pricefile, "r")  #open file in read mode
    line_read = filetoopen.readline()  #makes line_read equal to filetoopen.readlin()
    while line_read != "":  #ends on first blank line
        line_read = line_read[:-1]  #strip out new line character
        pricelist.append(float(line_read))  #append line to pizzalist
        line_read = filetoopen.readline()  #makes line_read equal to filetoopen.readlin()


###########################################################################################################################################

class Stack:  #create the class stack

    def __init__(self):  #initiates the stack
        self._items = []  #this is where stacks items are put into

    def push(self, item):  #initiates the push function
        self._items.append(item)  #appends items into the stack

    def pop(self):  #initiates the pop function
        return self._items.pop()  #pops/removes items out of the stack

    def peek(self):  #initiates the peek function
        return self._items[-1]  #looks at the first item in the stack

    def size(self):  #initiates the size function
        return len(self._items)  #shows the size of the stack


audit_stack = Stack()  #creates the audit stack
print_stack = Stack()  #creates the print stack


#############################################################################################################################################

def get_contacts():
    '''
    Purpose:this routine welcomes the user and asks if the order is delivery or pick up then gathers the comstumers name and phone number.
    Parameters:None
    Return:name,extra,phone
    '''
    print("\nWELCOME TO DREAM PIZZAS\n" + "-" * 23)  #prints a welcome message
    print("Press 1 for Delivery\nPress 2 for Pick up")  #print first question asking if order is delivery or pick up
    a = validnum(MINA,
                 MAXA)  #validates the answer/"a" to the question asked above and checks if it is within the boundaries MINA and MAXA and if it contains any invalid answers and returns valid answer
    if a == 1:  #if a is equal to 1 run this code
        print("extra $3 delivery cost added to bill")  #print delivery charge statement
        extra = 3  #make extra equal three
        audit_stack.push("Delivery")  #put delivery into the audit stack
        name, phone = get_name()  #run the get_name routine to collect the customers name and phone number
        get_address()  #run the get_address routine to collect the customers address
        return name, extra, phone  #returns extra and the customers name and phone number to be used later
    elif a == 2:  #if a is equal to 2 run this code
        audit_stack.push("Pick up")  #put Pick up into the audit stack
        name, phone = get_name()  #run the get_name routine to collect the customers name and phone number
        extra = 0  #make extra equal zero
        return name, extra, phone  #returns extra and the customers name and phone number to be used later


###################################################################################################################################################################################

def get_name():
    '''
    Purpose:this routine collects the customers name and phone number.
    Parameters:None
    Return:name,phone
    '''
    print("\nPlease enter customer's name: ")  #print question asking for customers name
    name = validnum3()  #validates the answer/"name" to the question asked above and checks if it contains any invalid answers and returns valid answer
    audit_stack.push(name)  #put the customers name into the audit stack
    print("\nplease enter customer's phone number: ")  #print question asking for customers phone number
    phone = validnum(MINPHO,
                     MAXPHO)  #validates the answer/"phone" to the question asked above and checks if it is within the boudaries MINPHO and MAXPHO and if it contains any invalid answers and returns valid answer
    audit_stack.push(phone)  #put the customers phone number into the audit stack
    return name, phone  #return the customers name and phone number so it can be used later


################################################################################################################################################################

def get_address():
    '''
    Purpose:this routine gets the customers address details and put them in a list so that the pizzas can be delivered
    Parameters:None
    Return:None
    '''
    print(
        "\n--please enter the delivery adress--\nPlease enter the house number: ")  #prints enter address statement and then question asking for the delivery address on a new line
    house_num = input()  #makes house_num equal to the answer to the question asked above
    addresslist.append(house_num)  #appends the house number into the addresslist
    print(
        "\nPlease enter the full street name(e.g. Great South Road):")  #print the question asking for the delivery street name
    street_name = validnum3()  #validates the answer/"street_name" to the question asked above and checks if it contains any invalid answers and returns valid answer
    addresslist.append(street_name)  #appends the street name into the addresslist
    print("\nPlease enter the suburb:")  #print the question asking for the delivery suburb
    suburb = validnum3()  #validates the answer/"suburb" to the question asked above and checks if it contains any invalid answers and returns valid answer
    addresslist.append(suburb)  #appends the suburb into the addresslist


##################################################################################################################################################################

def menu():
    '''
    Purpose:prints the pizza menu with prices for each one
    Parameters:None
    Return:None
    '''
    count = 1  #makes count equal 1
    print(" ")  #print nothing to make a space without breaking the menu
    for pizza in pizzalist:  #for every pizza/item in the pizza list
        print(count, pizza, "$" + str(pricelist[count - 1]))  #print count, pizza name and the price of the pizza
        count = count + 1  #increase count by one


####################################################################################################################################################################

def how_many():
    '''
    Purpose:find out how many pizzas the customer wants to purchase
    Parameters:None
    Return:amount
    '''
    print(
        "How many pizzas would you like to purchase? (Max 5 pizzas)")  #prints question asking how many pizzas the customer wants to purchase
    amount = validnum(MINPIZZA,
                      MAXPIZZA)  #validates the answer/"amount" to the question asked above and checks if it is within the boudaries MINPIZZA and MAXPIZZA and if it contains any invalid answers and returns valid answer
    audit_stack.push(amount)  #put amount into the audit stack
    return amount  #return amount so it can be used later


######################################################################################################################################################################

def get_pizza(amount, extra, name, phone):
    '''
    Purpose:this routine runs the pizza selection proccess in order and put the order into a list so it can later be used
    Parameters:amount,extra,name,phone
    Return:None
    '''
    while amount != 0:  #start while loop that when amount doesnt equal zero run code
        print("\n" + str(
            amount) + " pizzas remaining\nwhich Pizza would you like to purchase? (1-12)")  #prints statement thatb tells the user how many pizzas they can choose and asks which pizza they want to order
        amount = int(amount)  #make amount an integer
        order = validnum(MINCHO,
                         MAXCHO)  #validates the answer/"order" to the question asked above and checks if it is within the boudaries MINCHO and MAXCHO and if it contains any invalid answers and returns valid answer
        print("You have ordered the", pizzalist[order - 1],
              "pizza")  #prints a statement telling the user the pizza they have selected has been ordered
        pizza = (" pizza ")  #make pizza equal to pizza-
        price = ("$")  #make price equal to $
        orderlist.append(pizzalist[order - 1] + pizza + price + str(pricelist[
                                                                        order - 1]))  #append the pizza they have ordered, pizza, price and the price of the pizza they have ordered into the order list
        boughtlist.append(pricelist[order - 1])  #append the price of the pizza they have ordered into boughtlist
        amount = amount - 1  #decrease amount by one
    else:  #when while loop if finished run code
        get_price(extra, name, phone)  #run get_price routine


##########################################################################################################################################################################

def get_price(extra, name, phone):
    '''
    Purpose:print a receipt of the order placed and the customers details for the user
    Parameters:extra,name,phone
    Return:None
    '''
    total = function_one(sum(boughtlist),
                         extra)  #calculates the total of all the ordered pizzas and the extra delivery charge
    total = str(total)  #makes total a string
    total = ("$" + total)  #make total the price and a dollar sign behind it
    audit_stack.push(total)  #put the total into the audit stack
    if extra == 0:  #if extra is equal to zero then run this code
        print("\nCurrent Order\n" + "-" * 13 + "\n" + '\n'.join(map(str, orderlist)),
              "\nTotal:" + total + "\n\n--Customer info--\nName:" + str(name) + "\nPhone number:" + str(
                  phone))  #print reciept message containg the pizzas ordered, the total and the customers contact details
    elif extra == 3:  #else if extra equals 3 then run this code
        print("\nCurrent Order\n" + "-" * 13 + "\n" + '\n'.join(map(str, orderlist)),
              "\nDelivery cost $3\nTotal:" + total + "\n\n--Customer info--\nName:" + str(
                  name) + "\nPhone number:" + str(phone) + "\nAddress:" + str(addresslist[0]) + " " + str(
                  addresslist[1]) + ",", addresslist[
                  2])  #print reciept message containg the pizzas ordered, the delivery cost, the total, the customers address and the customers contact details


###########################################################################################################################################################################################################################################################################################

def confirm():
    '''
    Purpose:confirms if the order wants to be placed
    Parameters:None
    Return:None
    '''
    print(
        "\nWould you like to cancel the current order? (Y/N)")  #print this question asking if the user would like to cancel this order
    answer = validnum4()  #validates the answer/"answer" to the question asked above and checks if it contains any invalid answers and returns valid answer
    if answer == 'Y' or answer == 'y':  #if answer is equal to Y or y run this code
        print("Order cancelled.")  #print a statement telling the user the order has been cancelled
        audit_stack.push("Order cancelled")  #put "order cancelled" into the audit stack
        another()  #run the "another" routine
    elif answer == 'N' or answer == 'n':  #else if answer is equal to N or n run this code
        print("Order confirmed")  #print a statement telling the user the order has been confirmed
        audit_stack.push("Order Completed")  #put "order conpleted" into the audit stack
        another()  #run the "another" routine
    else:  #else run code
        print("Invalid Response")  #print invalid response statement if they input a str but not 'y' or 'n'
        confirm()  #run the confirm() routine again


###################################################################################################################

def another():
    '''
    Purpose:asks if they want to ,ake another order
    Parameters:None
    Return:None
    '''
    print(
        "\nWould you like to make another order? (Y/N)")  #print this question asking if the user would like to make another order
    answer = validnum4()  #validates the answer/"answer" to the question asked above and checks if it contains any invalid answers and returns valid answer
    if answer == 'Y' or answer == 'y':  #if answer is equal to Y or y run this code
        write_audit()  #run the write_audit routine
        main()  #run the main routine again
    elif answer == 'N' or answer == 'n':  #else if answer is equal to N or n run this code
        print(
            "\nThank you for ordering at dream pizza\nEnjoy your pizza")  #print thank you statement at the end of the orders
        write_audit()  #run the write_audit routine
    else:  #else run code
        print("Invalid Response")  #print invalid response statement if they input a str but not 'y' or 'n'
        another()  #run the another() routine again


#####################################################################################################################

def write_audit():
    '''
    Purpose:writes the audit on a separate file
    Parameters:None
    Return:None
    '''
    while (audit_stack.size() > 0):  #while the audit stack has items in it the while loop will run
        print_stack.push(audit_stack.peek())  #put the top item in the audit stack into the print stack
        audit_stack.pop()  #remove the top of the audit stack
    now = datetime.now()  #now equals datetime.now() which gets the current date and time
    message = (
        "Time:({}) Delivery or Pick up:({}) Customer name:({}) Customer phone:({}) Number of pizzas ordered:({}) Total cost:({}) Completed/Cancelled:({})".format(
            now, print_stack.pop(), print_stack.pop(), print_stack.pop(), print_stack.pop(), print_stack.pop(),
            print_stack.pop()))  #this creates the finished audit that is to be printed in the audit file
    file = "audit.txt"  #call the file audit.txt
    with open(file, 'a+') as file_object:  #make and open a text file called audit.txt
        file_object.write("\n")  #in the audit file make a new line
        file_object.write(message)  #in the audit file print message
        file_object.close()  #close the audit file
    del orderlist[:]  #delete the contents of orderlist
    del boughtlist[:]  #delete the contents of boughtlist


#######################################################################################################################################################################################################################################################################################################

def main():
    '''
    Purpose:runs all of the other routines apart from get_contacts
    Parameters:extra,name,phone
    Return:None
    '''
    name, extra, phone = get_contacts()  #run the get_contacts routine
    menu()  #run the menu routine
    amount = how_many()  #runs the how_many routine
    get_pizza(amount, extra, name, phone)  #runs the get_pizza routine
    confirm()  #runs the confirm routine


##########################################################################################################

read_file() #runs the read file routine
main()  #runs the main routine

####################################################
