gamma = ""
epsilon = 0
true = 0
false = 0
char = 0
num = 0
data = open("Day 3/data.txt").readlines()

for i in data[0]:
    for line in range(len(data)):
        if int(data[line][char]) == 1:
            true += 1
        else:
            false += 1

    if true > false:
        gamma += "1"
    else:
        gamma += "0"
    
    print(gamma)
    char += 1