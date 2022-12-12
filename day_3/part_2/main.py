
input_file = '../my_input.txt'


def item_2_priority(item):
    ascii_value = ord(item)
    if item.isupper():
        return ascii_value - 38
    if item.islower():
        return ascii_value - 96


if __name__ == '__main__':

    total_priorities = 0
    elf_group_set = None
    counter = 0

    with open(input_file) as rucksack_file:

        for rucksack_line in rucksack_file:
            rucksack_line = rucksack_line.strip('\n')

            elf_rucksack_set = set(rucksack_line)
            if elf_group_set:
                elf_group_set = elf_group_set.intersection(elf_rucksack_set)
            else:
                elf_group_set = elf_rucksack_set

            counter += 1

            if counter == 3:
                for badge in elf_group_set:
                    total_priorities += item_2_priority(badge)
                counter = 0
                elf_group_set = None

    print("Total sum of repeated item priorities is {}".format(total_priorities))
