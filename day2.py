colours = {"red": 12, "green": 13, "blue": 14}


def game(g_list):
    p = 1
    for i in g_list:
        p *= i
    return p


def is_possible(pair_color):
    for pair in pair_color:
        [n, color] = pair.split(" ")
        if color not in colours:
            return False
        if int(n) > colours[color]:
            return False
    return True


with open("test.txt", "r") as file:
    sum_ids = 0
    power_sum = 0
    for line in file:
        [game_id, data] = line.strip().split(": ")
        game_id = int(game_id.split(" ")[1])
        game_possible = True
        colours_count = {"red": 0, "green": 0, "blue": 0}
        for game_round in data.split("; "):
            colors = game_round.split(", ")
            if not is_possible(colors):
                game_possible = False
            for pair in colors:
                [n, color] = pair.split(" ")
                colours_count[color] = max(colours_count[color], int(n))
        if game_possible:
            sum_ids += game_id
        power = game([colours_count[key] for key in colours_count])
        power_sum += power
    print("PART 1 " + str(sum_ids))
    print("PART 2 " + str(power_sum))
