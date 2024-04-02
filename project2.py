# Mini Project 2

import re
contacts = {}

email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$")
name_pattern = re.compile(r"^[a-zA-Z]+$")
phone_pattern = re.compile(r"^\d{10}$") 

def display_menu():
    print("\nMenu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Quit")

def add_contact():
    print("\nEnter contact details:")
    name = input("Name: ")
    while not name_pattern.match(name):
        print("Invalid name! Please enter a valid name.")
        name = input("Name: ")

    phone = input("Phone number: ")
    while not phone_pattern.match(phone):
        print("Invalid phone number! Please enter a valid phone number.")
        phone = input("Phone number: ")

    email = input("Email address: ")
    while not email_pattern.match(email):
        print("Invalid email address! Please enter a valid email.")
        email = input("Email address: ")

    additional_info = input("Any additional info: ")

    unique_id = phone  
    contacts[unique_id] = {'Name': name, 'Phone': phone, 'Email': email, 'Additional Info': additional_info}
    print("Contact added successfully!")

def edit_contact():
    search_key = input("\nEnter phone number of contact to edit: ")
    if search_key in contacts:
        print("\nEditing contact with phone number:", search_key)
        print("Current details:")
        print(contacts[search_key])
        
        new_name = input("New Name (Leave empty if you want it to stay the same): ")
        if new_name:
            contacts[search_key]['Name'] = new_name
        new_phone = input("New Phone (Leave empty if you want it to stay the same): ")
        if new_phone:
            while not phone_pattern.match(new_phone):
                print("Invalid phone number! Please enter a 10-digit phone number.")
                new_phone = input("New Phone (Leave empty if you want it to stay the same): ")
            contacts[search_key]['Phone'] = new_phone
        new_email = input("New Email (Leave empty if you want it to stay the same): ")
        if new_email:
            while not email_pattern.match(new_email):
                print("Invalid email address! Please enter a valid email.")
                new_email = input("New Email (Leave empty if you want it to stay the same): ")
            contacts[search_key]['Email'] = new_email
        new_additional_info = input("New Additional Info (Leave empty if you want it to stay the same): ")
        if new_additional_info:
            contacts[search_key]['Additional Info'] = new_additional_info
        print("Contact updated !")
    else:
        print("Contact not found!")

def delete_contact():
    search_key = input("\nEnter phone number of contact to delete: ")
    if search_key in contacts:
        del contacts[search_key]
        print("Contact deleted!")
    else:
        print("Contact not found!")

def search_contact():
    search_key = input("\nEnter phone number of contact to search: ")
    if search_key in contacts:
        print("\nContact details:")
        print(contacts[search_key])
    else:
        print("Contact not found!")

def display_all_contacts():
    print("\nAll contacts:")
    for key, value in contacts.items():
        print(key, ":", value)

def export_contacts():
    file_name = input("\nEnter the file name to export contacts: ")
    file = open(file_name, 'w')
    for key, value in contacts.items():
        file.write(f"{key} : {value}\n")
    file.close()
    print("Contacts exported successfully!")

# -------------------------    

print("Welcome to the Contact Management System!")
while True:
    display_menu()
    choice = input("\nEnter your choice (1-7): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        edit_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        display_all_contacts()
    elif choice == '6':
        export_contacts()
    elif choice == '7':
        print("Thank you for using the Contact Management System!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 7.")

"""
Hello !
When you first open this app you will have options to add, edit, delete, search, display, or eport your contacts.
When you select add a contact, you will add the name, 10 digit number(which can be used to search for this contact in the future),
email, and anything additional info you would like to add.
When you would like to edit a contact, you will enter 2 from the menu and use that 10 digit number to look up which 
contact you would like to edit. The app will then go through which information you would like to edit.
Meaning you will first have the option to edit the name by just entering the new name, and if you dont wish to edit the name 
you would just hit enter to go through the next options and repeat (phone number, email, additional info).
When you would like to delete a contact, you will enter 3 and you would just enter their correct 10 digit phone number and if it is not
entered correctly you would have another chance to enter the valid phone number.
When you want to search for a contact, you will enter 4 and enter their valid 10 digit phone number  and the app will 
display all of their information.
When you enter 5, all of your contacts will be displayed.
When you enter 6, this exports your contacts from this app to a seperate text file
And of course once you enter 7, this will allow you to quit 


"""
    

