# Rock = (A, X) = 1
# Paper = (B, Y) = 2
# Scissors = (C, Z) = 3

# Win = 6
# Draw = 3
# Loss = 0

# Set the values for each of the choices.
points = {'X': 1, 'Y': 2,'Z': 3}
# Set winning, drawing and losing mappings.
winning = {'A': 'Y', 'B': 'Z', 'C': 'X'}
drawing = {'A': 'X', 'B': 'Y', 'C': 'Z'}
losing = {'A': 'Z', 'B': 'X', 'C': 'Y'}

# Keep track of the cumulative points.
cum_count = 0

# Read through text file.
with open(r'D:\Documents\Programming\Python Projects\Advent of Code 2022\Day 2\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line in text file.
    for line in lines:

        # Split the lines by newline and a blank space.
        turn = line.splitlines()[0].split(' ')

        # Set points for winning, drawing and losing strategies.
        # Calculate the choice we would need to make for the outcome.
        if turn[1] == 'X':
            turn_point = 0
            choice_point = points[losing[turn[0]]]
        elif turn[1] == 'Y':
            turn_point = 3
            choice_point = points[drawing[turn[0]]]
        else:
            turn_point = 6
            choice_point = points[winning[turn[0]]]

        # Add to total.
        cum_count += turn_point + choice_point

    print(cum_count)
