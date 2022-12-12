
input_file = '../my_input.txt'


if __name__ == '__main__':

    counter = 3
    start_of_packet = ''

    with open(input_file) as signal_file:

        line = signal_file.readline()
        start_of_packet = line[0:3]

        for letter in line[3:]:
            start_of_packet += letter
            counter += 1

            if len(set(start_of_packet)) == 4:
                break

            start_of_packet = start_of_packet[1:]

    print(counter)
    print(start_of_packet)
