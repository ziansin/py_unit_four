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
def main():
    dealer_first = get_card()
    dealer_second = get_card()
    dealer_tot = dealer_first + dealer_second
    get_card()
    first = get_card()
    get_card()
    second = get_card()
    user_tot = first + second
    print("You drew a", first, "and a", second)
    print("Your total is:", user_tot)
    print("")
    y_or_n = str(input("Draw another card? "))
    if y_or_n == "y":
        third = get_card()
        user_tot = first + second + third
        print("Your total is", user_tot)
    elif y_or_n == "n":
        print("Your total is", user_tot)
    print("")
    print("The dealer has a", dealer_first, "and", dealer_second)
    print("The dealer's total is", dealer_tot)
    print("")
    (get_winner(user_tot, dealer_tot))

main()