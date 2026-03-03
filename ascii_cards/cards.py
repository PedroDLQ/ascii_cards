def print_card(rank, suit, is_faceup=True):
    """
    function to print an ASCII representation of a single playing card (face down).

    Args:
        rank (str): The rank of the card ('2'-'10', 'J', 'Q', 'K', 'A', 'JK').
        suit (str): The suit of the card ('♠', '♥', '♦', '♣', '★', '☆').
        is_faceup (bool): Checks if the card is face up or face down. Optional, defaults to "True".
    """
    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"

    if not is_faceup:
        back_design = "│ ░░░░░░░ │"

        print(top)
        print(back_design)
        print(back_design) 
        print(back_design)
        print(back_design)
        print(back_design)
        print(bottom)

        return

    if rank == "10" or rank == "JK":  # Ten and Joker are the only ranks with two digits/letters
        rank_right = rank
        rank_left = rank
    else:
        rank_right = rank + " "
        rank_left = " " + rank

    suit_line = f"│    {suit}    │"
    rank_line_left = f"│{rank_left}       │"
    rank_line_right = f"│       {rank_right}│"

    print(top)
    print(rank_line_left)
    print(side)
    print(suit_line)
    print(side)
    print(rank_line_right)
    print(bottom)


def get_card(rank, suit, is_faceup=True):
    """
    function to get an ASCII representation of a single playing card (face down).

    Args:
        rank (str): The rank of the card ('2'-'10', 'J', 'Q', 'K', 'A', 'JK').
        suit (str): The suit of the card ('♠', '♥', '♦', '♣', '★', '☆').
        is_faceup (bool): Checks if the card is face up or face down. Optional, defaults to "True".

    Return:
        -> (str): the card in str format
    """
    top = "┌─────────┐\n"
    bottom = "└─────────┘\n"
    side = "│         │\n"

    card = []

    if not is_faceup:
        back_design = "│ ░░░░░░░ │\n"

        card.append(top)
        card.append(back_design)
        card.append(back_design)
        card.append(back_design)
        card.append(back_design)
        card.append(back_design)
        card.append(bottom)

        return "".join(card)

    if rank == "10" or rank == "JK":  # Ten and Joker are the only ranks with two digits/letters
        rank_right = rank
        rank_left = rank
    else:
        rank_right = rank + " "
        rank_left = " " + rank

    suit_line = f"│    {suit}    │\n"
    rank_line_left = f"│{rank_left}       │\n"
    rank_line_right = f"│       {rank_right}│\n"

    
    card.append(top)
    card.append(rank_line_left)
    card.append(side)
    card.append(suit_line)
    card.append(side)
    card.append(rank_line_right)
    card.append(bottom)

    return "".join(card)


def main():
    cards = [("A", "♠"), ("10", "♥"), ("K", "♦"), ("7", "♣"), ("JK", "☆"), ("JK", "★")]
    get_cards_print = []
    for rank, suit in cards:
        print_card(rank, suit)
        print()  # Add a space between cards

        get_cards_print.append(get_card(rank, suit))

    print("".join(get_cards_print))

    print_card("10", "󰣑", False)
    print(get_card("10", "󰣑", False))

if __name__ == "__main__":
    main()
