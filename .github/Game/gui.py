#gui.py

from kivy.uix.image import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from game import game

# Creates Window Manager:
# Home Page: Screen where user inputs how many players
# Game Page: Interactive game page. User input amount they want to bet and click on button of character
# they want to place a bet on.
#Dice Page: Rolls the dice after player placed their bets. Also shows total amount of money
#each player as left. Returns back to Game page or moves onto Winner page
#Loser Page: Shows up when player total reaches 0.
# Winner Page: Screen appears when there is a winner. Has option to return to
# home page to restart a new game.

#***Note: Have to enter an int for number of players in the Home Page, and bet in Game Page

game = game()

class Home_Page(Screen):
    """
    Home page: Initializes game with inputting number of players.
    """
    num_player = ObjectProperty(None)

class Game_Page(Screen):
    """
    Game Page is where the player enters amount to bet and what to bet on
    """
    amount = ObjectProperty(None)

    def __int__(self):
        self.player_id = 0 #fix with requests
        self.round = 0
        self.current_bet = 0

    def press_fish(self):
        """
        Button that player can click to chose "Fish" as their bet.
        :return: None
        """
        amount = self.ids.amount
        self.current_bet = 0

    def press_shrimp(self):
        """
        Button that player can click to chose "Shrimp" as their bet.
        :return: None
        """
        amount = self.ids.amount
        self.current_bet = 1

    def press_crab(self):
        """
        Button that player can click to chose "Crab" as their bet.
        :return: None
        """
        amount = self.ids.amount
        self.current_bet = 2

    def press_rooster(self):
        """
        Button that player can click to chose "Rooster" as their bet.
        :return: None
        """
        amount = self.ids.amount
        self.current_bet = 3

    def press_gourd(self):
        """
        Button that player can click to chose "Bottle Gourd" as their bet.
        :return: None
        """
        amount = self.ids.amount
        self.current_bet = 4

    def press_deer(self):
        """
        Button that player can click to chose "Deer" as their bet.
        :return: None
        """
        amount = self.ids.amount
        self.current_bet = 5

    def committed(self):
        """
        Once player clicks the enter button, the bet and amount betted will be used to calculate
        the winnings for that round.
        :return: None
        """
        amount_list = game._amounts
        amount_list.append(self.ids.amount)
        bet_list = game._bets
        bet_list.append(self.current_bet)


class Dice_Page(Screen):
    """
    Shows what the 3 dice are for that round and display player's winnings/loss for that round and
    updated total.
    """
    def __int__(self):
        self.player_id = 0  #not suppose to be fixed value
        self.round = 0      #not suppose to be fixed value
        self.winnings = 0

    def roll_dice(self):
        list_dice, num_list = game.round_dice()
        banana_split = game._dice
        banana_split = list_dice
        list_dice_str = []
        for num in num_list:
            if num == 0:
                list_dice_str.append("Fish")
            if num == 1:
                list_dice_str.append("Shrimp")
            if num == 2:
                list_dice_str.append("Crab")
            if num == 3:
                list_dice_str.append("Rooster")
            if num == 4:
                list_dice_str.append("Bottle Gourd")
            if num == 5:
                list_dice_str.append("Deer")
        # player_id = 0
        list_dice_str1 = ", ".join(list_dice_str)
        # current_bet = game.get_current_bet(player_id)
        # current_amount= game.get_current_amount(player_id)
        # winnings = game.calculate_player_win_loss(current_bet, current_amount, player_id, list_dice)
        # self.winnings = winnings
        return list_dice_str1

    def player_winningsloss(self):
        # return str(self.winnings())
        return "Error: Not Working Correctly"

    def get_total(self):
        # total = game.updated_player_total(self.player_id)
        # return str(total)
        return "Error 2.0: Everything's falling apart like my life"

class Winner_Page(Screen):
    """
    Displays the winner. Has option to return to Home Page to start another game.
    """
    def get_winner(self):
        winner = game.who_da_winner()
        return str(winner)

class Loser_Page(Screen):
    """
    Pops up when Player total reaches 0.
    """
    pass

class Page_manager(ScreenManager):
    pass

kv = Builder.load_file('game.kv')

class Game(App):
    def build(self):
        return kv

if __name__ == '__main__':
    Game().run()

#Needs fixing:
#-Currently hard coded player ID and round to 0 in Dice_Page, need to change depending on who is playing
#-Commented out code in Dice_Page b/c pops up error, need to fix so game plays correctly and
#calculates correct winner and updates total
#-Currently rolling the dice in Dice_Page doesn't reset itself even when making a new bet(i.e. when player presses "Continue Playing")
#-Trigger loser page to appear when player reaches 0, currently set to appear whenever players presses "End Game"
#cause if I can't get this code to work, everyone's gonna be a loser
#-Make the GUI prettier with images so I don't disappoint my ancestors
