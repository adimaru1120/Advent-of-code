with open('input.txt') as f:
    input = []
    for line in f.readlines():
        line = line.rstrip("\n")
        line = line.split(",")
        input = [int(num) for num in line]

    
    ### part 1

    input.sort()

    input_length = len(input)
    med = 0

    ### median of list 
    if input_length % 2 == 0:
        med = input_length / 2
    else:
        med = (input_length + 1) / 2

    med_val = input[int(med)]

    cost = 0
    
    for item in input:
        cost += abs(med_val - item)

    print(cost)