from day_1.elf import Elf

input_file = 'my_input.txt'

if __name__ == '__main__':

    elves_dict = {}
    current_elf = Elf(1)

    with open(input_file) as elves_calories_file:

        for calories_line in elves_calories_file:

            calories_num = calories_line.strip('\n')
            if calories_num:
                current_elf.add_calories(int(calories_num))
            else:
                current_elf = Elf(current_elf.number + 1)

            elves_dict[current_elf.number] = current_elf

    top_3_elves = sorted(elves_dict.values(), key=lambda elf: elf.calories, reverse=True)[0:3]

    total = 0
    for top_elf in top_3_elves:
        total += top_elf.calories
        print(top_elf)

    print("The Elves are carrying a total of {} calories".format(total))
