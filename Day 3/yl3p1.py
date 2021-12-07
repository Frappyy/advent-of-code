gamma = ""
epsilon = ""
one = 0
zero = 0
char = 0

data = open("Day 3/data.txt").readlines()

for i in range(len(data[0])-1):
    for line in range(len(data)):
        if data[line][char] == "1":
            one += 1
        elif data[line][char] == "0":
            zero += 1
        
    if one > zero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    
    char += 1
    one = 0
    zero = 0

print("Gamma:", gamma, "Epsilon:", epsilon)
print(int(gamma, 2), "*", int(epsilon, 2), "=", int(gamma, 2) * int(epsilon, 2))