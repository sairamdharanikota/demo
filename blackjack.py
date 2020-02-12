import Card
import os
import sys
def main():
    """ todo:Clear the screen """
    os.system("cls")

    print("Welcome to blackjack!")
    print("Press 1 to start a game!")
    print("Press 2 to exit")
    prompt = input(int(""))
    while (prompt):
        if prompt == 1:
            start_game()
        elif prompt == 2:
           print("about to exit")
           break
        else:
            print("please enter 1 or 2")
def start_game():
    deck = Card.Deck()
    deck.shuffle()
    player = Card.Hand()
    print(player)
    dealer = Card.Hand()
    give_card(dealer, 2)
    show_card(player, 2)
    show_card(dealer, 1)
 # explain if you need total as a function
    player_win = blackjack_check(player)
    dealer_win = blackjack_check(dealer)
    while (player_win):
        if player_c(player):
            #dealer_game()
        else:
            give_card(player, 1)
            player_win = blackjack_check(player)
            if player_loss():
                dealer_win = 1
                break

    if player_win:
        print("Yay! you won")
    elif dealer_win:
        print("Yay! you lost!")
    main()


def player_loss(someplayer):
    """Bool : Check total value of the cards and if > 21 return 0 """
    if someplayer.rank

def player_c(someplayer):
    print("Do you want to Hit or Stay")
    print("Press 0 for Hit ")
    print("Press 1 to stay ")
    if choice == 0:
        hit(player_c)
        while total(dealer) < 17:
            hit(dealer)
            score(dealer, player)
            start_game()

    return (input())


def show_card(somecard, count):
    """ None : wite code to print card based on count """


def give_card(somecard, count):
    """ None : write code to give card """
       somecard.remove_card(count)

def total(somecard):
    """ Int : write code to get a card and return a total"""


def blackjack_check(someplayer):
    """ Bool : code to check blackjack """


if __name__ =="__main__":
    main()