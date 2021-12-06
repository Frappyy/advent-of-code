horizontal = 0
depth = 0
aim = 0

data = open("Day 2/data.txt").readlines()

for i in range(len(data)):
    num = int(data[i].split(" ")[-1])

    if "up" in data[i]:
        aim = aim - num
    elif "down" in data[i]:
        aim = aim + num
    elif "forward" in data[i]:
        horizontal = horizontal + num
        depth = depth + (num * aim)

print("The final value is", horizontal * depth)