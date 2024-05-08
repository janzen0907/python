from pathlib import Path

# Not working currently 

path = Path('./pi_million_digits.txt')
pi = path.read_text()
# print(pi)

while True:
    print("Pick an option")
    print("1: Print digits of pi")
    print("2: Find birthday in Pi'")
    print("3: Quit")

    choice = input("Pick an option")
    if choice == '1':
        how_many_digits = input("How many digits to disply?")
        try:
            how_many_digits = int(how_many_digits)
        except ValueError:
            print("Must be a number")
            continue

        print(f"First {how_many_digits} of pi are")
        print(f"3.{pi[1:how_many_digits]}")
    elif choice == '2':
        birthdate = input("Enter your bday in dd/mm/yyyy format")
        # check the format
        if birthdate[2:3] != '/' or birthdate[5:6] != '/':
            raise ValueError("Date is in the wrong format")

        birthdate = birthdate.replace('/', '')
        try:
            int(birthdate)
        except ValueError:
            raise ValueError("Could not convert the date")
        
        index = pi.index(birthdate)
        print(f"Your birthdate exists {index} digits")
        

        


    elif choice == '3':
        print("Goodbye")
        quit()
    else:
        print("Pick an option form the menu")
    
        
 





        
    

