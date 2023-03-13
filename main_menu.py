from data_processing import Process_data
from app_functionality import Functions

# Main menu
class Menu:

    def main():
      while True:
        
        menu = input('''Main menu:
        1 - View Inventory 
        2 - Add new shoe 
        3 - Search Shoe 
        4 - Display shoe with the lowest quantity
        5 - Display shoe with the highest quantity 
        6 - Calculate the value of each shoe
        7 - Update shoe
        8 - Delete Shoe
        0 - Close Application
        >>> ''')  
            
        if menu == "1":
            file_name = "inventory"
            shoe_object = Process_data.shoe_objects()
            Functions.view_inventory(shoe_object)
        elif menu == 2:
           file_name = "inventory.txt"
           Functions.capture_shoe(file_name)
        elif menu == "3":
           shoe_code = input("Enter shoe code - to search:").upper()
           shoe_object = Process_data.shoe_objects()
           shoe = Functions.search_shoe(shoe_object, shoe_code)
           print(shoe)
        elif menu == "4":
           shoe_object = Process_data.shoe_objects()
           shoe = Functions.lowest_shoe_quantity(shoe_object)
           print(shoe)
        elif menu == "5":
           shoe_object = Process_data.shoe_objects()
           shoe = Functions.highest_shoe_quantity(shoe_object)
           print(shoe)
        elif menu == "6":
           shoe_object = Process_data.shoe_objects()
           shoe = Functions.value_per_item(shoe_object)
        elif menu == "7":
           shoe_code = input("Enter shoe code - to update:").upper()
           shoe_object = Process_data.shoe_objects()
           shoe = Functions.update_shoe(shoe_object, shoe_code)
        elif menu == "8":
           shoe_code = input("Enter shoe code to delete: ").upper()
           shoe_object = Process_data.shoe_objects()
           shoe = Functions.delete_shoe(shoe_object, shoe_code)
        elif menu == "0":
           print("Bye!")
           exit()
        else:
           print("Invalid input. Please try again.")
             
    main()