cur_cal = 0
max_cal = 0

with open(r'D:\Documents\Programming\Python Projects\Programming Challenges\Adventure of Code\Day 1\input.txt', 'r') as file:

    lines = file.readlines()

    for line in lines:

        if line == '\n':
            cur_cal = 0
        else:
            cur_cal += int(line)

        if cur_cal > max_cal:
            max_cal = cur_cal

print(max_cal)