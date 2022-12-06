
from string import ascii_lowercase, ascii_uppercase

def entryScoring(entry):
    score = 0
    for i,lowercase_el in enumerate(ascii_lowercase):
        if lowercase_el == entry:
            score += i+1
    for j,uppercase_el in enumerate(ascii_uppercase):
        if uppercase_el == entry:
            score += j+27
    return score

f = open("day3.txt", "r")
input_list = f.readlines()
f.close()



input_ex_list = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    "PmmdzqPrVvPwwTWBwg",
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

result = 0

group_list = []
counter = 0
for input_ex in input_list:
    input_ex = input_ex[:-1]
    group_list.append(input_ex)
    counter += 1

    if counter == 3:
        print(len(group_list), group_list)
        commonality = set(group_list[0]).intersection(group_list[1]).intersection(group_list[2])
        commonality = list(commonality)[0]
        print(commonality)
        counter = 0
        group_list = []
        result += entryScoring(commonality)

print(result)