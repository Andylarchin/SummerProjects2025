isStillWorking = True; 
print('Welcome to the CLI Calculator!')

while isStillWorking == True:
    firstNumber = input("Enter your first number: ");
    secondNumber = input("Enter your second number: ");
    operator = input("Enter the operator (+, -, *, /, ^): ");
    
    if operator == '+':
        result = float(firstNumber) + float(secondNumber);
        print("----------------------------------------------------------")
        print(f"The result of {firstNumber} + {secondNumber} is: {result}");
    elif operator == '-':
        result = float(firstNumber) - float(secondNumber);
        print("----------------------------------------------------------")
        print(f"The result of {firstNumber} - {secondNumber} is: {result}");
    elif operator == '*':
        result = float(firstNumber) * float(secondNumber);
        print("----------------------------------------------------------")
        print(f"The result of {firstNumber} * {secondNumber} is: {result}");
    elif operator == '/':
        if float(secondNumber) == 0:
            print("----------------------------------------------------------")
            print("Error: Division by zero is not allowed.");
        else:
            result = float(firstNumber) / float(secondNumber);
            print("----------------------------------------------------------")
            print(f"The result of {firstNumber} / {secondNumber} is: {result}");
    elif operator == '^':
        result = float(firstNumber) ** float(secondNumber);
        print("----------------------------------------------------------")
        print(f"The result of {firstNumber} ^ {secondNumber} is: {result}");

    print("Do you want to perform another calculation? (yes/no): ");
    if input().lower() != 'yes':
        isStillWorking = False;
        print("Thank you for using the CLI Calculator! Goodbye!");
      
    