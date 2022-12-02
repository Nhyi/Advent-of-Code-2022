# Keep track of current and maximum calorie counts.
cur_cal = 0
max_cal = 0

# Open inputs file.
with open(r'D:\Documents\Programming\Python Projects\Programming Challenges\Adventure of Code\Day 1\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line in text file.
    for line in lines:

        # If the line is blank, reset calorie counter.
        if line == '\n':
            cur_cal = 0
        else:
            # Keep on adding calories.
            cur_cal += int(line)

        # If the current calories is greater than any previous elf update.
        if cur_cal > max_cal:
            max_cal = cur_cal

print(max_cal)