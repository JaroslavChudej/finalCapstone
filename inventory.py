#=======================================================================#
#   This program is a stock inventory manager that reads data from .txt #
#   which then a user can manipulate.                                   #
#   The program demonstrates the author's ability of using OOP.         #
#   The author is using docstrings as aditional commenting method for   #
#   the first time.                                                     #
#=======================================================================#


#======================[CLASS SHOE]========================


# The following block defines a class called Shoe that takes in five
# attributes of an object: country, code, product, cost, and quantity.
class Shoe:
    '''
    class Shoe takes in five arguments as atributes of an object 'shoe', 
    that are: country, code, product, cost, quantity.
    Methods defined within the class are: get_cost(), get_quantity() and
    __str__().
    '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method within the class to return the cost of the shoes.
    def get_cost(self):
        return self.cost
        
    # Method within the class to return the quantity of the shoes.
    def get_quantity(self):
        return self.quantity
        
    # Method within the class to return a string representation of a class.
    def __str__(self):
        return  f"Country:  {self.country}\n" \
                f"Code:     {self.code}\n" \
                f"Product:  {self.product}\n" \
                f"Cost:     {self.cost}\n" \
                f"Quantity: {self.quantity}\n"


#=============[SHOE LIST]==============

shoe_list = []
'''
The list will be used to store a list of objects of shoes.
'''

#==========[FUNCTIONS OUTSIDE THE CLASS]==============

def read_shoes_data():
    '''
    This function opens the file inventory.txt and reads the data from 
    this file, then creates a shoes object with this data and appends this 
    object into the shoes list. 
    One line in this file represents data to create one object of shoes. 
    The block uses the try-except function for error handling to verify
    the inventory.txt file exists.
    The for loop skips the first line in the file and appends the folowing 
    five attributes read in each line representing by pos[0]-pos[4], 
    country, code, product, cost, quantity. The last two attributes are 
    casted into a float and integer respectively so they can be used in 
    calculations by other functions.
    '''
    try:
        with open("inventory.txt", "r") as file:
            inventory = file.readlines()
            for line in inventory[1:]:
                line = line.strip()
                line = line.split(",")
                shoe_list.append(Shoe(line[0], line[1], line[2], float(line[3]), int(line[4])))

    except FileNotFoundError:
        output = "──────────────────────────────────────────\n"
        output += "This program requires a file inventory.txt\n"
        output += "\n"
        output += "The file not found!\n"
        output += "───────────────────────────────────────────"
        print(output)

    return shoe_list


def capture_shoes():
    '''
    This function reads in user input of shoe object attributes, creates
    a shoe object, appends this object inside the shoe list, and appends 
    the object data into the inventory.txt file for consistency.
    '''
    # The following block declares variables for user input of shoe object
    # attributes, takes the input and verifies expected values for cost and
    # quantity which must be float and integer respectively.
    country = input("Enter the country of the shoe: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the product of the shoe: ")
    
    while True:
        cost = input("Enter the cost of the shoe: ")
        try:
            cost = float(cost)
            break
        except ValueError:
            print("You have entered invalid characters!")
            continue
    
    while True:
        quantity = input("Enter the quantity of the shoe: ")
        try:
            quantity = int(quantity)
            break
        except ValueError:
            print("You have entered invalid characters!")
            continue

    # The following block creates a new shoe object and appends it into shoe list.
    shoe = Shoe(country, code, product, float(cost), int(quantity))
    shoe_list.append(shoe)

    # The following block appends the object's data to the inventory.txt file.
    with open("inventory.txt", "a") as file:
        file.write(f"{country},{code},{product},{cost},{quantity}\n")
    print(f"\nThe shoe with code {code} has been added to the inventory.\n")


def view_all():
    '''
    This function iterates over the shoes list and prints the details of the shoes 
    returned from the __str__ function.
    '''
    print("\n────[All the shoes in the inventory]────\n")
    for shoe in shoe_list:
        print(shoe)
    print("────────────────────────────────────────\n")


def re_stock():
    '''
    This function finds the shoe object with the lowest quantity, which is 
    the shoes that need to be restocked. The user can type the quantity to
    be added and the file inventory.txt is then overwritten with the new data
    in the shoe list.
    '''
    # The following block declares a variable min_quantity with positive
    # infinity value to mitigate possible errors during comparison, then 
    # it loops over the shoe list to find the lowest quantity value.
    min_quantity = float("inf")
    re_stock_shoe = None
    for shoe in shoe_list:
        if shoe.quantity < min_quantity:
            re_stock_shoe = shoe
            min_quantity = shoe.quantity

    print(f"\nThe shoe with the lowest quantity is: {re_stock_shoe}\n")

    # The following block reads in user input of the volume of shoes to be added
    # to the stock, checks if it is a positive value, and add the volume to 
    # the correct shoe object.
    # The write statement overwrites the whole .txt file, so it writes the first
    # legenda line first and then writes each line/shoe object using for loop.
    add_stock = input("Enter the quantity of shoes you would like to add to the stock: ")
    try:
        add_stock = int(add_stock)
        if add_stock < 0:
            print("Invalid input. Quantity cannot be negative.")
        else:
            re_stock_shoe.quantity += add_stock
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
                print(f"\nThe shoe with code {re_stock_shoe.code} has been restocked with {add_stock} units.\n")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def search_shoe():
    '''
    This function reads in user input of a shoe SKU code, searches shoe list
    for an object with the coresponding code using the shoe code given
    and prints it out.
    '''
    code = input("Enter the code of the shoe you want to search: ")
    found = False
    for shoe in shoe_list:
        if shoe.code == code:
            print("The details of the shoe with code " + code + " are:")
            print(shoe)
            found = True
            break
    if not found:
        print("No shoe found with code " + code)


def value_per_item():
    '''
    This function calculates the total value for each item using formula
    (value = cost * quantity) iterating through the shoe list and print the
    result for each object in the list.
    '''
    if not shoe_list:
        print("The shoe list is empty.")
    else:
        print("\n───[The value per item for all the shoes in the inventory]───\n")
        for shoe in shoe_list:
            value = shoe.cost * shoe.quantity
            print(f"{shoe.code}: {value}")
        print("──────────────────────────────────────────────────────────────\n")

def highest_qty():
    '''
    This function loops over the shoe list to find object with the highest
    value of quantity attribute and displays the object and the quantity 
    in the stock as notification that the product is on sale.
    '''
    if not shoe_list:
        print("The shoe list is empty.")
    else:
        max_quantity_shoe = shoe_list[0]
        for shoe in shoe_list[1:]:
            if shoe.quantity > max_quantity_shoe.quantity:
                max_quantity_shoe = shoe

        print(f"The shoe {max_quantity_shoe.product} with the highest quantity of {max_quantity_shoe.quantity} goes on sale!")


#========================[MAIN]==========================

# The following block is the main program menu that reads user input to 
# operate the program.

shoe_list = read_shoes_data()

while True:
    menu_output = "\n────────────────[Shoe Inventory Menu]─────────────────\n"
    menu_output += "\n    1. View all shoes\n"
    menu_output += "    2. Search for a shoe\n"
    menu_output += "    3. Add shoes to the inventory\n"
    menu_output += "    4. Re-stock shoes\n"
    menu_output += "    5. Calculate the value per item\n"
    menu_output += "    6. Determine the product with the highest quantity\n"
    menu_output += "    0. Exit\n"
    menu_output += "──────────────────────────────────────────────────────"
    print(menu_output)
   
    choice = input("Enter your choice: ")
    '''
    The following if/elif/else statement calls respective function to execute
    the command based on the user input stored in variable called choice /
    selection from the menu - Shoe Inventory Menu above.
    '''
    if choice == "1":
        view_all()
    elif choice == "2":
        search_shoe()
    elif choice == "3":
        capture_shoes()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

#===========================[END OF PROGRAM]============================#
