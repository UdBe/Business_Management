import invent
import billing

def mainmenu():

    print("\nWelcome!! \n ")
    print("1. Generate Billing Details ")
    print("2. Manage Inventory ")
    print("3. Security Vault  ")
    print("4. View Transaction History ")
    print("5. Exit \n ")
    choice = int(input("Enter Choice: "))

    if choice == 1: 
        pass

    elif choice == 2: 
        invent.askmenu()
        mainmenu()  

    elif choice == 3: 
        pass

    elif choice == 4: 
        pass
    
    elif choice == 5: 
        pass

    else: 
        print("Invalid Choice")
        mainmenu()

mainmenu()