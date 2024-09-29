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
    """
    Prints the list of items ordered, extended price, total, taxes, and grand total.
    """
    TAX_RATE = 0.07  # Assuming a tax rate of 7%
    
    if not your_order:
        print("No items ordered.")
        return

    print("\nYour Order:")
    total = 0
    for item_code, quantity in your_order:
        quantity = int(quantity)
        for menu_item in data.menu_dict:
            if menu_item['code'] == item_code:
                item_total = menu_item['price'] * quantity
                total += item_total
                print(f"{menu_item['name']} (x{quantity}) - ${menu_item['price']} each - Total: ${item_total}")
    
    tax = total * TAX_RATE
    grand_total = total + tax

    print(f"\nSubtotal: ${total:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")  

def change_order(your_order):
    """
    Allows the user to modify the current order by changing quantity or removing items.
    """
    if not your_order:
        print("Your order is currently empty.")
        return your_order

    while True:
        print("\nCurrent Order:")
        for index, (item_code, quantity) in enumerate(your_order, start=1):
            print(f"{index}. {item_code} - Quantity: {quantity}")
        
        print("\nOptions: ")
        print("C to change an item quantity")
        print("R to remove an item")
        print("B to go back to the main menu")
        
        choice = input("Choose an option: ").upper()

        if choice == 'C':
            item_num = int(input("Enter the item number you want to change: ")) - 1
            new_quantity = int(input("Enter new quantity: "))
            if 0 <= item_num < len(your_order):
                your_order[item_num] = (your_order[item_num][0], new_quantity)
                print(f"Updated {your_order[item_num][0]} to quantity {new_quantity}.")
            else:
                print("Invalid item number.")
        
        elif choice == 'R':
            item_num = int(input("Enter the item number you want to remove: ")) - 1
            if 0 <= item_num < len(your_order):
                removed_item = your_order.pop(item_num)
                print(f"Removed {removed_item[0]} from your order.")
            else:
                print("Invalid item number.")
        
        elif choice == 'B':
            break
        
        else:
            print("Invalid choice. Please try again.")

    return your_order


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
