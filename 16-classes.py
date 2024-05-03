# Class names should start with caps
class Dog:
    '''A simple representation of a dog'''

    # Dunder/ magic metho
    # THis is called when you crreate a new instanece of the class
    # self will get passed in by python and must come first
    # self gets created bu the __new__ duncer function, but usually wont write that yourself
    def __init__(self, name, age):
        '''Creates a new dog object'''
        # Self refers to the current instance
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting'''
        print(f'{self.name} is now sitting')

fido = Dog('Fido', 2)
print(fido)
print(f'Dogs name is {fido.name}')
fido.sit()

