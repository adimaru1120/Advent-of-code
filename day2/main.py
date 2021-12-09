import os

wejscie = []
with open('input.txt') as f:
    wejscie = f.readlines()

depth = 0
horizontal = 0

### part 1
'''
for str in wejscie:
    splited = str.split()
    
    if splited[0] == "forward":
        horizontal += int(splited[1])
    elif splited[0] == "down":
        depth += int(splited[1])
    elif splited[0] == "up":
        depth -= int(splited[1])
'''

### part 2

aim = 0

for str in wejscie:
    splited = str.split()
    
    if splited[0] == "forward":
        horizontal += int(splited[1])
        depth += aim * int(splited[1])
    elif splited[0] == "down":
        aim += int(splited[1])
    elif splited[0] == "up":
        aim -= int(splited[1])
        
print(depth * horizontal)