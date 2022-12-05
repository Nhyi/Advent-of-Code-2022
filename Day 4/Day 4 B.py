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

        # Calculate the left and right interval for the first pair.
        first_left_interval = int(pair_assignment[0].split('-')[0])
        first_right_interval = int(pair_assignment[0].split('-')[1])
        # Create a list of integers between the 2 intervals.
        first_list = [i for i in range(first_left_interval, first_right_interval + 1)]

        # Calculate the left and right interval for the second pair.
        second_left_interval = int(pair_assignment[1].split('-')[0])
        second_right_interval = int(pair_assignment[1].split('-')[1])
        # Create a list of integers between the 2 intervals.
        second_list = [i for i in range(second_left_interval, second_right_interval + 1)]

        # Check if left or right interval in any pair exists in the opposite pairs list.
        if (second_left_interval in first_list or second_right_interval in first_list) or \
            (first_left_interval in second_list or first_right_interval in second_list):

            # Increment the contained counter.
            contained_count += 1

    print(contained_count)