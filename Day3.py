valid = 0

with open("test.txt") as f:
    for line in f:
        test = line.split()
        test2 = ((list(map(int, test))))
        if((test2[0] + test2[1] > test2[2]) and (test2[1] + test2[2] > test2[0]) and (test2[2] + test2[0] > test2[1])):
            valid += 1
        print(valid)
