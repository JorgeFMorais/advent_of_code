
from day_2.rps import RockPaperSissors

input_file = 'my_input.txt'


if __name__ == '__main__':

    game = RockPaperSissors()

    with open(input_file) as rock_paper_sizzors_file:

        for rps_line in rock_paper_sizzors_file:

            rps_split = rps_line.strip('\n').split(' ')
            player_a = rps_split[0]
            player_b = rps_split[1]

            game.play(player_a, player_b)

    print(game.score_b)
