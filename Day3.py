valid = 0
invalid = 0

with open("test.txt") as f:
    for line in f:
        test = line.split()
        test2 = ((list(map(int, test))))
        if(test2[0] + test2[1] <= test2[2]):
            invalid += 1
        elif(test2[0] + test2[1] >= test2[2]):
            valid += 1

　
print(valid, invalid)
