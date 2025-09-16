#CALCULATOR (Simple)
#Basic arithmetic operations: addition, subtraction, multiplication, division

#definitions
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
    
    def get_two_numbers(self):
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                return num1, num2
            except ValueError:
                print("Invalid Input! Please input the correct numbers")
                continue

    def ask_continue(self):
        while True:
            cont = input("Would you like to continue? (y/n) ")
            if cont.lower() == 'y' :
                return True
            elif cont.lower() == 'n' :
                print ("Exiting...")
                exit()
            else :
                print ("Please enter y or n")
    
calculator = Calculator()

#Arithmetic operations menu
Operations = {
'1': 'Addition',
'2': 'Subtraction',
'3': 'Multiplication',
'4': 'Division',
'5': 'Exit the calculator'
}

#The actual operation
while True:
    print("\nMenu:")
    for  key, value in Operations.items():
        print(f"{key}: {value}")
    
    choice = input("Choose an Option: ")

    if choice == '1':
        num1, num2 = calculator.get_two_numbers()

        print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
       
        calculator.ask_continue()

    elif choice == '2':
        num1, num2 = calculator.get_two_numbers()

        print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")

        calculator.ask_continue()

    elif choice == '3':
        num1, num2 = calculator.get_two_numbers()

        print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")

        calculator.ask_continue()

    elif choice == '4':
        num1, num2 = calculator.get_two_numbers()
  
        try:
            print(f"{num1} / {num2} = {calculator.division(num1, num2)}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            continue

        calculator.ask_continue()
    
    elif choice == '5':
        print("Exiting the program.")
        exit()

    else:
        print("Invalid choice. Please Try Again.")
        break

