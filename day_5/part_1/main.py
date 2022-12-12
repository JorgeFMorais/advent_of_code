
import re

input_file = '../my_input.txt'


if __name__ == '__main__':

    crate_dict = {}
    loaded = False

    with open(input_file) as cargo_crates_file:

        for line in cargo_crates_file:
            line = line.strip('\n')

            if not line:
                loaded = True
                continue

            # Load cargo state
            if not loaded:
                for cargo in re.finditer('\[', line):
                    index = cargo.start() + 1

                    id = line[index]
                    stack = int(index / 4 + 0.75)

                    if crate_dict.get(stack):
                        crate_dict[stack].append(id)
                    else:
                        crate_dict[stack] = [id]

            # Perform cargo movements
            else:
                parse = re.findall('\d+', line)
                num_crates_2_move = int(parse[0])
                start_stack = int(parse[1])
                end_stack = int(parse[2])

                for __ in range(num_crates_2_move):
                    crate = crate_dict[start_stack].pop(0)
                    crate_dict[end_stack].insert(0, crate)

    top_crates = ''
    for stack in sorted(crate_dict):
        top_crates += crate_dict[stack][0]

    print("Crates at top of the stack are {}".format(top_crates))
