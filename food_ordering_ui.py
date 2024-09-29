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

def print_check(your_order):
    print("\nYour order:")
    print('Your check')  

def change_order(your_order):
    print("Change the order:")
    

if __name__ == '__main__':

    drinks = []
    appetizers = []
    salads = []
    entrees = []
    desserts = []


    show_main_menu()
