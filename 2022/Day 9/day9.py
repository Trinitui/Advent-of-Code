#https://adventofcode.com/2022/day/9

# -- Initialize Grid --
# 6w x 5h
h = "H"
t = "T"

grid = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [h,0,0,0,0,0]
]

f = open("2022/Day 9/day9_ex.txt", "r")
input_list = f.readlines()
f.close()

print(input_list)


# Functions to use 
def showGrid(gridlike):
    for el in gridlike:
        print(el)

def findIndexH(gridlike):
    for i,row in enumerate(gridlike):
        print(row)
        for j,el in enumerate(row):
            if el == "H":
                print("Found head!",i,j,el)
                return i,j
                

# Main loop through instructions
for k,instruction in enumerate(input_list):
    print(f"===== MOVE {k}: {instruction[:-1]} =====")
    # Parse Instructions
    instruction = instruction[:-1]
    move = instruction[2]

    # Initialize data needed for move
    row,col = findIndexH(grid)

    if instruction[0] == "R":
        
        # Parse Movement RIGHT
        final_pos = col + int(move)
        grid[row][final_pos] = h
        grid[row][final_pos - 1] = t

        # Create Tail's trail RIGHT
        for l,inter in enumerate(grid[row]):
            if l >= col and l <= final_pos - 1:
                grid[row][l] = "X"
        
        print(f"End of move State: {grid[row]}")

    if instruction[0] == "L":

        # Parse Movement LEFT
        final_pos = col - int(move)
        grid[row][final_pos] = h
        grid[row][final_pos + 1] = t
        
        # Create Tail's trail LEFT
        for l,inter in enumerate(grid[row]):
            if l <= col and l >= final_pos + 1:
                grid[row][l] = "X"
        
        print(f"End of move State: {grid[row]}")




    if instruction[0] == "U":

        # Parse Movement UP
        grid[row][col] = "X"
        final_pos = row - int(move)
        grid[final_pos][col] = h
        print(row,col)
        print(f"End of move State: {grid[final_pos]}")




    if instruction[0] == "D":
        #row,col = findIndexH(grid)

        grid[row][col] = "X"
        final_pos = row + int(move)
        grid[final_pos][col] = h
        print(row,col)
        print(f"End of move State: {grid[final_pos]}")


print("\nFINAL LAYOUT:")
print(showGrid(grid))


