from shoe import Shoe

# Processes data.
class Process_data():

    # Reads data from file and returns a list of shoes.
    def extract_data(file_name: str) -> list:    
        try:
            data = []   
                  
            with open(f"{file_name}.txt", "r+") as read_file:
                for line in read_file:
                    lines = line.split(",")
                    data.append(lines)

                return data
        except IOError:
            print("File name does not exist.")

    # Reads data from file and returns a list of Shoe objects.
    def shoe_objects() -> list[object]:     
        try:
            processed_data = []
            file_name = "inventory"
            shoe_objects = Process_data.extract_data(file_name)

            for item in shoe_objects[1:]:
                shoe = Shoe(item[0], item[1], item[2], item[3], item[4])
                processed_data.append(shoe)      

            return processed_data
        except IOError:
            return ("File name does not exist.")