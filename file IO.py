import csv
import os  

def handle_txt_file():
    try:
        with open('example.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["name", "age", "height", "sport"])
            writer.writerows([
                ["lydia", 22, "170cm", "cycling"],
                ["richard", 19, "190cm", "running"],
                ["isadora", 19, "150cm", "hiking"],
                ["jakob", 26, "190cm", "football"],
                ["monty", 35, "100cm", "sprinting"]
            ])
        print("File created and written successfully.")
        print(f"File path: {os.path.abspath('example.csv')}") 
    except Exception as e:
        print(f"An error has occurred while writing to the file: {e}")

def read_csv_file():
    try:
        with open('example.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            print("\nContents of the CSV file:")
            for row in reader:
                print(row)  
    except FileNotFoundError:
        print("The file is missing. Check for its creation.")
    except Exception as e:
        print(f"An error has occurred while reading the file: {e}")

if __name__ == "__main__":
    print("Writing to CSV file...")
    handle_txt_file()

    print("\nReading from CSV file...")
    read_csv_file()