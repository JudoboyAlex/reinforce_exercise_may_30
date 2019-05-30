def select_cards(possible_cards, hand):

    for current_card in possible_cards:
            print("Do you want to pick up {}?".format(current_card))
            answer = input()
            if answer.lower() == 'y':
                hand.append(current_card)
                if len(hand) == 3:
                    return hand

            
available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = select_cards(available_cards, [])
display_hand = "\n".join(new_hand)
print("Your new hand is: \n{}".format(display_hand))
            

# Do you want to pick up queen of spades?y
# Do you want to pick up 2 of clubs?n
# Do you want to pick up 3 of diamonds?n
# Do you want to pick up jack of spades?y
# Do you want to pick up queen of hearts?y
# Your new hand is: 
# queen of spades
# jack of spades
# queen of hearts

# Make sure the user can't pick up more than three cards.

# Make sure the user must pick up exactly three cards.