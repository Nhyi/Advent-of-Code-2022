# Import modules.
from string import ascii_lowercase

# Keep track of the priority item values.
prio_count = 0

# Read through text file.
with open(r'D:\Documents\Programming\Python Projects\Advent of Code 2022\Day 3\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line in text file.
    for line in lines:

        # Split the lines by newline.
        rucksack = line.splitlines()[0]

        # Put each rucksack in a list and find the number of items in it.
        items = list(rucksack)
        no_items = len(items)

        # Split the items into rucksack 1 and 2.
        rucksack1 = items[int(no_items/2):]
        rucksack2 = items[:int(no_items/2)]

        # Calculate the common items.
        duplicate_items = list(set(rucksack1).intersection(rucksack2))

        # If a duplicate item exists, calculate the priority value of it.
        if len(duplicate_items) != 0:

            for item in duplicate_items:

                letter_value = ascii_lowercase.index(item.lower()) + 1

                # If the item is uppercase then shift the value of it by 26
                if item == item.upper():
                    letter_value += 26

                # Add to the running priority count.
                prio_count += letter_value

    print(prio_count)
