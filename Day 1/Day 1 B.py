# Keep a list of calories for each elf as well as counter.
cur_cal = 0
cal_list = []

# Open text file.
with open(r'D:\Documents\Programming\Python Projects\Advent of Code 2022\Day 1\inputs.txt', 'r') as file:

    # Read all lines in text file.
    lines = file.readlines()

    # Iterate through each line.
    for line in lines:

        # If the line is blank add the calories to the list for that elf and reset counter.
        if line == '\n':
            cal_list.append(cur_cal)
            cur_cal = 0
        else:
            # Keep on adding calories.
            cur_cal += int(line)

# Sort the calories list.
sorted_cal = sorted(cal_list)
# Sum the largest 3.
print(sum(sorted_cal[-3:]))