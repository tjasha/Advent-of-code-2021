input = open('inputSonar.txt').readlines()

i = 0
a = 0
while i < len(input)-3:
    sum1 = int(input[i]) + int(input[i + 1]) + int(input[i + 2])
    sum2 = int(input[i + 1]) + int(input[i + 2]) + int(input[i + 3])
    if sum2 > sum1:
        a = a + 1
    i = i + 1
print (a)