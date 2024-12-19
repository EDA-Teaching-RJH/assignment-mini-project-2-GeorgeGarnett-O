import csv  # imports a module that allows me to use the tools from this import 


def handle_txt_file():# takes care of anywriting on the csv file data
    try: # starts a block to handle errors 
       
        with open('example.csv', 'w') as csv_file:  # ensures proper formatting for the csv file 
            writer = csv.writer(csv_file)# allows mne to use rows for the cvs file 

          
            writer.writerow(["name", "age", "height", "sport"])# proves catogry for the rows , the data

            
            writer.writerows([
                ["lydia", 22, "170cm", "cycling"],  
                ["richard", 19, "190cm", "running"],  
                ["isadora", 19, "150cm", "hiking"],  
                ["jakob", 26, "190cm", "football"], 
                ["monty", 35, "100cm", "sprinting"]  
            ])# writes multiple rows for the data for the file 
        
        print("File created and written successfully.")# shows in terminal the message
        
    except Exception as e:  # catches errors in the try block 
        print(f"An error has occurred while writing to the file: {e}")# message if error occurs 


def read_csv_file():# defines the function read cvs file , handling the data
    try: # block for potential errors 
        
        with open('example.csv', 'r') as csv_file:# opens example file in r meaning real mode which pons a file for reading and assigns it to the csv file 
        
            reader = csv.reader(csv_file)# makes an object link to csv file 

            print("\nContents of the CSV file:")# displays a heading 
            for row in reader:  # loops each row 
                print(row)  # prints the row 
        
    except FileNotFoundError:  # catches errors 
        print("The file is missing. Check for its creation.")# shows in terinaml if this type of error ocurs 
    except Exception as e:  # catches another error 
        print(f"An error has occurred while reading the file: {e}")# prints message if it cathes this error


if __name__ == "__main__":  #  makes it so that the block runs if the script is executed
    print("Writing to CSV file...")  
    handle_txt_file()  # calls function to write data to csv file

    print("\nReading from CSV file...")  # displays message 
    read_csv_file()  # calls function to read data from csv file 