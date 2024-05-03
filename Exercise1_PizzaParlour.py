
# Fix this later
pizzas = [
    {
        'type': 'Pepperoni', 
        'price': 12.50, 
        'sauce': 'red', 
        'toppings': ['pepperoni']}, 
    {
    'type': 'Cheese', 'price': 11.25,
    'sauce': 'red', 'toppings': []}, 'pizza_type': 'Chicken Bacon Ranch',
          'price': 14.10, 'sauce': 'white', 'toppings': 'chicken, bacon, ranch',
          'pizza_type': 'Canadian', 'price': 13.50, 'sauce': 'red', 'toppings':
          'sausage, bacon, onion'}
]

orders = []
message = 0
while message != 4:

    message = input('Please select from the following options; 1: Add pizza to order, 2:Check order for allergen, 3:Print Order, 4: quit')
    int(message)
    print(message)
    if message == 1:
        print(pizzas['pizza_type'])
        pizza_to_add = input("What pizza would you like to add to your order?")
        orders.append(pizza_to_add)
        orders.append(pizzas['price'])
    elif message == 2:
        allergy = input('What allergens would you like to check for?')
        if pizzas['toppings'] in allergy:
            print(f'{pizzas["pizza_type"]} contains the following allergens ')
        elif allergy == 'tomato':
            if pizzas['sauce'] == 'red':
                print(f'{pizzas["pizza_type"]} contains the following allergens ')
        elif allergy == 'dairy' or 'cheese':
            if pizzas['sauce'] == 'white':
                print(f'{pizzas["pizza_type"]} contains the following allergens ')
        else:
            print("No allergens in this order")
    if message == 3:
        for order in orders:
            print(order)
    if message == 4:
        quit()

    
    

