from random import randrange
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Guess")
print(ascii_banner, end="")
number = int(input("Choose the Number from in Range you want (minimum - 10,n):- "))
comp = randrange(number)
def game():
    guess = int(input("Guess the Number:- "))
    if guess == comp:
        print(f"You Win {comp} was the number")
        quit()  
    print("smaller" if guess > comp else "larger")
while True:
    game()