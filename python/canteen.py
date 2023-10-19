# Define the menu items
import time

food_menu = {
    "Rice": {
        "price": 500
    },
    "Beans": {
        "price": 300
    },
    "Pasta": {
        "price": 150
    },
    "Yam": {
        "price": 100
    },
    "Plantain": {
        "price": 50
    },
}

protein_menu = {
    "Egg": {
        "price": 200
    },
    "Fish": {
        "price": 150
    },
    "Shrimp": {
        "price": 1000
    },
    "Broccoli": {
        "price": 700
    },
    "Chickpeas": {
        "price": 250
    },
}

drinks_menu = {
    "Green Tea": {
        "price": 400
    },
    "Coffee": {
        "price": 1500
    },
    "Orange Juice": {
        "price": 600
    },
    "Soda": {
        "price": 250
    },
    "Alcoholic Beverages": {
        "price": 2000
    },
}

# Define a function to display the menus
def display_menus():
    print("Food Menu:")
    for item, details in food_menu.items():
        print(f"{item}: ${details['price']}")
    time.sleep(2)
    print("\nProtein Menu:")
    for item, details in protein_menu.items():
        print(f"{item}: ${details['price']}")
    time.sleep(2)
    print("\nDrinks Menu:")
    for item, details in drinks_menu.items():
        print(f"{item}: ${details['price']}")

# Define a function to take orders
def place_order():
    total_cost = 0
    order = {}
    time.sleep(2)
    while True:
        display_menus()
        item = input("Enter the item you want to order (or 'done' to finish): ").strip()
        
        if item.lower() == 'done':
            break
        
        menu = None
        
        if item in food_menu:
            menu = food_menu
        elif item in protein_menu:
            menu = protein_menu
        elif item in drinks_menu:
            menu = drinks_menu
        
        if menu is not None:
            quantity = int(input(f"Enter the quantity of {item} you want to order: "))
            if quantity > 0:
                order[item] = quantity
                total_cost += menu[item]['price'] * quantity
            else:
                print("Quantity must be greater than 0.")
        else:
            print("Item not found in the menu. Please try again.")
    
    return order, total_cost

# Main program
print("Welcome to My Kitchen")
order, total_cost = place_order()

if order:
    print("\nYour Order:")
    for item, quantity in order.items():
        print(f"{item} x{quantity}")
    
    print(f"Total Cost: ${total_cost}")
    print("Thank you for ordering!")

