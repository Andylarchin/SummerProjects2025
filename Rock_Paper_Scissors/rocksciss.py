
from matplotlib.pylab import randint

Choices = ['rock','paper','scissors'];


def get_user_choice():
    userChoice = input('Choose which object do you want to choose: ').lower();
    while userChoice not in Choices:
        print('Invalid choice! Try again!')
        userChoice = input('Choose which object do you want to choose: ').lower();
    return userChoice;

def get_computer_choice():
    return Choices[randint(0,3)]


def determine_winner(user,computer):
    if user == computer:
        return "It's a tie choose again!"
    if(user == 'rock' and computer == 'scissors'):
        return "User wins!"
    elif(user == 'paper' and computer == 'rock'):
        return "User wins!"
    elif(user == 'scissors' and computer == 'paper'):
        return 'User wins!'
    else:
        return 'Computer wins!'

def play():
   print("Welcome to the rock paper scissors game.");
   while True:
       userFinalChoice = get_user_choice();
       computerFinalChoice = get_computer_choice()

       print(f'\n You chose: {userFinalChoice}');
       print(f'\n Computer chose: {computerFinalChoice}');
       print(f'\n{determine_winner(userFinalChoice,computerFinalChoice)}');

       play_again = input('Do you want to play again? y/n: ').lower();
       if play_again != 'y':
           print('Thanks for playing!')
           break; 

play();

