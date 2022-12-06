
f = open("Day 4/day4.txt", "r")
input_list = f.readlines()
f.close()

def getRange(lower,upper):
    lower = int(lower)
    upper = int(upper)
    
    num_range = list(range(lower,upper+1))
    
    # if the range is 6-6, it won't print a list, so we need to manually make one
    if len(num_range) == 0:
        num_range.append(lower)
    
    if lower == upper - 1:
        num_range = []
        num_range.append(lower)
        num_range.append(upper)
    
    return num_range


example_list = [
    "2-4,6-8\n",
    "2-3,4-5\n",
    "5-7,7-9\n",
    "2-8,3-7\n",
    "6-6,4-6\n",
    "2-6,4-8\n"
]

num_dupes = 0

for example in input_list:
    # String manipulation
    example = example[:-1]
    first_example = example.split(",")[0]
    second_example = example.split(",")[1]
    
    # Get range for first number
    first_lower,first_upper = first_example.split("-")
    first_range = getRange(first_lower,first_upper)

    # Get range for second number
    second_lower,second_upper = second_example.split("-")
    second_range = getRange(second_lower,second_upper)

    
    # It has to fully contain the other to be counted
    intersection_length = len(set(first_range).intersection(second_range))
    if intersection_length > 0:
        if (intersection_length == len(first_range)) or (intersection_length == len(second_range)):
                print("======")
                print(example)
                print(first_range)
                print(len(first_range))
                print(len(second_range))
                print(intersection_length)
                if (intersection_length != len(first_range)) and (intersection_length != len(second_range)):
                    print("Not matched to any range!")
                #print(first_range,second_range)
                #print(set(first_range).intersection(second_range))
                num_dupes += 1

print(num_dupes)

# 747 is too high
# 445 is too low
# 446 is too low
# 447 is too low
# 518 was right!