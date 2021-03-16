#game.py
import logging
from typing import List, Union, Tuple
import random
from dataclasses import dataclass
import numpy as np

@dataclass
class dice(object):
    pic: str

# Creates Dice objects that have the 6 characters as faces.

    @staticmethod
    def _change_to_pic(num)-> str:
        """
        Converts an int to 1 of the 6 characters.
        :param num: Random number generated
        :return:
        """
        if num == 0:
            return "Fish"
        if num == 1:
            return "Shrimp"
        if num == 2:
            return "Crab"
        if num == 3:
            return "Rooster"
        if num == 4:
            return "Bottle Gourd"
        if num == 5:
            return "Deer"
    def __str__(self):
        return f'{self._change_to_pic(self.number)}'

class game(object):

    def __init__(self, num_players: int = 1):

        self._num_players = num_players
        self._pic = ("Fish", "Shrimp", "Crab", "Rooster", "Bottle Gourd", "Deer")
        self._player_total= [[100] for _ in range(num_players)]
        self._player_win_loss = [[] for _ in range(num_players)]
        self._player_loser = [False for _ in range (num_players)]
        self._round = 0
        self._amounts = [[] for _ in range(num_players)]
        self._bets = [[] for _ in range(num_players)]
        self._dice = []

    def roll_dice(self):
        """
        Rolls 1 die and returns dice object.
        :return: Dice object with Pic and corresponding number
        """
        chosen_num = random.randint(0, 5)
        return dice(chosen_num), chosen_num

    def round_dice(self):
        """
        Rolls 3 dice and returns list of 3 dice objects.
        :return: List of 3 dice and list of corresponding numbers for that round
        """
        dice1, num1 = self.roll_dice()
        dice2, num2 = self.roll_dice()
        dice3, num3 = self.roll_dice()
        return [dice1, dice2, dice3], [num1, num2, num3]

    def calculate_player_win_loss(self, bet: int, amount: float, player_id: int, dice_list: List[dice]) :
        """
        Calculates how much a player loses or wins each round and appends it to self._player_win_loss[player_id]
        :param bet: What item the player bet on
        :param amount: Amount the player bet
        :param player_id: Player ID
        :param dice_list: List of dice objects
        :return: Amount player lose or won this round
        """
        amount_won_loss = 0
        if dice(bet) in dice_list:
            repeat = dice_list.count(dice(bet))
            amount_won_loss = amount * repeat
        else:
            amount_won_loss = -amount

        player_wl = self._player_win_loss[player_id]
        player_wl.append(amount_won_loss)
        return amount_won_loss

    def get_current_bet(self, player_id):
        """
        Get the bet for that round for the player.
        :param player_id: Player_ID
        :return: Current bet
        """
        bet_list = self._bets[player_id]
        round = len(bet_list)-1
        current_bet = bet_list[round]
        return current_bet

    def get_current_amount(self, player_id):
        amount_list = self._amounts[player_id]
        round = len(amount_list)-1
        current_amount = amount_list[round]
        return current_amount

    def get_win_loss(self, player_id)-> float:
        '''
        Returns how much lossed or won by a player in a specified round.
        :param player_id: Player ID
        :return: How much a player lossed or won in a specified round
        '''
        all_winnings = self._player_win_loss[player_id]
        latest_round = len(all_winnings)-1
        round_winnings = all_winnings[latest_round]
        return round_winnings

    def get_player_total(self, player_id, round) -> float:
        """
        Returns player total amount of money for specified round
        :param player_id: Player ID
        :param round: Current round
        :return: Player total amount of money after specified round
        """
        all_total = self._player_total[player_id]
        total = all_total[round]
        return total

    def updated_player_total(self,  player_id: int) -> float:
        """
        Updates the player total of money after current round executed
        :param player_id: Player ID
        :return: Updated total
        """
        current_total = self._player_total[player_id]
        round_win_loss = self._player_win_loss[player_id]
        new_total = current_total[len(current_total)-1]+ round_win_loss[len(round_win_loss)-1]

        current_total.append(new_total)
        return new_total

    def determine_loser(self, player_id: int):
        """
        Determine which players loss all their money and cannot play anymore.
        :param player_id: Player ID
        """
        current_total = self._player_total[player_id]
        player_current_total = current_total[len(current_total)-1]

        if player_current_total <= 0:
            self._player_loser[player_id] = True


    def who_da_winner(self) -> int:
        """
        Finds the winner from array of players.
        :return: Winner of the Game
        """
        is_player_losing = self._player_loser

        for player in is_player_losing:
            if player == False:
                winner = is_player_losing.index(player)
        return winner


