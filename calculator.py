while True:
    print("""\nCALCULATOR MENU""")
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Floor Division')
    print('6. Remainder')
    print('0. Exit')
    ch = int(input("Enter your choice: "))
    if ch == 0:
        print("Exiting the calculator. Goodbye!")
        break
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    if ch == 1:
        print("Result:", a + b)
    elif ch == 2:
        print("Result:", a - b)
    elif ch == 3:
        print("Result:", a * b)
    elif ch == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero!")
    elif ch == 5:
        if b != 0:
            print("Result:", a // b)
        else:
            print("Error: Floor division by zero!")
    elif ch == 6:
        if b != 0:
            print("Result:", a % b)
        else:
            print("Error: Modulo by zero!")
    else:
        print("Please enter a valid option.")
