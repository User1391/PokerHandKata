import data_structures

move_on: bool = False
num_players = 0
while not move_on:
    print("How many players (2-9)?")
    try:
        num_players: int = int(input())
        move_on = True
    except Exception as e:
        print("Invalid input. Please retry.")

move_on = False
players = []
for i in range(num_players):
    player_name = input(f"Player {i} name: ")
    players.append(data_structures.Player(player_name))
