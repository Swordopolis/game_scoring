def scythe_points():
    points = 0
    
    pop = int(input("pop: "))
    if pop < 7:
        pop_mod = {"star": 3, "hex": 2, "resource": 1}
    elif pop < 13:
        pop_mod = {"star": 4, "hex": 3, "resource": 2}
    else: 
        pop_mod = {"star": 5, "hex": 4, "resource": 3}
    #print(f"pop modifier is {pop_mod}")
    
    stars =  int(input("stars: "))
    points += pop_mod["star"] * stars
    print(points)
    hexes = int(input("hexes: "))
    points += pop_mod["hex"] * hexes
    print(points)
    resources = int(input("resources: "))//2
    points += pop_mod["resource"] * resources
    print(points)
    bonus = int(input("bonus: "))
    points += bonus
    print(points)
    coins = int(input("coins: "))
    points += coins
    print(points)
    return points

def score_scythe():
    player_count = int(input("player count:"))
    players = {}
    for i in range(player_count):
        player_name = input("player name:")
        players[player_name] = {"name": player_name, "score": scythe_points()}
    for player in players:
        #print(player)
        print(players[player]["name"], " : ", players[player]["score"])

score_scythe()