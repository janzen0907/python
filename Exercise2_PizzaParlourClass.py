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
        elif allergens == 'dairy' or 'tomatoes'
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
    

                    
                
        

