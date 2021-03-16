#game_db.py
from uuid import uuid4
from game import game
import asyncio

class GameDB():

# Database to create a game.

    def __init__(self):
        self.current_games= {}

    async def add_game(self, num_players:int):
        await asyncio.sleep(0.05)
        game_id= str(uuid4())
        game_dict = self.current_games
        game_dict[game_id] = game(num_players)
        return game_id
