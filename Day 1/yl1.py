from typing import Counter

lines = open("Day 1/data.txt").readlines()
counter = 0

for i in range(len(lines)-1):
    number = int(lines[i].strip())
    next_number = int(lines[i+1].strip())

    if number < next_number:
        counter += 1

print(counter)