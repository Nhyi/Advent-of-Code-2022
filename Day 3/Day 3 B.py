# Import modules.
from string import ascii_lowercase

# Keep track of the group count and list number.
group_count = 0

# Read through text file.
with open(r'D:\Documents\Programming\Python Projects\Advent of Code 2022\Day 3\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line.
    while len(lines) > 0:

        # Grab the first 3 lines and remove them for the 3 grouped rucksacks.
        rucksack1 = list(lines.pop(0).strip('\n'))
        rucksack2 = list(lines.pop(0).strip('\n'))
        rucksack3 = list(lines.pop(0).strip('\n'))

        # Calculate the common items in all 3 rucksacks.
        duplicate_items = list((set(rucksack1).intersection(rucksack2)).intersection(rucksack3))[0]

        # Calculate the value of the item .
        letter_value = ascii_lowercase.index(duplicate_items.lower()) + 1

        # If the item is uppercase then shift the value of it by 26
        if duplicate_items == duplicate_items.upper():
            letter_value += 26

        # Add to the running priority count.
        group_count += letter_value

    print(group_count)
