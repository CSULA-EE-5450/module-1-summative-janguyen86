#test_game.py
from unittest import TestCase
from game import game, dice

# Test cases for game.py
class TestGame(TestCase):
    def setUp(self) -> None:
        self.game = game(2)

    def test_round_dice(self):
        list_dice, list_num = self.game.round_dice()
        self.assertEqual(len(list_dice), 3)
        self.assertEqual(len(list_num), 3)

    def test_calculate_player_win_loss(self):
        dice_list = [dice(1), dice(1), dice(3)]
        bet_win = 1
        bet_loss = 4
        amount = 25
        len_player_wl = len(self.game._player_win_loss)
        self.assertEqual(self.game.calculate_player_win_loss(bet_loss, amount, 0, dice_list), -25)
        self.assertEqual(self.game.calculate_player_win_loss(bet_win, amount, 0, dice_list), 50)
        self.assertEqual(len_player_wl, 2)

    def test_update_player_total(self):
        player_id = 0
        self.game._player_total[player_id] = [100]
        self.game._player_win_loss[player_id] = [-25]
        self.assertEqual(self.game.updated_player_total(0), 75)
        self.assertEqual(len(self.game._player_total[player_id]), 2)

    def test_determine_loser(self):
        player_id_win = 0
        player_id_loss = 1
        self.game._player_total= [[100, 75], [100, 0]]
        self.game.determine_loser(0)
        self.game.determine_loser(1)
        self.assertEqual(self.game._player_loser[0], False)
        self.assertEqual(self.game._player_loser[1], True)

    def test_who_da_winner(self):
        self.game._player_loser= [True, True, False, True]
        list_loser = self.game._player_loser
        self.assertEqual(self.game.who_da_winner(), 2)