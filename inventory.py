from tabulate import tabulate
"""
This function creates a class Shoe. It then initialises the following attributes country,code,product,cost and quantity.
The function then creates methods def get_cost(self) which returns the cost of the shoe in this method; get_quantity(self):
which returns the quantity of the shoes;  def to_file(self) which returns detials regarding the product, country,
code, cost, and quantity.
"""
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 

    def get_cost(self):
        return ("The cost of shoes is ", str(self.cost))

    def get_quantity(self):
        return ("The quantity of the shoes is", str(self.quantity))
    
    def to_file(self):
        return f""" 
        {self.product}, {self.country}, {self.code}), {self.cost},{self.quantity}
        """

    def __str__(self):
        return f"""
        --------------------------
        "Shoe: {self.product},
        ({self.country}, 
        {self.code}),
        Cost: {self.cost}, 
        Quantity: {self.quantity}"
        """


"""
This fucntion of the program creates an empty list to store the shoes. It then opens the inventory.txt file, and skips
the first line, and then reads the data for each shoe from each line. It then creates a Shoe object for each line of 
data and appends it to the shoe_list. The try-except block is used to deal with potential errors, eg. the file not 
being found or an error occurring while reading the data. The cost and quantity attributes are converted to float and 
int types to match the types expected by the Shoe class constructor. A return the list of shoes is created.
"""
shoe_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as items_file:
            items_file.readline()
            next(items_file) 
            for line in items_file:
                country, code, product, cost, quantity = line.strip("\n").split(',')
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
                print(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt file was not found.")
    except Exception as e:
        print(f"An error occurred while reading shoe data: {e}")
    
    return shoe_list  

shoe_list = read_shoes_data()


"""
This section of the function captures the information of a new shoe from the user and creates a new Shoe object with 
the provided information. It then adds the new shoe object to the shoe_list and returns the updated list. It then 
prompts the user to enter the name, cost, and quantity of the shoe. It checks whethee the cost and quantity inputs are
positive numbers before creating the new shoe object.
"""

def capture_shoes(shoe_list):
    name = input("Please enter the name of the shoe: ")
    while True:
        cost = input("PLease enter the shoe cost: ")
        if cost.isnumeric() and float(cost) >= 0:
            break
        print("Invalid input. Please enter a positive number for cost.")

    while True:
        quantity = input("Please enter shoe quantity: ")
        if quantity.isnumeric() and int(quantity) >= 0:
            break
        print("Invalid input. Please enter a positive integer for quantity.")

    shoe = Shoe(country="", code="", product=name, cost=float(cost), quantity=int(quantity))
    shoe_list.append(shoe)
    return shoe_list


"""
This function takes a list of Shoe objects called shoe_list and uses tabular format using the tabulate module to display
the shoes information. It checks if the shoe_list is empty, if it is, it will print a message indicating that there are
no shoes available. If the tabulate module is not installed, it will print a message asking the user to install it in 
order to view the shoes in a table. The function also loops through the shoe_list and creates a list of lists with the
relevant details for each shoe, which is then passed to tabulate along with the appropriate headers to generate the 
table. The table is then printed to the console.
"""
def view_all(shoe_list):
    if not shoe_list:
        print("No shoes available.")
        return

    try:
        from tabulate import tabulate
    except ImportError:
        print("The tabulate module is not installed. Please install it to view the shoes in a table.")
        return

    shoes = []
    for s in shoe_list:
        shoes.append([s.code, s.product, s.cost, s.quantity])

    print(tabulate(shoes, headers=["Code", "Name", "Cost", "Quantity"]))


"""
This function re-stocks the shoe inventory by adding a quantity to the shoe with the lowest quantity in the list. It 
first checks if there are any shoes in the list, then determines which shoe has the lowest quantity using a lambda 
function. The user is then prompted for the quantity to be added to inventory, and updates the shoe quantity. The code 
then rewrites the shoe inventory file with the updated quantity for each shoe.
"""
def re_stock(shoe_list):
    if not shoe_list:
        print("No shoes available.")
        return

    shoe_to_restock = min(shoe_list, key=lambda x: x.quantity)
    print(f"The shoe with the lowest quantity is: {shoe_to_restock.product}")

    while True:
        restock_quantity = input(f"How many {shoe_to_restock.product} do you want to add to inventory? ")
        try:
            restock_quantity = int(restock_quantity)
        except ValueError:
            print("That was an invalid input. Please enter a number.")
            continue

        if restock_quantity < 0:
            print("The quantity cannot be negative. Please try again. ")
            continue

        break

    shoe_to_restock.quantity += int(restock_quantity)
    print(f"You have added {restock_quantity} {shoe_to_restock.product} to inventory.")

    # Rewrite the file with updated shoe quantity
    with open("shoe_inventory.txt", "w") as f:
        for s in shoe_list:
            f.write(s.to_file())

re_stock(shoe_list)


"""
This function takes in a list of Shoe objects called shoe_list. It first checks if the list is empty and prints a
message if it is. The user is then prompted to enter a shoe code to search for. It loops through the shoe_list and if
it finds a Shoe object with a matching code, it prints out the Shoe's information and returns the Shoe object. If no 
matching Shoe object is found, it prints a message indicating that.

"""
def search_shoe(shoe_list):
    if not shoe_list:
        print("No shoes available.")
        return

    search_code = input("Please enter a shoe code to search for: ")
    for s in shoe_list:
        if s.code == search_code:
            print(f"Shoe found: {s.code} - {s.product}, cost: {s.cost}, quantity: {s.quantity}")
            return s

    print(f"No shoe with code {search_code} was found.")

   
"""
This function calculates the value per item for each shoe in the shoe_list and prints the results in a table using the
tabulate module. The value per item is calculated by dividing the cost of the shoe by the quantity of that shoe. If the
shoe_list is empty, the function prints "there are no shoes available". The headers of the table are "Code", "Product",
"Cost", "Quantity", and "Value per item". The shoe data is stored in a list of lists, where each list reflects a shoe 
and contains its data and the value per item. The tabulate function is used to print the data in a formatted table.
"""
def value_per_item(shoe_list):
    if not shoe_list:
        print("No shoes available.")
        return

    shoes = []
    for s in shoe_list:
        value_per_item = s.cost / s.quantity
        shoes.append([s.code, s.product, s.cost, s.quantity, value_per_item])

    print(tabulate(shoes, headers=["Code", "Product", "Cost", "Quantity", "Value per item"]))


"""
This function determins the product woth the highest quantity. It checks whether the shoe list is empty and prints the
relevant message. It then uses the max function to obtain the quantity of shoe and the pairs available. It then prints 
that the shoe is on sale once it obtains the relevant information.
"""
def highest_qty(shoe_list):
    if not shoe_list:
        print("No shoes available.")
        return

    max_qty_shoe = max(shoe_list, key=lambda s: s.quantity)

    print(f"The shoe with the highest quantity is {max_qty_shoe.product} (code: {max_qty_shoe.code}) with {max_qty_shoe.quantity} pairs available. This shoe is now on sale.")


"""
This function contains the main menu for the shoe inventory system. It uses a while loop to keep displaying the menu 
until the user chooses to exit. Depending on the user's choice, the corresponding function is called to perform the 
desired action. The program is exited when the user chooses to exit. Also the main function is recalled when the user 
enters main.
"""
def main():
    shoe_list = read_shoes_data()

    while True:
        print("1. View all shoes")
        print("2. Value per item")
        print("3. Add shoes to inventory")
        print("4. Search for a shoe")
        print("5. Re-stock shoes and read shoe data")
        print("6. Exit program")

        choice = input("Please enter your choice: ")

        if choice == "1":
            view_all(shoe_list)
            read_shoes_data()
        
        elif choice == "2":
            value_per_item(shoe_list)
            
        elif choice == "3":
            capture_shoes(shoe_list)

        elif choice == "4":
            search_shoe(shoe_list)

        elif choice == "5":
            re_stock(shoe_list)
            read_shoes_data()

        elif choice == "6":
            print("You are exiting the program...")
            break

        else:
            print("You have entered an invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

