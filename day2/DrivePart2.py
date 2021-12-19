input = open('input.txt').readlines()

i = 0
forward = 0
depth = 0
aim = 0
while i < len(input):
    if input[i].startswith('forward'):
        forward += int(input[i][-2])
        depth += int(input[i][-2])*aim
    else:
        if input[i].startswith('up'):
            aim -= int(input[i][-2])
        else:
            aim += int(input[i][-2])
    i = i + 1

print(forward * depth)