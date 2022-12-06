# Example starting input:
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

example_col_1 = ["N","Z"]
example_col_2 = ["D","C","M"]
example_col_3 = ["P"]



class Column(object):
    """
    Base class.
    Args:
        *args (list): list of arguments
        **kwargs (dict): dict of keyword arguments
    Attributes:
        self
    """

    def __init__(self,name):
        self.name = name
        self.containers = []

    
    def setupContainers(self,container_list):
        self.containers = container_list
        #print("Containers Set Up!: ", self.containers)
    
    def getContainers(self):
        return self.containers
    
    def showContainers(self):
            return print("Printing Current State of containers: ",self.containers)
    
    def changeContainers(self,new_list):
        self.containers = new_list
        print("Changed containers to: ",self.containers)
'''

example_col_1 = Column("Col1")
example_col_2 = Column("Col2")
example_col_3 = Column("Col3")
example_col_1.setupContainers(["N","Z"] )
example_col_2.setupContainers(["D","C","M"])
example_col_3.setupContainers(["P"])

print(example_col_1.showContainers())
print(example_col_2.showContainers())
print(example_col_3.showContainers())


for inst in example_instructions:
    print("\n=======")
    print("INSTRUCTIONS",inst[:-1])
    inst = inst[:-1]
    inst = inst.replace("move ","").replace(" from ","|").replace(" to ","|").replace("\n","")

    num_move, source, destination = inst.split("|")
    
    if source == '1':
        print("\tDetecting a move from Source 1")
        to_move = example_col_1.getContainers()
        new_list = to_move[int(num_move):]
        to_move = to_move[:int(num_move)]
        example_col_1.changeContainers(new_list)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            change_this = example_col_2.getContainers()
            to_move = to_move[::-1]
            change_this = to_move + change_this
            example_col_2.changeContainers(change_this)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            change_this = example_col_3.getContainers()
            to_move = to_move[::-1]
            change_this = to_move + change_this
            example_col_3.changeContainers(change_this)
    
    if source == '2':
        print("\tDetecting a move from Source 2")
        to_move = example_col_2.getContainers()
        new_list = to_move[int(num_move):]
        to_move = to_move[:int(num_move)]
        example_col_2.changeContainers(new_list)

        if destination == "1":
            print("\t\tDetecting a move to Destination 1")
            change_this = example_col_1.getContainers()
            to_move = to_move[::-1]
            change_this = to_move + change_this
            example_col_1.changeContainers(change_this)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            change_this = example_col_3.getContainers()
            to_move = to_move[::-1]
            change_this = to_move + change_this
            example_col_3.changeContainers(change_this)
    
    if source == '3':
        print("\tDetecting a move from Source 3")
        to_move = example_col_3.getContainers()
        new_list = to_move[int(num_move):]
        to_move = to_move[:int(num_move)]
        example_col_3.changeContainers(new_list)

        if destination == "1":
            print("\t\tDetecting a move to Destination 1")
            change_this = example_col_1.getContainers()
            to_move = to_move[::-1]
            change_this = to_move + change_this
            example_col_1.changeContainers(change_this)
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            change_this = example_col_2.getContainers()
            to_move = to_move[::-1]
            change_this = to_move + change_this
            example_col_2.changeContainers(change_this)

    print("INTERSTITAL STATE: ")
    print(example_col_1.showContainers())
    print(example_col_2.showContainers())
    print(example_col_3.showContainers())

print("\n ====== \n")
print("FINAL STATE")
print(example_col_1.showContainers())
print(example_col_2.showContainers())
print(example_col_3.showContainers())

print("\n ====== \n")
print("FINAL ANSWER")
print(example_col_1.getContainers()[0],example_col_2.getContainers()[0],example_col_3.getContainers()[0])

'''



# My starting input below:
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

col_1 = Column("Col1")
col_2 = Column("Col2")
col_3 = Column("Col3")
col_4 = Column("Col4")
col_5 = Column("Col5")
col_6 = Column("Col6")
col_7 = Column("Col7")
col_8 = Column("Col8")
col_9 = Column("Col9")

col_1.setupContainers(["S","P","H","V",'F',"G"] )
col_2.setupContainers(["M","Z","D","V","B","F","J","G"])
col_3.setupContainers(["N","J","L","M","G"])
col_4.setupContainers(["P","W","D","V","Z","G","N"])
col_5.setupContainers(["B","C","R","V"])
col_6.setupContainers(["Z","L","W","P","M","S","R","V"])
col_7.setupContainers(["P","H","T"])
col_8.setupContainers(["V","Z","H","C","N","S",'R',"Q"])
col_9.setupContainers(["J","Q","V","P","G","L","F"])

print(col_1.showContainers())
print(col_2.showContainers())
print(col_3.showContainers())
print(col_4.showContainers())
print(col_5.showContainers())
print(col_6.showContainers())
print(col_7.showContainers())
print(col_8.showContainers())
print(col_9.showContainers())

