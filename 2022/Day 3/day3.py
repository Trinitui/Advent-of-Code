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

input_ex_list = ["vJrwpWtwJgWrhcsFMMfFFhFp",
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
"PmmdzqPrVvPwwTWBwg",
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
"CrZsJsPPZsGzwwsLwLmpwMDw"]

priority_sum = 0
for input_ex in input_list:
    print("------")
    input_ex = input_ex[:-1]
    a = int(len(input_ex)/2)
    #print(a)
    print("first part: ", input_ex[:-a],len(input_ex[:-a]))
    print("second part: ", input_ex[a:][:-1],len(input_ex[a:]))

    fp = input_ex[:-int(a)]
    sp = input_ex[int(a):]
    common_entry = set(fp).intersection(sp)
    common_entry = list(common_entry)[0]
    print(common_entry,entryScoring(common_entry))
    priority_sum += entryScoring(common_entry)


print("====")
print(priority_sum)
print("====")

# 7955 TOO LOW
# 7986 TOO LOW
# 8185 RIGHT ANSWER
