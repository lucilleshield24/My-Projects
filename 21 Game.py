class Player:
    def __init__(self, name):
        self.name = name
    def prompt(self, total):
        self.number = int(input("{}, please choose 1, 2, or 3 to be added to the running total.".format(self.name)))
        total = total + self.number
        total = self.check2(self.number, total)
        print("The total is now {}.".format(total))
        self.check(total)
        return total
    def check(self, total):
        if total == 21:
            print("{} is the winner! Congratulations!".format(self.name))
            exit()
        else:
            return total
    def check2(self, number, total):
        if total > 21:
            print("Sorry, you exceeded 21. Not allowed!")
            total = total - self.number
            self.number = int(input(" Please choose 1, 2, or 3 to be added to the running total without exceeding 21."))
            total = total + self.number
        return total

def quit():
    toquit = input("Do you want to exit the program? If so, type \"yes\". If not, type \"no\".")
    if toquit == "yes":
        print("You have exited the program.")
        exit()
    
Player1 = Player("Player 1")
Player2 = Player("Player 2")
total = 0
while total < 21:
    total = Player1.prompt(total)
    total = Player2.prompt(total)
    quit()