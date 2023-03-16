
headsCounter = 0
total = 0


def askForInput(headsCounter, total):
    hOrT = input("Throw the coin and enter heads or tails here: ?")
    if(hOrT == "heads"):
        headsCounter += 1
        total += 1
        avgHeads = (headsCounter/total)*100
        print(f"Heads: {round(avgHeads,1)}%")
    elif(hOrT == "tails"):
        total += 1
        avgHeads = (headsCounter/total)*100
        print(f"Heads: {round(avgHeads,1)}%")
    else:
        return
    askForInput(headsCounter, total)

askForInput(headsCounter, total)

