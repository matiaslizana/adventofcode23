def checkMatches(card):
    matches = 0
    for w in card["winners"]:
        for h in card["have"]:
            if w == h:
                matches += 1
    return matches


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    total = 0
    cards = {}

    print("Reading cards... ")
    for line in Lines:
        numbers = line.split(": ")
        numbersSplit = numbers[1].split("| ")
        winners = numbersSplit[0].replace("  ", " ").strip().split(" ")
        have = numbersSplit[1].replace("  ", " ").strip().split(" ")
        cardNumber = int(numbers[0].strip().replace("Card", ""))
        cards[cardNumber] = []
        cards[cardNumber].append({"num": cardNumber, "copy": False, "winners": winners, "have": have})
        print("\tCard " + str(cardNumber))

    print("Processing cards... ")
    for cNum in cards:
        print("\tCard " + str(cNum))
        for c in cards[cNum]:
            copies = checkMatches(c)
            for m in range(copies):
                cardCopyIndex = cNum + m + 1
                cards[cardCopyIndex].append({"num": cardCopyIndex,
                                             "copy": True,
                                             "winners": cards[cardCopyIndex][0]["winners"],
                                             "have": cards[cardCopyIndex][0]["have"]})

    for cNum in cards:
        for c in cards[cNum]:
            total += 1
    print(total)

