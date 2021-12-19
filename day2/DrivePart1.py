input = open('input.txt').readlines()

i = 0
forward = 0
depth = 0
while i < len(input):
    if input[i].startswith('forward'):
        forward += int(input[i][-2])
    else:
        if input[i].startswith('up'):
            depth -= int(input[i][-2])
        else:
            depth += int(input[i][-2])
    i = i + 1

print(forward * depth)