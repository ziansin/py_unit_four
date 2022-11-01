import random
def who_wins(user, computer):
    if user == 3 and computer == 1:
        return(str("The computer wins"))
    elif user == 3 and computer == 2:
        return(str("You win!"))
    elif user == 3 and computer == 3:
        return(str("It is a tie"))
    elif user == 2 and computer == 1:
        return(str("You win!"))
    elif user == 2 and computer == 2:
        return(str("It is a tie"))
    elif user == 2 and computer == 3:
        return(str("The computer wins"))
    elif user == 1 and computer == 1:
        return(str("It is a tie"))
    elif user == 1 and computer == 2:
        return(str("The computer wins"))
    elif user == 1 and computer == 3:
        return(str("You win!"))

def main():
    user_num = int(input("1 for rock, 2 for paper, 3 for scissors: "))
    computer_num = random.randint(1,3)
    print("Computer chose", computer_num)
    print(who_wins(user_num, computer_num))

if __name__ == '__main__':
    main()