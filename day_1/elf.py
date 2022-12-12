
from dataclasses import dataclass, field


@dataclass(order=True)
class Elf:
    number: int
    calories: int = 0

    def add_calories(self, calories):
        self.calories += calories

    def __str__(self):
        return "Elf {} is carrying {} calories".format(self.number, self.calories)