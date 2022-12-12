from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def __init__(self, range_str):
        range_split = range_str.split('-')
        self.start = int(range_split[0])
        self.end = int(range_split[1])

    def fully_contains(self, other):
        return self.start <= other.start and other.end <= self.end

    def overlaps(self, other):
        return self.start <= other.end and other.start <= self.end
