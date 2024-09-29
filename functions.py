import data

# Update an existing menu item
def update_menu_item(menu, code, field, new_value):
    pass

# Add a new item to the menu
def add_menu_item(menu, code, name, price, stock):
    pass

# Remove a menu item based on the code
def remove_menu_item(menu, code):
    pass

# Handle customer requests and verify stock availability
def process_customer_request(menu, request_code, quantity):

    quantity = int(quantity)
    for item in menu:
        if item['code'] == request_code:
            if item['stock'] >= quantity:
                item['stock'] -= quantity  # Reduce the stock
                print(f"{quantity} x {item['name']} ordered. Stock remaining: {item['stock']}")
                return True
            else:
                print(f"Not enough stock for {item['name']}. Available: {item['stock']}, Requested: {quantity}")
                return False
    print(f"Item {request_code} not found on the menu.")
    return False

# Display the menu items
def display_menu(menu):
    for item in menu:
        print(f"{item['code']} - {item['name']} - ${item['price']} (Stock: {item['stock']})")
