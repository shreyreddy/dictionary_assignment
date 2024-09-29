import data

# Update an existing menu item
def update_menu_item(menu, code, field, new_value):
    for item in menu:
        if item['code'] == code:
            if field == 'name':
                item['name'] = new_value
            elif field == 'price':
                item['price'] = int(new_value)
            print(f"{code} updated: {field} changed to {new_value}")
            return True
    print(f"Item {code} not found.")
    return False


# Add a new item to the menu
def add_menu_item(menu, code, name, price, stock):
    new_item = {"code": code, "name": name, "price": int(price), "stock": int(stock)}
    menu.append(new_item)
    print(f"Added new item: {new_item}")


# Remove a menu item based on the code
def remove_menu_item(menu, code):
    for item in menu:
        if item['code'] == code:
            menu.remove(item)
            print(f"Removed item: {code}")
            return True
    print(f"Item {code} not found.")
    return False


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
