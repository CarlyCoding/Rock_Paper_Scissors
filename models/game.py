from models.player import Player

class Game():

        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2

        def who_wins(self):
            if self.player1.choice == self.player2.choice:
                return None
            if self.player1.choice == "Rock":
                if self.player2.choice == "Scissors":
                    return ("{player2} wins!".format)
            if self.player1.choice == "Paper":
                if self.player2.choice == "Rock":
                    return ("{player1} wins!".format)
            if self.player1.choice == "Scissors":
                if self.player2.choice == "Paper":
                    return ("{player1} wins!".format)






# This function will take in 2 players and compare their results, returning a string of the winning player



