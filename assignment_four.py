import random

def get_card():
    return(random.randint(1,10))

def get_winner(user_total, dealer_total):
    if user_total > 21 and dealer_total < 21:
        return(print("You busted"))
    elif user_total > 21 and dealer_total > 21:
        return(print("You both busted"))
    elif dealer_total > 21:
        return(print("Dealer busted"))
    elif dealer_total > user_total:
        return(print("Loser"))
    elif user_total > dealer_total:
        return(print("You win!!!"))
    elif user_total == dealer_total:
        return(print("Tie"))
def main():
    get_card()
    first = get_card()
    get_card()
    second = get_card()
    user_tot = first + second
    print("You drew the", first, "and the", second)
    print("Your total is:", user_tot)
    print("")
    y_or_n = str(input("Draw another card? "))
    if y_or_n == "y":
        third = get_card()
        user_tot = first + second + third
        print("Your total is", user_tot)
        if user_tot < 21:
            y_or_n_second = str(input("Draw another card? "))
            if y_or_n_second == "y":
                fourth = get_card()
                user_tot = first + second + third + fourth
                print("Your total is", user_tot)
                if user_tot < 21:
                    y_or_n_third = str(input("Draw another card? "))
                    if y_or_n_third == "y":
                        fifth = get_card()
                        user_tot = first + second + third + fourth + fifth
                        print("Your total is", user_tot)
                        if user_tot < 21:
                            y_or_n_fourth = str(input("Draw another card? "))
                            if y_or_n_fourth == "y":
                                sixth = get_card()
                                user_tot = first + second + third + fourth + fifth + sixth
                                print("Your total is", user_tot)
                            elif y_or_n_third == "n":
                                print("Your total is", user_tot)
                    elif y_or_n_third == "n":
                        print("Your total is", user_tot)
            elif y_or_n_second == "n":
                print("Your total is", user_tot)
    elif y_or_n == "n":
        print("Your total is", user_tot)
    print("")
    dealer_first = get_card()
    dealer_second = get_card()
    dealer_tot = dealer_first + dealer_second
    if dealer_tot < 16:
        dealer_third = get_card()
        dealer_tot = dealer_first + dealer_second + dealer_third
        if dealer_tot < 12:
            dealer_fourth = get_card()
            dealer_tot = dealer_first + dealer_second + dealer_third + dealer_fourth
            print("The dealer has the", dealer_first, "the", dealer_second, "the", dealer_third, "and the", dealer_fourth)
        else:
            print("The dealer has the", dealer_first, "the", dealer_second, "and the", dealer_third)
    else:
        print("The dealer has the", dealer_first, "and the", dealer_second)
    print("The dealer's total is", dealer_tot)
    print("")
    (get_winner(user_tot, dealer_tot))

main()