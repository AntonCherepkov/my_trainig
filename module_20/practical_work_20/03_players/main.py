players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_list = [
    (players + scores) for players, scores in players.items()
]

print(players_list)

# зачет!