f = open("Day 5/day5.txt", "r")
input_list = f.readlines()
f.close()


def handleSource(source_col):
    to_move = source_col.getContainers()
    new_list = to_move[int(num_move):]
    to_move = to_move[:int(num_move)]
    source_col.changeContainers(new_list)
    return to_move

def handleDestination(to_move_l,destination_col):
    change_this = destination_col.getContainers()
    to_move_l = to_move_l[::-1]
    change_this = to_move_l + change_this
    destination_col.changeContainers(change_this)

counter = 0
for inst in input_list:
    # Do check
    check =\
    len(col_1.getContainers())+\
    len(col_2.getContainers())+\
    len(col_3.getContainers())+\
    len(col_4.getContainers())+\
    len(col_5.getContainers())+\
    len(col_6.getContainers())+\
    len(col_7.getContainers())+\
    len(col_8.getContainers())+ len(col_9.getContainers())

    
    counter += 1
    print("\n=======")
    print("INSTRUCTIONS",inst[:-1])
    inst = inst[:-1]
    inst = inst.replace("move ","").replace(" from ","|").replace(" to ","|").replace("\n","")

    num_move, source, destination = inst.split("|")

    if source == '1':
        print("\tDetecting a move from Source 1")
        move_containers = handleSource(col_1)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '2':
        print("\tDetecting a move from Source 2")
        move_containers = handleSource(col_2)
        
        if destination == "1":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '3':
        print("\tDetecting a move from Source 3")
        move_containers = handleSource(col_3)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '4':
        print("\tDetecting a move from Source 4")
        move_containers = handleSource(col_4)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "5":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '5':
        print("\tDetecting a move from Source 5")
        move_containers = handleSource(col_5)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '6':
        print("\tDetecting a move from Source 6")
        move_containers = handleSource(col_6)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "6":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '7':
        print("\tDetecting a move from Source 7")
        move_containers = handleSource(col_7)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '8':
        print("\tDetecting a move from Source 8")
        move_containers = handleSource(col_8)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)
        if destination == "9":
            print("\t\tDetecting a move to Destination 9")
            handleDestination(move_containers,col_9)
    
    if source == '9':
        print("\tDetecting a move from Source 9")
        move_containers = handleSource(col_9)
        
        if destination == "2":
            print("\t\tDetecting a move to Destination 2")
            handleDestination(move_containers,col_2)
        if destination == "3":
            print("\t\tDetecting a move to Destination 3")
            handleDestination(move_containers,col_3)
        if destination == "4":
            print("\t\tDetecting a move to Destination 4")
            handleDestination(move_containers,col_4)
        if destination == "5":
            print("\t\tDetecting a move to Destination 1")
            handleDestination(move_containers,col_1)
        if destination == "6":
            print("\t\tDetecting a move to Destination 6")
            handleDestination(move_containers,col_6)
        if destination == "7":
            print("\t\tDetecting a move to Destination 7")
            handleDestination(move_containers,col_7)
        if destination == "8":
            print("\t\tDetecting a move to Destination 8")
            handleDestination(move_containers,col_8)
        if destination == "9":
            print("\t\tDetecting a move to Destination 5")
            handleDestination(move_containers,col_5)

    print("INTERSTITAL STATE: ")
    print(col_1.showContainers())
    print(col_2.showContainers())
    print(col_3.showContainers())
    print(col_4.showContainers())
    print(col_5.showContainers())
    print(col_6.showContainers())
    print(col_7.showContainers())
    print(col_8.showContainers())
    print(col_9.showContainers())

    after_check =\
    len(col_1.getContainers())+\
    len(col_2.getContainers())+\
    len(col_3.getContainers())+\
    len(col_4.getContainers())+\
    len(col_5.getContainers())+\
    len(col_6.getContainers())+\
    len(col_7.getContainers())+\
    len(col_8.getContainers())+ len(col_9.getContainers())

    if after_check < check:
        print("UH OH, CONTAINER DROPPED")
        print("COUNTER AT: ",counter)
        break



print("\n ====== \n")
print("FINAL STATE")
print(col_1.showContainers())
print(col_2.showContainers())
print(col_3.showContainers())
print(col_4.showContainers())
print(col_5.showContainers())
print(col_6.showContainers())
print(col_7.showContainers())
print(col_8.showContainers())
print(col_9.showContainers())

print("\n ====== \n")
print("FINAL ANSWER")
print(col_1.getContainers()[0],
    col_2.getContainers()[0],
    col_3.getContainers()[0],
    col_4.getContainers()[0],
    col_5.getContainers()[0],
    col_6.getContainers()[0],
    col_7.getContainers()[0],
    col_8.getContainers()[0],
    col_9.getContainers()[0], 
)