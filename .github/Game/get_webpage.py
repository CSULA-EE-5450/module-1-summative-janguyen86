import requests

# Uses requests to retrieve the Fast API created in webpage.py

class Get_the_Game():

    def get_create_game(self, num: int):
        num_param = {"num_player" : num}
        ge = requests.get("http://localhost:8000/game/create/", params = num_param)

    def post_rolling_dice(self, game_id: str):
        game_param = {"game_id" : game_id}
        pos = requests.post("http://localhost:8000/game/{game_id}/rollingdice")

    def post_amount_win_loss(self, game_id: str, player_id: int):
        game_param = {"game_id": game_id, "player_id": player_id}
        pos = requests.post("http://localhost:8000/game//game/{game_id}/{player_id}/winloss")

    def get_new_total(self, game_id: str, player_id: int):
        game_param = {"game_id": game_id, "player_id": player_id}
        ge = requests.post("http://localhost:8000/game//game/{game_id}/{player_id}/new_total")

    def get_winner(self, game_id: str):
        game_param = {"game_id": game_id}
        pos = requests.post("http://localhost:8000/game//game/{game_id}/winner")

if __name__ == '__main__':
    Get_the_Game().run()
