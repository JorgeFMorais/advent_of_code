
input_file = '../my_input.txt'


if __name__ == '__main__':

    counter = 13
    start_of_message = ''

    with open(input_file) as signal_file:

        line = signal_file.readline()
        start_of_message = line[0:13]

        for letter in line[13:]:
            start_of_message += letter
            counter += 1

            if len(set(start_of_message)) == 14:
                break

            start_of_message = start_of_message[1:]

    print(counter)
    print(start_of_message)
