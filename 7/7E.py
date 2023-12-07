from enum import Enum
from functools import cmp_to_key


class HandType(Enum):
    FIVEKIND = 1 << 5
    FOURKIND = 1 << 4
    FULLHOUSE = 1 << 3
    THREEKIND = 1 << 2
    TWOPAIR = 1 << 1
    ONEPAIR = 1 << 0
    HIGHCARD = 0


def GetHandType(hand):
    cardsMap = {}
    for i, c in enumerate(hand):
        if c != 1:
            cardsMap = {hand[0]: 1}
            hand[0], hand[i] = hand[i], hand[0]
            break
    jokers = 0
    for c in hand[1:]:
        if c in cardsMap:
            if c != 1:
                cardsMap[c] += 1
            else:
                jokers += 1
        else:
            cardsMap[c] = 1
    sortedHand = list({k: v for k, v in sorted(cardsMap.items(), key=lambda item: item[1], reverse=True)}.items())
    sortedHand[0][1] += jokers
    if sortedHand[0][1] == 5:
        return HandType.FIVEKIND
    if sortedHand[0][1] == 4:
        return HandType.FOURKIND
    if sortedHand[0][1] == 3:
        if sortedHand[1][1] == 2:
            return HandType.FULLHOUSE
        if sortedHand[1][1] == 1:
            return HandType.THREEKIND
    if sortedHand[0][1] == 2:
        if sortedHand[1][1] == 2:
            return HandType.TWOPAIR
        if sortedHand[1][1] == 1:
            return HandType.ONEPAIR
    return HandType.HIGHCARD


def IsHandStronger(handA, handB):
    if handA["handType"].value > handB["handType"].value:
        return 1
    if handB["handType"].value > handA["handType"].value:
        return -1
    if handA["handType"].value == handB["handType"].value:
        for i in range(5):
            if handA["cards"][i] > handB["cards"][i]:
                return 1
            if handA["cards"][i] < handB["cards"][i]:
                return -1
    return 0


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    total = 0
    hands = []
    for line in Lines:
        cardPlay = line.split(" ")
        hand = []
        for card in cardPlay[0]:
            if card == "T":
                hand.append(10)
            elif card == "J":
                hand.append(1)
            elif card == "Q":
                hand.append(12)
            elif card == "K":
                hand.append(13)
            elif card == "A":
                hand.append(14)
            else:
                hand.append(int(card))
        handType = GetHandType(hand)
        hands.append({"cards": hand, "bid": int(cardPlay[1].strip()), "handType": handType})
    sortedHands = sorted(hands, key=cmp_to_key(IsHandStronger))

    total = 0
    for i, s in enumerate(sortedHands):
        total += s["bid"] * (i + 1)
    print(total)