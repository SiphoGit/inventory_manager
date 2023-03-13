from data_processing import Process_data

class Functions:

    # Adds new shoe to the file.
    def capture_shoe(file_name: str):
        with open(file_name, 'a') as file:

            country = input("Enter country:").capitalize()
            code = input("Shoe code:").upper()
            product = input("Name:").capitalize()
            cost = input("Cost:")
            quantity = input("Quantity:")

            writer = [country, code, product, cost, quantity]

            # Write shoe information to the file
            for item in writer:
                if item != writer[-1]:
                    file.write(f"{item},")
                else:
                    file.write(item)

            file.write('\n')

        print(f"{product} added!")

    # Prints the inventory.
    def view_inventory(lst: list[object]): 
        for shoe in lst: 
            print(shoe)
            
    # Lets the user to search a shoe using shoe code.
    def search_shoe(lst: list[object], shoe_code: str) -> str:     
        for shoe in lst:
            if shoe.code == shoe_code:
                return shoe
            
        return ("Shoe not found.")
    
    # returns the shoe with the lowest quantity.
    def lowest_shoe_quantity(lst: list[object]) -> str:
        new_file_contents = sorted(Process_data.shoe_objects(), key=lambda lst: int(lst.quantity))

        return (f'''The Shoe with the lowest quantity is: \nShoe name: {new_file_contents[0].product} \nQuantity: {new_file_contents[0].quantity} ''')
    
    # Returns the shoe with the highest quantity.
    def highest_shoe_quantity(lst: list[object]) -> str:
        new_file_contents = sorted(Process_data.shoe_objects(), reverse=True, 
                                   key=lambda lst: int(lst.quantity))
        
        return (f'''The Shoe with the highest quantity is: \nShoe name: {new_file_contents[0].product} \nQuantity: {new_file_contents[0].quantity} ''')

    # Return the total value of each shoe type
    def value_per_item(shoe_objects: list[object]) -> str:       
        for shoe in shoe_objects:
            value = int(shoe.quantity) * int(shoe.cost)
            print(f"\nShoe: {shoe.product} \nValue: R{value}")
    
    # Removes shoe from inventory.
    def delete_shoe(shoe_objects: list[object], shoe_code: str):
        try:
            for line in shoe_objects:
                if line.code == shoe_code:
                    shoe_objects.remove(line)
                    print(f"{line.product} deleted!")

                    with open("inventory.txt", "w") as file: 
                        file.write("Country,Code,Product,Cost,Quantity\n")

                        for item in shoe_objects:
                            file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}")    
                else:
                    print("Shoe not found")
                    break         
        except IOError:
                    print("File name does not exist.")   
    
    def update_shoe(shoe_objects: list[object], shoe_code: str) -> str:      
        try:            
            for shoe in shoe_objects:
                if shoe.code == shoe_code:
                    print(f"\nEdit: {shoe}")

                    select_option = input('''\nWhat would you like to edit:
                    1 - Country
                    2 - Code 
                    3 - Shoe name 
                    4 - Shoe price
                    5 - Shoe quantity
                    0 - Back to main menu
                    >>> ''')

                    if select_option == "1":
                        new_country = input("Enter new country: ").upper()
                        shoe.country = new_country
                        
                        with open("inventory.txt", "w") as file:
                            file.write("Country,Code,Product,Cost,Quantity\n")
                            
                            for item in shoe_objects:
                                file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}") 

                        print(f"{shoe.product} country updated!\n{shoe}" )   
                    elif select_option == "2":
                        new_code = input("Enter new code: ").upper()
                        shoe.code = new_code
                        
                        with open("inventory.txt", "w") as file:
                            file.write("Country,Code,Product,Cost,Quantity\n")

                            for item in shoe_objects:
                                file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}") 

                        print(f"{shoe.product} code update!\n{shoe}" )  
                    elif select_option == "3":
                        new_shoe_name = input("Enter new shoe name: ").capitalize()
                        shoe.product = new_shoe_name
                        
                        with open("inventory.txt", "w") as file:
                            file.write("Country,Code,Product,Cost,Quantity\n")
                            for item in shoe_objects:
                                file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}") 

                        print(f"Shoe name updated to {shoe.product}\n{shoe}" )   
                    elif select_option == "4":
                        new_price = input("Enter new price: ")
                        shoe.cost = new_price
                        
                        with open("inventory.txt", "w") as file:
                            file.write("Country,Code,Product,Cost,Quantity\n")
                            for item in shoe_objects:
                                file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}") 

                        print(f"{shoe.product} price updated!\n{shoe}" )   
                    elif select_option == "5":
                        new_quantity = input("Enter new quantity: ")
                        shoe.quantity = f"{new_quantity}\n"
                        
                        with open("inventory.txt", "w") as file:
                            file.write("Country,Code,Product,Cost,Quantity\n")
                            for item in shoe_objects:
                                file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}") 
                        print(f"{shoe.product} price updated!\n{shoe}" )      
                    elif select_option == "0":
                        break
                    else:
                        print("invalid option")
        except IOError:
                print("File name does not exist.") 

                