horizontal = 0
depth = 0

data = open("Day2/data.txt").readlines()

for i in range(len(data)):
    num = int(data[i].split(" ")[-1])

    if "up" in data[i]:
        depth = depth - num
    elif "down" in data[i]:
        depth = depth + num
    elif "forward" in data[i]:
        horizontal = horizontal + num

print("The final value is", horizontal * depth)