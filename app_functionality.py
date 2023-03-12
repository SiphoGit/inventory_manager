from data_processing import Process_data

class Functions:

    # Adds new shoe to the file.
    def capture_shoe(file_name: str):
        with open(file_name, 'a') as file:

            country = input("Enter country:")
            code = input("Shoe code:")
            product = input("Name:")
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
    def search_shoe(lst: list[object], shoe_code) -> str:     
        for item in lst:
            if item.code == shoe_code:
                return (f"{item}")
            
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
    def delete_shoe(shoe_objects: list, updated_new_file: str, shoe_code: str):
        try:
            for line in shoe_objects:
                if line.code == shoe_code:
                    shoe_objects.remove(line)
                    print(f"{line.product} deleted!")

                    with open(updated_new_file, "w") as file: 
                        file.write("Country,Code,Product,Cost,Quantity\n")
                        for item in shoe_objects:
                            file.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}")    

                if line.code not in shoe_code: 
                    print("Shoe not found")
                    break
        except IOError:
                    print("File name does not exist.")   
       
                