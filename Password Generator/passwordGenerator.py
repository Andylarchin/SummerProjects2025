from matplotlib.pylab import randint

print("Welcome to the Password Generator!")

letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
              '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '|']

while True:
    password = ''
    passwordLength = int(input("Enter the desired password length: "))

    while passwordLength > 25:
        print("Your password length is too long, choose another amount!")
        passwordLength = int(input("Enter the desired password length: "))

    for x in range(passwordLength):
        listChoice = randint(1, 4)
        if listChoice == 1:
            letter = randint(0, len(letterList) - 1)
            password += letterList[letter]
        elif listChoice == 2:
            number = randint(0, len(numberList) - 1)
            password += numberList[number]
        elif listChoice == 3:
            symbol = randint(0, len(symbolList) - 1)
            password += symbolList[symbol]

    print(f'Your generated password is: {password}')

    another = input("Do you want to generate another password? (y/n): ").strip().lower()
    if another != 'y':
        print("Goodbye!")
        break
