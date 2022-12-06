# Open and read the file.
with open(r'D:\Documents\Programming\Python Projects\Advent of Code 2022\Day 6\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = list(file.readlines()[0])

    # Go through each letter in the string.
    for i in range(len(lines) - 4 + 1):
        # Create a list of 4 letter packets to check.
        letter_array = lines[i:i+4]

        # If the set of the array and the length of the array are the same, we have a packet.
        if len(set(letter_array)) == len(letter_array):
            # Print the ith + 4 value since it starts from 0.
            print(i+4)
            break