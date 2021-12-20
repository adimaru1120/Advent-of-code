with open('input.txt') as f:
    input = []
    for line in f.readlines():
        line = line.rstrip("\n")
        line = line.split(",")
        input = [int(num) for num in line]

# input = [3, 4, 3, 1, 2]

    ### part 1

    zero_cnt = 0
    for days in range(80):

        ### adding new entrys at the begining of new day 
        if zero_cnt > 0:
            for i in range(zero_cnt):
                input.append(9)

        zero_cnt = 0
        for i, item in enumerate(input):
            input[i] -= 1

            if input[i] == 0:
                input[i] = 7
                zero_cnt += 1
        
       
    print(len(input))

    
            
