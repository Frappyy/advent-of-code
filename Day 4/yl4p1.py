data = open("Day 4/data.txt").readlines()

numbers = [line.split(",") for line in data]
print(numbers)