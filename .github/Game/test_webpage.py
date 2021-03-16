#test_webpage.py
import pytest
from fastapi.testclient import TestClient
from webpage import app

# Test cases for webpage.py

@pytest.fixture
def base_client():
    return TestClient(app)

def test_home(base_client):
    response = base_client.get('/')
    assert response.json() == {"message": "Welcome to Bầu Cua Tôm Cá"}

def test_create(base_client):
    response = base_client.get('/game/create/2')
    response_json = response.json()
    assert response_json["success"] is True

@pytest.fixture
def get_game(base_client):
    resp = base_client.get('/game/create/2')
    resp_json = resp.json()
    return resp_json

def test_rolling_dice(get_game, base_client):
    game_id = get_game["game_id"]
    response = base_client.get("/game/{game_id}/rollingdice")
    response_json = response.json()
    assert response_json["success"] is True
    assert len(response_json["list_dice"]) == 3

def test_winloss(get_game, base_client):
    game_id = get_game["game_id"]
    player_id = 0
    response = base_client.post("/game/{game_id}/{player_id}/winloss")
    response_json = response.json()
    assert response_json["success"] is True
    assert len(response_json["winnings"]) == 1

def test_new_total(get_game, base_client):
    game_id = get_game["game_id"]
    player_id = 0
    response= base_client.get('/game/{game_id}/{player_id}/new_total')

def test_winner(get_game, base_client):
    game_id = get_game["game_id"]
    response = base_client.get("/game/{game_id}/winner")
    response_json = response.json()
    assert response_json["success"] is True
    assert int(response_json["winner"]) == 0

if __name__ == '__main__':
    pytest.main()
