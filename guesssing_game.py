#random number  generation game using python numpy
import numpy as np
import random
n=np.random.randint(1,20,1)
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
name=input('enter your name: ')
print('welcome to the GAME LOFT--> ', name)
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<n: 
        print("you enter less number please input greater number.\n")
    elif guess_number>n:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1
if (number_of_guesses>9):
    print(f"game is over...you crossed the guesses limit !!your guessed number is {n}")    
    


