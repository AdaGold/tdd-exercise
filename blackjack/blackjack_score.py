VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):

    score = 0

    if len(hand) > 5:
        return "Invalid"
    
    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid"
        elif card in ['Jack', 'Queen', 'King']:
            score += 10
        elif card == "Ace":
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += card

        if score > 21:
            return "Bust"

    return score

