cur_cal = 0
cal_list = []

with open(r'D:\Documents\Programming\Python Projects\Programming Challenges\Adventure of Code\Day 1\input.txt', 'r') as file:

    lines = file.readlines()

    for line in lines:

        if line == '\n':
            cal_list.append(cur_cal)
            cur_cal = 0
        else:
            cur_cal += int(line)

sorted_cal = sorted(cal_list)
print(sum(sorted_cal[-3:]))