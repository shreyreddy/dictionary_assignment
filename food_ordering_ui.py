import data
import functions

def show_main_menu():
    your_order = []
    while True:
        print("Sp's Diner")  # Display your name
        print("********************")
        print('N for a new order')
        print("C to change your order")
        print('X for close orders and print the check')
        print("R to reset the order")
        print('M for manager menu')
        print('Q for quit')
        user_menu_choice = input('Your input: ').upper()  
        
        if user_menu_choice == 'Q':
            break
        elif user_menu_choice == 'X':
            if your_order:
                print_check(your_order)
            else:
                print("No items in your order.")
        elif user_menu_choice == 'C':
            your_order = change_order(your_order)  # Change items in the order
        elif user_menu_choice == 'N':
            print('New order')
            while input('Add a dish? (y/n): ').lower() == 'y':  
                try:
                    item_code, quantity = input("Enter item code and quantity : ").split()
                    quantity = int(quantity)
                    if functions.process_customer_request(data.menu_dict, item_code, quantity):
                        your_order.append((item_code, quantity))
                    else:
                        print(f"Item code {item_code} not found in the menu.")
                except ValueError:
                    print("Invalid input. Please enter the item code followed by the quantity.")
                print('Your current order: ', your_order)
        elif user_menu_choice == 'R':
            your_order = []  # Reset the order
            print("Order reset.")
        elif user_menu_choice in 'Mm':
            manager_menu()

def print_check(your_order):
    print("\nYour order:")
    print('Your check')  

def change_order(your_order):
    print("Change the order:")

def manager_menu():
    while True:
        print("\nManager Menu:")
        print("1. Update a menu item")
        print("2. Add a new menu item")
        print("3. Remove a menu item")
        print("4. Display menu")
        print("5. Return to main menu")
        choice = input("Choose an option: ")

        if choice == '1':
            code = input("Enter item code: ")
            field = input("What do you want to update (name/price)? ").lower()
            new_value = input(f"Enter new {field}: ")
            functions.update_menu_item(data.menu_dict, code, field, new_value)
        elif choice == '2':
            code = input("Enter new item code: ")
            name = input("Enter item name: ")
            price = input("Enter item price: ")
            stock = input("Enter item stock: ")
            functions.add_menu_item(data.menu_dict, code, name, price, stock)
        elif choice == '3':
            code = input("Enter item code to remove: ")
            functions.remove_menu_item(data.menu_dict, code)
        elif choice == '4':
            functions.display_menu(data.menu_dict)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
    

if __name__ == '__main__':

    drinks = []
    appetizers = []
    salads = []
    entrees = []
    desserts = []


    show_main_menu()
