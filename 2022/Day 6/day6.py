f = open("Day 6/day6.txt", "r")
input_list = f.readlines()[0]
f.close()

e_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 7
e_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # 5
e_3 = "nppdvjthqldpwncqszvftbrmjlhg" # 6
e_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 10

temp = []
for i,char in enumerate(input_list):
    print(i+1, char)
    
    temp.append(char)
    
    if len(temp) == 4:
        print(temp)
        if len(list(set(temp))) == 4:
            print(i+1)
            break
        
        temp.remove(temp[0])
        print(temp)


    
    #print(temp)
    #print(set(temp))