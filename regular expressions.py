import re

text = """

contact =  geo.joghn@spencer.com for buisness enquires.

support is avaliable at support@service.org or @infodomain.com

invalid emails like not an-elmail@ and @misterdmoan are ignored.

""" 

email_sequence = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

emails = re.findall(email_sequence,text)

if emails:
    
    print("found valid email adress:")

    
    for email in emails : 
        print(email)

    else :    
        print ("No valid emails found.")
