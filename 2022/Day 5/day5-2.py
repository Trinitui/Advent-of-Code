    # https://adventofcode.com/2022/day/5

'''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
'''

example_instructions = [
'move 1 from 2 to 1\n',
'move 3 from 1 to 3\n',
'move 2 from 2 to 1\n',
'move 1 from 1 to 2\n'
]

example_grid = [
    ["Z","N"],
    ["M","C","D"],
    ["P"]
]   

'''
FINAL ORIENTATION:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

'''

# Challenge now is a NON-LIFO SOLUTION
# Main loop!
for inst in example_instructions:
    
    print('\n')
    # Get list from instruction
    inst = inst[:-1]
    print(inst)
    inst = inst.replace("move ","").replace(" from ","|").replace(" to ","|").replace("\n","").split("|")
    
    # Initialize variables from instructions
    num_to_move = int(inst[0])
    source = int(inst[1]) - 1
    destination = int(inst[2]) - 1

    #Do NON LIFO
    # Move Whole chunk of list, not just popping one at a time

    chunk_to_move = example_grid[source][:num_to_move]
    print(chunk_to_move)
    example_grid[destination].append(example_grid[source][:num_to_move])
    example_grid[destination] = [item for sublist in example_grid[destination] for item in sublist]
    #example_grid[source][:num_to_move]
    print("Moving...",example_grid)
    print("Move Complete")
    break

print(example_grid)
ans = []
for row in example_grid:
    ans.append(row[-1])
print("".join(ans))







# ----------------------------- ACTUAL WORK FOR DAY 1-1 BELOW

'''
    [M]             [Z]     [V]    
    [Z]     [P]     [L]     [Z] [J]
[S] [D]     [W]     [W]     [H] [Q]
[P] [V] [N] [D]     [P]     [C] [V]
[H] [B] [J] [V] [B] [M]     [N] [P]
[V] [F] [L] [Z] [C] [S] [P] [S] [G]
[F] [J] [M] [G] [R] [R] [H] [R] [L]
[G] [G] [G] [N] [V] [V] [T] [Q] [F]
 1   2   3   4   5   6   7   8   9 

 '''

'''
f = open("2022/Day 5/day5.txt", "r")
input_list = f.readlines()
f.close()

grid = [
    ["G","F","V","H","P","S"],
    ["G","J","F","B","V","D","Z","M"],
    ["G","M","L","J","N"],
    ["N","G","Z","V","D","W","P"],
    ["V","R","C","B"],
    ["V","R","S","M","P","W","L","Z"],
    ["T","H","P"],
    ["Q","R","S","N","C","H","Z","V"],
    ["F","L","G","P","V","Q","J"]
]

# Main loop!
for inst in input_list:
    
    print('\n')
    # Get list from instruction
    inst = inst[:-1]
    print(inst)
    inst = inst.replace("move ","").replace(" from ","|").replace(" to ","|").replace("\n","").split("|")
    
    # Initialize variables from instructions
    num_to_move = int(inst[0])
    source = int(inst[1]) - 1
    destination = int(inst[2]) - 1

    #DoLIFO
    for popper in range(0,num_to_move):
        grid[destination].append(grid[source].pop())
        print("Moving...",grid)
    print("Move Complete")

print(grid)
ans = []
for row in grid:
    ans.append(row[-1])
print("".join(ans))

'''