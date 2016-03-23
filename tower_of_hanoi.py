
# Find min number of moves to move a tower of height 64
moves_for_height_dict = {}

def moveTower(height, fromPole, toPole, withPole):
    global moves_for_height_dict
    move_count = 0
    if height == 1:
        move_count += 1
    if height > 1:
        if (height - 1) in moves_for_height_dict:
            move_count += moves_for_height_dict[height - 1]
        else:
            move_count += moveTower(height - 1, fromPole, withPole, toPole)
        move_count += 1
        if (height - 1) in moves_for_height_dict:
            move_count += moves_for_height_dict[height - 1]
        else:
            move_count += moveTower(height - 1, fromPole, withPole, toPole)
    moves_for_height_dict[height] = move_count
    return move_count

print moveTower(64, "A", "B", "C")

