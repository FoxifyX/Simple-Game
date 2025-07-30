import os

Contacts = "Contacts_1.txt"

def view_contacts():
    ''' View all the available contacts '''

    if not os.path.exists(Contacts):
        print("❌ No contact found!")
    else:
        with open(Contacts, "r") as f:
            lines = f.readlines()

        print("\n📝 All contacts")
        
        for line in lines:

            if line:
                name, number = line.strip().split(",")
                print(f"👤 {name} -> 📞 {number}")     

            else:
                print("❌ No contact found")


def save_contact():
    '''Save a Contact by user input'''

    name = input("\n👤 Enter the name: ")
    number = input("📞 Enter the contact number: ")

    with open(Contacts, "a") as f:
        f.write(f"{name},{number}\n")
    print(f"\n✅ Contact successfully saved..")


def rem_contact():

    if not os.path.exists(Contacts):
        print("❌ No contact found!")

    else:
        remove = input("Enter your contact name to remove: ")
        detect = False
        li = []

        with open(Contacts, "r") as f:
            
            lines = f.readlines()

            for line in lines: 
                name, number = line.strip().split(",")

                if(remove.lower() != name.lower()):
                    li.append(f"{name},{number}\n")

                else:
                    detect = True

        with open(Contacts, "w") as f:
            f.writelines(li)

        if detect:
            print("\n✅ This contact has successfully removed")

        else:

            print("\n❌ Contact can not found!")

def search(search):
    ''' Search any contact '''


    if not os.path.exists(Contacts):
        print("❌ No contact found!")
    else:

        found = False

        with open(Contacts, "r")  as f:
            lines = f.readlines()


            for line in lines:

                name, number = line.strip().split(",")  

                if search in name.lower() or search in number.lower():
                    print(f"\n👤 {name} -> 📞 {number}")
                    found = True
                
                    

        if found:
            print("✅ Contact found!")

        else:
            print("❌ No contact found!")

            
def update():
    update = input("Enter the name to update: ").strip().lower()
    found = False

    with open(Contacts, "r") as f:
        lines = f.readlines()

    updated_lines = []

    for line in lines:
        name, number = line.strip().split(",")
        if update == name.lower():
            print(f"\n👤 {name} -> 📞 {number}")
            found = True
            print("What do you want to change?\n1.Name\n2.Number")
            choice = input("📝 Enter between [1-2]: ")

            if choice == "1":
                new_name = input("Enter the new name: ")
                updated_line = f"{new_name},{number}\n"

            elif choice == "2":
                new_number = input("Enter the new number: ")
                updated_line = f"{name},{new_number}\n"

            else:
                print("⚠️ Invalid choice, skipping update.")
                updated_line = line  # keep original

            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    if found:
        with open(Contacts, "w") as f:
            f.writelines(updated_lines)
        print("✅ Contact successfully updated!")
    else:
        print("❌ No contact found!")

    
''' Main Code '''

a = True

while a:
    print("\n📒Contact Book📒\n")
    print("1.Add contact\n2.View all contact\n3.Remove Contact\n4.Search\n5.Edit\n6.Exit\n")

    choice = input("👉 Select between[1-5]: ")

    if choice:
        if(choice in ["1","2","3","4","5","6"]):
            
            if choice == "1":
                save_contact()

            elif choice == "2":
                view_contacts()

            elif choice == "3":
                rem_contact()

            elif choice == "4":
                name = input("👉 Enter a name to search: ").strip().lower()
                search(name)

            elif choice == "5":
                update()

            elif choice == "6":

                x = True
                while x:
                    again = input("⚠️ Are you want to exit?[y/n]: ").strip().lower()

                    if again == "y":
                        print("\n👋 You successfully exited..\n")
                        a = False
                        x = False

                        break

                    elif again == "n":
                        print("\n🔄 Continuing...\n")
                        x = False
                    
                    else:
                        print("⚠️ Please select between Y or N [Y = yes/N = no]")






        else:
            print("⚠️ Please select between[1-5]")

    else:
        print("❌ Can't be empty")

