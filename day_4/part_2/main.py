from day_4.range import Range

input_file = '../my_input.txt'


if __name__ == '__main__':

    total_overlaped_pairs = 0

    with open(input_file) as sections_file:

        for pair in sections_file:
            pair = pair.strip('\n')
            section_ranges = pair.split(',')

            range_a = Range(section_ranges[0])
            range_b = Range(section_ranges[1])

            if range_a.overlaps(range_b):
                total_overlaped_pairs += 1

    print("Total amount of overlaped pairs is {}".format(total_overlaped_pairs))
