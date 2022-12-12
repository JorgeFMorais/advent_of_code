
from dataclasses import dataclass


@dataclass
class RockPaperSissors:

    # Evaluation tables for possible inputs
    outcome_dict = {
        'A': {'X': 0, 'Y': -1, 'Z': 1},
        'B': {'X': 1, 'Y': 0, 'Z': -1},
        'C': {'X': -1, 'Y': 1, 'Z': 0}
    }

    shape_score = {
        'A': 1, 'B': 2, 'C': 3,
        'X': 1, 'Y': 2, 'Z': 3
    }

    outcome_score = {
        -1: 0,
        0: 3,
        1: 6
    }

    force_outcome_dict = {
        'X': 1,
        'Y': 0,
        'Z': -1
    }

    score_a: int = 0
    score_b: int = 0

    def calculate_scores(self, input_a, input_b, result):
        self.score_a += self.shape_score[input_a] + self.outcome_score[result]
        self.score_b += self.shape_score[input_b] + self.outcome_score[result * -1]

    def play(self, input_a, input_b):
        result = self.outcome_dict[input_a][input_b]
        self.calculate_scores(input_a, input_b, result)

    def force_outcome(self, input_a, outcome):
        result = self.force_outcome_dict[outcome]

        input_b = None
        for expected_input, expected_result in self.outcome_dict[input_a].items():
            if result == expected_result:
                input_b = expected_input
                break

        self.calculate_scores(input_a, input_b, result)

