#testing statements

while True:
    try:
        max_num = int(input("Enter a maximum number to count to: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

menu = {
    '1': 'Count to the maximum number',
    '2': 'Count to the maximum number and print even numbers',
    '3': 'Count to the maximum number and print odd numbers',
    '4': 'Exit'
}

#count = 0

while True:
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}: {value}")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        for num in range(max_num + 1):
            print(num)
        while True:
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() == 'y':
                break
            elif cont.lower() == 'n':
                print("Exiting the program.")
                exit()
            else:
                print("Please enter 'y' or 'n'.")
    elif choice == '2':
        for num in range(max_num + 1):
            if num % 2 == 0:
                print(num, "is even")
        while True:
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() == 'y':
                break
            elif cont.lower() == 'n':
                print("Exiting the program.")
                exit()
            else:
                print("Please enter 'y' or 'n'.")
    elif choice == '3':
        for num in range(max_num + 1):
            if num % 2 != 0:
                print(num, "is odd")
        while True:
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() == 'y':
                break
            elif cont.lower() == 'n':
                print("Exiting the program.")
                exit()
            else:
                print("Please enter 'y' or 'n'.")
    elif choice == '4':
        print("Exiting the program.")
        exit ()
    else:
        print("Invalid choice. Please try again.")

