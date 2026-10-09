from dataclasses import dataclass
from typing import NamedTuple

from adventofcoderunner import dayrunner
import re

day2_regex = re.compile(r'(\d+)-(\d+) (.): (.+)')

class Day2Line:
  min_chars: int
  max_chars: int
  letter: str
  password: str
  password_length: int
  password_letter_count: int

  def __init__(self, line: str):
    match = day2_regex.match(line)
    if not match:
      raise ValueError("Doesn't match format.")

    self.min_chars = int(match.group(1))
    self.max_chars = int(match.group(2))
    self.letter = match.group(3)
    self.password = match.group(4)
    self.password_length = len(self.password)
    self.password_letter_count = len([a for a in self.password if a == self.letter])

class Day2(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    passwords = [Day2Line(l) for l in self.input.all_lines()]
    p1 = 0
    p2 = 0

    for p in passwords:
      if p.password_letter_count >= p.min_chars and p.password_letter_count <= p.max_chars:
        p1 += 1

        # This is a guess as to what part 2 is! :D
        if p.password_length >= p.min_chars and p.password_length <= p.max_chars:
          p2 += 1

    return dayrunner.RunResult(
      part_1_answer=p1,
      part_2_answer=p2,
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day2, 2)