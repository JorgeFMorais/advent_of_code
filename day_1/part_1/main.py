
from day_1.elf import Elf

input_file = '../my_input.txt'


if __name__ == '__main__':

    top_elf = Elf(0)
    current_elf = Elf(1)

    with open(input_file) as elves_calories_file:

        for calories_line in elves_calories_file:

            calories_num = calories_line.strip('\n')
            if calories_num:
                current_elf.add_calories(int(calories_num))
            else:
                current_elf = Elf(current_elf.number + 1)

            if current_elf.calories > top_elf.calories:
                top_elf = current_elf

    print(top_elf)
