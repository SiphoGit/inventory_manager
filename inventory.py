# Imported Libraries
from tabulate import tabulate

# Shoe Class.
# Class attributes
class Shoe:

    file_contents = []
    pay_rate = 0.8
    proccessed_data = []

    # Initiates instance attributes.
    # Instance attributes.
    def __init__(self, country, code, product, cost, quantity):
    
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        # Appends all instances created to 'file_contents' list
        Shoe.file_contents.append(self)

    # Let's user search product by code.
    # Searches and prints the shoe searched.
    # Let's user exit the loop.
    def search_item(self):

        while True:
            product_code = input('''Enter Product code - to search product
E - Exit >>>''').upper()
            for item in Shoe.proccessed_data:
                if item[1] == product_code:
                    print(f"There's {item[4]} pairs of {item[2]} left.\n")
                    break

            if product_code == "E":
                print("Goodbye!!!")
                exit()

    # Sorts lists in 'file_contents' by the last value, in ascending order.
    # Appends products with lowest quantity to 'lowest_quantity' list.
    # Prints results in a table.     
    def lowest_product_quantity(self):
        
        new_file_contents = []
        lowest_quantity = []
        list_index = 0
   
        new_file_contents = sorted(Shoe.proccessed_data[1:], key=lambda lst: int(lst[4]))
        lowest_quantity.append(new_file_contents[0])  

        for lst in new_file_contents[1:]:    
            if lst[4] == new_file_contents[list_index][4]:
                lowest_quantity.append(lst)
                
        print("Shoes to be restocked.\n")
        print(tabulate([[product[2], product[4]] for product in lowest_quantity], headers=["Shoe", "Pairs"]))

    # Sorts list in 'file_contents' by the last value, in descending order.
    # Appends products with highest quantity to 'highest_quantity' list.
    # Prints results in a table. 
    def highest_product_quantity(self):

        highest_quantity = []
        list_index = 0

        new_file_contents = sorted(Shoe.proccessed_data[1:], reverse=True, key=lambda lst:int(lst[4]))
        highest_quantity.append(new_file_contents[0])  

        for lst in new_file_contents[1:]:
            if lst[4] == new_file_contents[list_index][4]:
                highest_quantity.append(lst)
        
        print("Shoes on sale.\n")
        print(tabulate([[product[2], product[4]] for product in highest_quantity], headers=["Shoe", "Pairs"]))

    # Get's the product of 'Quantity' and 'Cost' for each product.
    # Opens 'inventory.txt'
    # Joins new column to the file.
    def value_per_item(self):

        item_value = []
        [item_value.append(int(lst[4]) * int(lst[3])) for lst in Shoe.proccessed_data[1:]]

        new_file_name = input("Enter new file name>>> ")
        new_column_name = input("Enter new column name>>> ") 

        with open("inventory.txt", "r") as ofile:
            ofile = ofile.readlines()

            with open(f"{new_file_name}.txt", "w+") as ifile:
                index_counter = 0
                header = f"Country,Code,Product,Cost,Quantity,{new_column_name}\n"
                ifile.write(header)

                for line in ofile[1:]:
                    rows = line.strip().split(",")
                    ifile.write(",".join(rows) + f",{str(item_value[index_counter])}\n")
                    index_counter += 1

        # Opens the newly created file.
        # Appendes data to 'new_file_contents'
        # Prints 'new_file_contents' in a table.

        with open(f"{new_file_name}.txt", "r+") as new_file:
            new_file_contents = []
            for line in new_file:
                    line = line.split(",")                   
                    new_file_contents.append(line)

            print("\n" + tabulate([[product[0], product[1],product[2], f"{product[3]}",product[4], f"{product[5]}"] 
                for product in new_file_contents[1:]], 
                headers=["Country","Code","Product","Cost(R)", "Quantity", "Value(R)"]))

    # Reads data from an external file.
    # Creates objets from an external file
    # Error raised when file name does not exist.
    @classmethod
    def read_data(cls):

        while True:     
            try:
                file_name = input("\nEnter file name>>> ")

                with open(f"{file_name}.txt", "r+") as read_file:
                    lines = [line.split(",") for line in read_file]
       
                    shoe = [
                        Shoe(country, code, product, cost, quantity)
                        for country, code, product, cost, quantity in lines 
                        ]
                    break      
            except IOError:
                print("File name does not exist.")

    # Represents objects as strings.
    def __repr__(self):
        return f'''{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}''' 

    # Processes data and appends it to 'proccessed_data' list.
    @classmethod
    def data_proccessing(cls):

        for line in Shoe.file_contents:
            line = str(line)
            items = line.split(", ")
            Shoe.proccessed_data.append(items)
           
# Executes the program.
# Calls Shoe class.
# Reads data.
# Processes data
# Main menu and user's input.
def main():

    Shoe.read_data()
    Shoe.data_proccessing()
 
    while True:
        menu = input('''\nPlease select on of the options below:
S - search product by code
LQ - get the product with the lowest quantity
HQ - get the product with the highest quantity
V - create new column and calculate the value of each item
E - Exit
>>> ''').upper()
        print("")

        if menu == "S":
            Shoe.search_item(None)
        elif menu == "LQ":
            Shoe.lowest_product_quantity(None)
        elif menu == "HQ":
            Shoe.highest_product_quantity(None)
        elif menu == "V":
            Shoe.value_per_item(None)
        elif menu == "E":  
            print("Goodbye!\n")
            exit()
        else:
            print("Oops - incorrect input")
            
main()
