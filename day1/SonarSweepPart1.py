results = open('inputSonar.txt', 'r').readlines()

i = 0
a = 1
while i < len(results):
    if results[i] > results[i-1]:
        a = a + 1
    i = i + 1
print (a)