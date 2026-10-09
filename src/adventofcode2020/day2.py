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

  def __init__(self, line: str):
    match = day2_regex.match(line)
    if not match:
      raise ValueError("Doesn't match format.")

    self.min_chars = int(match.group(1))
    self.max_chars = int(match.group(2))
    self.letter = match.group(3)
    self.password = match.group(4)

  def passes_part_1(self) -> bool:
    letter_count = len([l for l in self.password if l == self.letter])
    return letter_count >= self.min_chars and letter_count <= self.max_chars

  def passes_part_2(self) -> bool:
    left_letter = self.password[self.min_chars + 1]
    right_letter = self.password[self.max_chars + 1]

    return (left_letter == self.letter) != (right_letter == self.letter)

class Day2(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    passwords = [Day2Line(l) for l in self.input.all_lines()]

    return dayrunner.RunResult(
      part_1_answer=len([p for p in passwords if p.passes_part_1()]),
      part_2_answer=len([p for p in passwords if p.passes_part_2()]),
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day2, 2)