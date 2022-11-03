import random

#Zain Pilcher
#11/3/22
#Program for playing blackjack

def get_card():
    # function for drawing the card
    return(random.randint(1,10))

def get_winner(user_total, dealer_total):
    """
    if the user's total is less than the dealer's at the end or the user busts, then you loser
    if the dealer's total is less than the user's at the end or he busts, then he is loses
    if you both get the same amount then it's a tie
    :param user_total: the user's total amount from the cards
    :param dealer_total: the dealer's total amount from the crads
    :return: The result when the total's are finalized
    """
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
    """
    adds the first two cards that are drawn, and gives the user four chances to draw more cards to try to get 21
    the dealer usually plays it safe by not drawing if the amount is 16 or more
    If the user or dealer gets 21, they get a blackjack
    """
    get_card()
    first = get_card()
    get_card()
    second = get_card()
    user_tot = first + second
    print("You drew the", first, "and the", second)
    print("Your total is now:", user_tot)
    print("")
    y_or_n = str(input("Draw another card? "))
    if y_or_n == "y":
        third = get_card()
        user_tot = first + second + third
        print("You drew the", third)
        print("Your total is now", user_tot)
        if user_tot < 21:
            y_or_n_second = str(input("Draw another card? "))
            if y_or_n_second == "y":
                fourth = get_card()
                user_tot = first + second + third + fourth
                print("You drew the", fourth)
                print("Your total is now", user_tot)
                if user_tot < 21:
                    y_or_n_third = str(input("Draw another card? "))
                    if y_or_n_third == "y":
                        fifth = get_card()
                        user_tot = first + second + third + fourth + fifth
                        print("You drew the", fifth)
                        print("Your total is now", user_tot)
                        if user_tot < 21:
                            y_or_n_fourth = str(input("Draw another card? "))
                            if y_or_n_fourth == "y":
                                sixth = get_card()
                                user_tot = first + second + third + fourth + fifth + sixth
                                print("You drew the", sixth)
                                print("Your total is now", user_tot)
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
    print("The dealer drew the", dealer_first, "and the", dealer_second)
    print("The dealer's total is", dealer_tot)
    if dealer_tot < 16:
        dealer_third = get_card()
        dealer_tot = dealer_first + dealer_second + dealer_third
        print("")
        print("The dealer drew the", dealer_third)
        print("The dealer's total is", dealer_tot)
        if dealer_tot < 16:
            dealer_fourth = get_card()
            dealer_tot = dealer_first + dealer_second + dealer_third + dealer_fourth
            print("")
            print("The dealer drew the", dealer_fourth)
            print("The dealer's total is", dealer_tot)
            if dealer_tot < 16:
                dealer_fifth = get_card()
                dealer_tot = dealer_first + dealer_second + dealer_third + dealer_fourth + dealer_fifth
                print("")
                print("The dealer drew the", dealer_fifth)
                print("The dealer's total is", dealer_tot)
            elif dealer_tot > 21:
                print("Bust")
        elif dealer_tot > 21:
            print("Bust")
    else:
        print("The dealer holds")
    print("")
    print(user_tot, "-", dealer_tot)
    """
    if the user gets 21 then the user blackjacks
    if the dealer gets 21 then the dealer blackjacks
    """
    if dealer_tot == 21:
        print("Dealer blackjack")
    if user_tot == 21:
        print("User blackjack")
    (get_winner(user_tot, dealer_tot))

main()
