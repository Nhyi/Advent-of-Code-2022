# Keep track of the pairs that fully contain the other.
contained_count = 0

# Open and read the file.
with open(r'D:\Documents\Programming\Python Projects\Advent of Code 2022\Day 4\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    # Iterate through each line.
    for line in lines:

        # Split each line into it's individual pairs
        pair_assignment = line.replace('\n', '').split(',')

        # Calculate the left and right interval for the first pair and its range.
        first_left_interval = int(pair_assignment[0].split('-')[0])
        first_right_interval = int(pair_assignment[0].split('-')[1])
        first_range = abs(first_right_interval - first_left_interval)

        # Calculate the left and right interval for the second pair and its range.
        second_left_interval = int(pair_assignment[1].split('-')[0])
        second_right_interval = int(pair_assignment[1].split('-')[1])
        second_range = abs(second_right_interval - second_left_interval)

        # Check if one interval contains another by looking at the left and right values as well as the range.
        if (second_range <= first_range and second_left_interval >= first_left_interval and second_right_interval <= first_right_interval) or \
        (first_range <= second_range and second_left_interval <= first_left_interval and second_right_interval >= first_right_interval):

            # Increment the contained counter.
            contained_count += 1

    print(contained_count)