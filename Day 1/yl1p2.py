lines = open("Day 1/data.txt").readlines()
counter = 0

for i in range(len(lines)-3):
    a = int(lines[i].strip()) + int(lines[i+1].strip()) + int(lines[i+2].strip())
    b = int(lines[i+1].strip()) + int(lines[i+2].strip()) + int(lines[i+3].strip())
    if a < b:
        counter += 1
    print(a, b)

print(counter)