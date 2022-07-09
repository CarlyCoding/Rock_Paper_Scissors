from models.player import Player

class Game():

        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2

        def who_wins(self):
            if self.player1.choice == self.player2.choice:
                return None

            if self.player1.choice == "Rock" and self.player2.choice == "Scissors":
                return ("{player1} wins!".format)

            if self.player1.choice == "Paper" and self.player2.choice == "Rock":
                return ("{player1} wins!".format)

            if self.player1.choice == "Scissors" and self.player2.choice == "Paper":
                return ("{player1} wins!".format)

            # By ruling all the above situations out the only other outcome would be P2 winning. Not indented to keep
            # outside the if. 
            return ("{player2} wins!".format)



