list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []

with open(r'D:\Documents\Programming\Python Projects\Advent of Code 2022\Day 5\inputs.txt', 'r') as file:

    # Read through all file lines.
    lines = file.readlines()

    for line in lines:

        if '[' in list(line) or ']' in list(line):

            cleaned_line = line.replace('\n', '')
            line_list = list(cleaned_line)

            list1.append(line_list[1])
            list2.append(line_list[5])
            list3.append(line_list[9])
            list4.append(line_list[13])
            list5.append(line_list[17])
            list6.append(line_list[21])
            list7.append(line_list[25])
            list8.append(line_list[29])
            list9.append(line_list[33])

            for iterate_list in [list1, list2, list3, list4, list5, list6, list7, list8, list9]:
                try:
                    iterate_list.remove(' ')
                except:
                    pass

        elif 'move' in line:
            stack_dump = []
            array_list = [list1, list2, list3, list4, list5, list6, list7, list8, list9]
            moves = line.replace('move', '').replace('from', '').replace('to', '').replace('\n', '')
            moves = (moves.split(' '))
            iterated_moves = [x for x in moves if x != '']
            for i in range(int(iterated_moves[0])):
                pop_value = array_list[int(iterated_moves[1])-1].pop(0)
                stack_dump.insert(0, pop_value)
            for i in range(int(iterated_moves[0])):
                secondary_pop = stack_dump.pop(0)
                array_list[int(iterated_moves[2])-1].insert(0, secondary_pop)

    string_storage = []
    for individual_list in array_list:
        if len(individual_list) != 0:
            string_storage.append(individual_list[0])

print(''.join(string_storage))