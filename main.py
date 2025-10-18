contacts = []
while True :
    print("1: View All Contacts")
    print("2: Add Contacts")
    print("3: Remove Contact")
    print("4: Search Contact")
    print("5: Exit")
    c1 = int(input("Enter Your Choice : "))
    
    if (c1 == 1):
        for contact in contacts:
            print(contact)
            
    elif (c1 == 2):
        name = input("Enter The Name of the Person : ")
        phone = int(input("Enter The Contact Number : "))
        contact = {
            "Name" : name,
            "Phone No" : phone
        }
        contacts.append(contact)
        
    elif(c1 == 3):
        rname = input("Enter the name of the contact you want to remove : ")
        for contact in contacts :
            if (contact['Name'].lower() == rname.lower()):
                contacts.remove(contact)
                print(f"{rname} has been removed from your contact list")
            else:
                print(f"There is no contact with the name {rname} in your contact book")
                
    elif(c1 == 4):
        sname = input("Enter The Name of Contact : ")
        for contact in contacts:
            if(contact["Name"].lower() == sname.lower()):
                print(f"Name: {contact['Name']} \n  Phone: {contact['Phone No']}")
                break
        else:
            print("Contact Not Found")
            
    elif(c1 == 5):
        break
                
                
