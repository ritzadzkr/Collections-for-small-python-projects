#CALCULATOR (Simple)
#Basic arithmetic operations: addition, subtraction, multiplication, division

class Calculator:
    #addition
    def add(self, x, y):
        return x + y

    #subtraction1
    def subtract(self, x, y):
        return x - y

    #multiplication
    def multiply(self, x, y):
        return x * y

    #division
    def division(self, x, y):
        return x / y

calculator = Calculator()

#Arithmetic operation
Operations = {
'1': 'Addition',
'2': 'Subtraction',
'3': 'Multiplication',
'4': 'Substitution',
'5': 'Exit the calculator'
}

#The actual operation
while True:
    print("\nMenu:")
    for  key, value in Operations.items():
        print(f"{key}: {value}")
    
    choice = int(input("Choose an Option: "))
    
    while True:
        try :
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            break
        except ValueError:
            print ("Invalid Input! Please input the correct numbers")
            continue

            
    if choice == '1':
        print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
        while True:
            cont = input("Would you like to continue? (y/n) ")
            if cont.lower() == 'y' :
                break
            elif cont.lower() == 'n' :
                print("Exiting...")
                exit()
            else:
                print("Please enter y or n")

    elif choice == '2':
        print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
        while True:
            cont = input("Would you like to continue? (y/n) ")
            if cont.lower() == 'y' :
                break
            elif cont.lower() == 'n' :
                print("Exiting...")
                exit()
            else:
                print("Please enter y or n")

    elif choice == '3':
        print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
        while True:
            cont = input("Would you like to continue? (y/n) ")
            if cont.lower() == 'y' :
                break
            elif cont.lower() == 'n' :
                print("Exiting...")
                exit()
            else:
                print("Please enter y or n")

    elif choice == '4':
        print(f"{num1} / {num2} = {calculator.division(num1, num2)}")
        while True:
            cont = input("Would you like to continue? (y/n) ")
            if cont.lower() == 'y' :
                break
            elif cont.lower() == 'n' :
                print("Exiting...")
                exit()
            else:
                print("Please enter y or n")
    
    elif choice == 5:
        print("Exiting the program.")
        exit()

    else:
        print("Invalid choice. Exiting.")
        break