f = open("Day 6/day6.txt", "r")
input_list = f.readlines()[0]
f.close()

e_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 19
e_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # 23
e_3 = "nppdvjthqldpwncqszvftbrmjlhg" # 23
e_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 29

temp = []
for i,char in enumerate(input_list):
    print(i+1, char)
    
    temp.append(char)
    
    if len(temp) == 14:
        print(temp)
        if len(list(set(temp))) == 14:
            print(i+1)
            break
        
        temp.remove(temp[0])
        print(temp)


    
    #print(temp)
    #print(set(temp))