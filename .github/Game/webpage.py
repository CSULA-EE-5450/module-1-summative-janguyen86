#webpage.py
import uvicorn
from fastapi import FastAPI, HTTPException, status
from game import game
from game_db import GameDB

#Creates Fast API for the game

game = game()
GameDB = GameDB()
app = FastAPI(title="Bau Cua Tom Ca",
              description="Multiplayer Betting Game by Janice the Menace")

async def get_game(game_id: str) -> game:

    the_game = await GameDB.get_game(game_id)
    if the_game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Game {game_id} not found.")
    return the_game

@app.get("/")
async def home():
    return {"message" : "Welcome to Bầu Cua Tôm Cá"}

@app.get("/game/create/{num_players:int}")
async def create_game(num_players:int):
    game_id = await GameDB.add_game(num_players)
    return {"success": True, "game_id":game_id}

@app.post("/game/{game_id}/rollingdice")
async def rolling_dice(game_id: str):
    list_dice, num_list= game.round_dice()
    return {"success": True, "list_dice": list_dice}

@app.post('/game/{game_id}/{player_id}/winloss')
async def amount_win_loss(game_id: str, player_id: int):
    winloss = game.get_win_loss(player_id)
    return {"success": True, "winnings": winloss}

@app.get('/game/{game_id}/{player_id}/new_total')
async def new_total(game_id: str, player_id: int):
    round = game._round
    winloss = game.get_player_total(player_id, round)
    return {"success": True, "winnings": winloss}

@app.get("/game/{game_id}/winner")
async def get_winner(game_id:str):
    winner = game.who_da_winner()
    return {"success": True, "winner":winner}

if __name__ == '__main__':
    uvicorn.run('webpage:app', port=8000, log_level='info', reload=True)


