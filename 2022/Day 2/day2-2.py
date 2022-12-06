# A is Rock
# B is Paper
# C is Scissors

# X Need to Lose
# Y Need to Draw
# Z Need to Win

# 1 point for rock
# 2 points for paper
# 3 points for scissors

# 0 if you lost
# 3 for a draw
# 6 if you win

def translate(to_translate):
    score = 0

    if to_translate == "A":
        score += 1
    if to_translate == "B":
        score += 2
    if to_translate == "C":
        score += 3
    
    return score

def evalTurn(my,op):
    #print("DEBUG: ",my,op)
    pnts = 0
    if my == op:
        print("Draw! 3 points")
        pnts += 3
    
    if (my < op):
        if my == 1 and op == 3:
            print("You won on a rocks-scissor matchup")
            pnts += 6
        else:
            print("You lose!")
            pnts += 0
    
    if (my > op):
        if op ==1 and my == 3:
            print("You lost on a rocks-scissor matchup")
            pnts += 0
        else:
            print("You win!")
            pnts += 6
    
    return pnts



f = open("day2.txt", "r")
input_list = f.readlines()
f.close()

my_points = 0

for input_el in input_list:
    print("======")
    if len(input_el) == 4:
        data = input_el[:-1]
        #print(data)
        opponent_choice = data[0]
        outcome = data[-1]
    else:
        data = input_el
        opponent_choice = data[0]
        outcome = data[-1]

    my_choice = "T"

    if outcome == "X":  # I NEED TO LOSE
        if opponent_choice == "A": # ROCK
            my_choice = "C"
        if opponent_choice == "B": # PAPER
            my_choice = "A"
        if opponent_choice == "C": # SCISSORS
            my_choice = "B"

    if outcome == "Y": # I NEED TO DRAW
        if opponent_choice == "A": # ROCK
            my_choice = "A"
        if opponent_choice == "B": # PAPER
            my_choice = "B"
        if opponent_choice == "C": # SCISSORS
            my_choice = "C"
    
    if outcome == "Z": # I NEED TO WIN
        if opponent_choice == "A": # ROCK
            my_choice = "B"
        if opponent_choice == "B": # PAPER
            my_choice = "C"
        if opponent_choice == "C": # SCISSORS
            my_choice = "A"
    
    #print(opponent_choice, my_choice)

    
    if my_choice == "C":
        my_points += 3
    if my_choice == "B":
        my_points += 2
    if my_choice == "A":
        my_points += 1

    
    my_points += evalTurn(translate(my_choice),translate(opponent_choice))
    print("op|me")
    #print(input_el[:-1],len(input_el))
    #print(data)
    print("------")
    print(opponent_choice,my_choice,my_points)
    print("------")
print(my_points)


# 12316 WAS CORRECT!