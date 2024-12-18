import re # this si to import the module so i can use regular expressions 

email_info = """

contact =  geo.joghn@spencer.com for buisness enquires.

support is avaliable at support@service.org or @infodomain.com

invalid emails like not an-elmail@ and @misterdmoan are ignored.

""" # texts comitaing various  emails also """ is used to help with search for valid and invlaid emails  

email_sequence = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b" # this is a sequnce of peramerts for the username and symbols to fit within eff3ctively ensuring that only valid email adress is correct and matches contaained symbols and letter within this sequnce.

emails = re.findall(email_sequence,email_info)# searches though function email_info list for matching email subtracting that match provided  

if emails: # checks that the email in the lsit is valid and not empty and matches
    
    print("found valid email adress:") # shows text in terminal

    
    for email in emails : # this loops though the list of matched emails 
        print(email) # shows text in teminal 

    else :    # if not valid email is found will print said text belwo 
        print ("No valid emails found.")
