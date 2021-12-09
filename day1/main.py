import os


wejscie = []
with open('input.txt') as f:
    wejscie = f.readlines()

counter = 0

### part 1
''' 
for index, value in enumerate(wejscie):
    if index is 0:
        continue
    else:
        if(int(wejscie[index]) > int(wejscie[index - 1])):
            counter += 1

'''

### part 2
i = 0
val = []

while i < len(wejscie) - 2:
    suma = 0

    for k in range(3):
        suma += int(wejscie[i + k])

    val.append(suma)

    if i == 0:
        pass
    else:
        if val[i] > val[i - 1]:
            counter += 1
    i += 1
    

print(counter)
