f = open("2022/Day 7/day7_ex.txt", "r")
input_list = f.readlines()
f.close()




command_list = []
ls_flag = 0

directory = {}

# Dynamicaly build a dictionary from keys and stuff

for el in input_list:
    el = el[:-1]
    if el[0] == "$":
        continue
    else:    
        # Make aware of current directory!
        if el.__contains__("dir") == True:
            print(el)
            directory[el[-1]] = {}

print(directory)
