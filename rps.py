import random


class game:

    def __init__(self, rounds, userCount, compCount):
        self.userMatchIn = rounds
        self.userCount = userCount
        self.compCount = compCount
        self.item = []
        self.item.append("rock")
        self.item.append("paper")
        self.item.append("scissors")

    def rock(self):
        print("You chose rock")
        self.compPlay = random.choice(self.item)
        print("Comp plays " + self.compPlay)

        if self.compPlay == self.item[0]:
            print("\nDRAW")
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

        if self.compPlay == self.item[1]:
            print("\nComputer wins!!!")
            self.compCount += 1
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

        if self.compPlay == self.item[2]:
            print("\nYou win!!!")
            self.userCount += 1
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

    def paper(self):
        print("You chose paper")
        self.compPlay = random.choice(self.item)
        print("Comp plays " + self.compPlay)

        if self.compPlay == self.item[0]:
            print("\nYou win!!!")
            self.userCount += 1
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

        if self.compPlay == self.item[1]:
            print("\nDRAW")
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

        if self.compPlay == self.item[2]:
            print("\nComputer wins!!!")
            self.compCount += 1
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

    def scissors(self):
        print("You chose scissors")
        self.compPlay = random.choice(self.item)
        print("Comp plays " + self.compPlay)

        if self.compPlay == self.item[0]:
            print("\nComputer wins!!!")
            self.compCount += 1
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

        if self.compPlay == self.item[1]:
            print("\nYou win!!!")
            self.userCount += 1
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))

        if self.compPlay == self.item[2]:
            print("\nDRAW")
            print("You: {}\t Computer: {}".format(self.userCount, self.compCount))


def main():
    userMatchIn = int(input("Enter the number of matches you want to play: "))
    rps = game(userMatchIn, 0, 0)
    for rpsgame in range(userMatchIn):
        userOptIn = int(input("\nEnter 1 for rock, 2 for paper OR 3 for scissors:"))
        if userOptIn == 1:
            rps.rock()
        elif userOptIn == 2:
            rps.paper()
        elif userOptIn == 3:
            rps.scissors()
        else:
            print("Invalid option entered. Please try again.")


if __name__ == "__main__":
    main()
