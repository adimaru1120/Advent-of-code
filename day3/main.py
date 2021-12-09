import os

wejscie = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        wejscie.append(line)

epsilon = ""
gamma = ""

### part 1

# for i in range(len(wejscie[0])):
#     ones = 0
#     zeros = 0
#     for j in range(len(wejscie)):
#         if wejscie[j][i] == '0':
#             zeros += 1
#         else:
#             ones += 1
    
#     if zeros > ones:
#         gamma += '0'
#         epsilon += '1'
#     else:
#         gamma += '1'
#         epsilon += '0'

### part 2

obecny = wejscie
i = 0

while len(obecny) != 1:
    zeros = []
    ones = []

    for j in range(len(obecny)):
        if obecny[j][i] == '0':
            zeros.append(obecny[j])
        else:
            ones.append(obecny[j])

    if len(ones) == len(zeros):
        obecny = ones
    elif len(ones) > len(zeros):
        obecny = ones
    else:
        obecny = zeros
    
    i += 1

epsilon = obecny[0]
    
obecny = wejscie
i = 0

while len(obecny) != 1:
    zeros = []
    ones = []

    for j in range(len(obecny)):
        if obecny[j][i] == '0':
            zeros.append(obecny[j])
        else:
            ones.append(obecny[j])

    if len(ones) == len(zeros):
        obecny = zeros
    elif len(ones) < len(zeros):
        obecny = ones
    else:
        obecny = zeros
    
    i += 1

gamma = obecny[0]

print(int(epsilon, 2) * int(gamma, 2))