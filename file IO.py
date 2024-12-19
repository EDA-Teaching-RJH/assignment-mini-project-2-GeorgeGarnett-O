import csv


def handle_txt_file():

    try:

        with open ('example.csv','w',newline='') as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(["name","age","height","sport"])

            writer.writerows([
                ["lydia",22,"170cm","cycling"],
                ["richard", 19, "190cm", "running"]
                ["isadora",  19, "150cm", "hiking"]
                ["jakob", 26, "190cm", "football"]
                ["monty", 35, "100cm", "sprinting"]
            ])

            print("files creating and writng is now active and a success.")

    except Exception as e:
                
            print(f"error has occurred with the writng in this file: {e}")

def read_csv_file():
    
    try:
        with open('example.csv','r') as csv_file:
            reader = csv.reader(csv_file)
            print("\ncontents of the csv file:")
            for now in reader:
                 print("row")
            
    except FileNotFoundError:
            print("missing file .check for your files for its creation")
    except Exception as e:
            print(f"an error has been presented while reading the file: {e}")

if __name__ == "__main__":

    print("write to csv file...")
    
handle_txt_file() 

print("\nReading from csv file...")

'read_csv_file'