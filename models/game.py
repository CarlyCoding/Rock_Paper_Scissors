from models.player import Player

class Game():

        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2

        def who_wins(self):
            if self.player1.choice == self.player2.choice:
                return None

            if self.player1.choice == "Rock" and self.player2.choice == "Scissors":
                return (f'{self.player1.name} wins! {self.player1.name} chose Rock, beating paper!')

            if self.player1.choice == "Paper" and self.player2.choice == "Rock":
                return (f'{self.player1.name} wins! {self.player1.name} chose Paper, beating Rock!')

            if self.player1.choice == "Scissors" and self.player2.choice == "Paper":
                return (f'{self.player1.name} wins! {self.player1.name} chose Scissors, beating Paper!')

            # By ruling all the above situations out the only other outcome would be P2 winning. Not indented to keep
            # outside the if. 
            return (f'{self.player2.name} wins!')

# Notes to improve in future after testing:

# -If player two wins it doesn't return a formatted string as I have not yet coded this- it defaults to the P2 win code.  
# -Flask has issues with the 'none' aka draw result. This requires reworking. 
# -An alternative design choice would be a welcome page with a button to take to the game & result with PC opponent using a loop/ random func.
# I would have coded in lower case for my css and html.
# The URL is case sensitive for RPS choice- would add if == lower case option too. 



