class Pizza:
    toppings = []
    def __init__(self, name, price, toppings):
        self.name = name
        self.price = price
        self.toppings.append(toppings)

    def __str__(self):
        return f'{self.name} has the following toppings {self.toppings}: {self.price}'

    def has_allergen(self, allergens):
        if self.toppings == allergens:
            return True
        elif allergens == 'dairy' or 'tomatoes':
            return True
        return False
    
    def add_toppings(self, **add_toppings):
        for item in add_toppings:
            if item == self.toppings:
                raise ValueError
            self.price += .75
            self.toppings.append(add_toppings)

class WhitePizza(Pizza):
    def __init__(self, name, price, toppings):
        super().__init__(name, price, toppings)

    def has_allergen(self, allergens):
        if self.toppings == allergens:
            return True
        elif allergens == 'dairy':
            return True
        return False
    
class PizzaOrder(Pizza):
    

    def __init__(self, name, price, toppings):
        super().__init__(name, price, toppings) 
    
    
    def add_pizza(pizzaToAdd):
        pizzas = []
        
        try:
            if isinstance(pizzaToAdd, Pizza):
              pizzas.append(pizzaToAdd)
        except TypeError as te:
            print("Must pass in a Pizza object")
    
    # Should have a print_order method which prints out the order as a list of the pizzas
    def print_order():
        pass
    
    # Should have a get_total method which returns the sum of all the prices of the pizzas
    def get_total():
        pass