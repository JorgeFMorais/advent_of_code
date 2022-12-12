
input_file = '../my_input.txt'


def item_2_priority(item):
    ascii_value = ord(item)
    if item.isupper():
        return ascii_value - 38
    if item.islower():
        return ascii_value - 96


if __name__ == '__main__':

    total_priorities = 0

    with open(input_file) as rucksack_file:

        for rucksack_line in rucksack_file:
            rucksack_line = rucksack_line.strip('\n')
            compartment_length = int(len(rucksack_line) / 2)
            first_compartment = rucksack_line[:compartment_length]
            second_compartment = rucksack_line[compartment_length:]

            first_set = set(first_compartment)
            second_set = set(second_compartment)

            repeated_items = first_set.intersection(second_set)

            print(repeated_items)

            for item in repeated_items:
                print(item_2_priority(item))
                total_priorities += item_2_priority(item)

    print("Total sum of repeated item priorities is {}".format(total_priorities))
