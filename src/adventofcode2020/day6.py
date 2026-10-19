from functools import reduce
from typing import Counter, Iterable

from adventofcoderunner import dayrunner

class Day6Group:
  line_list: list[str]
  question_answers: Counter[str]

  def __init__(self, lines: Iterable[str]):
    self.line_list = list(lines)
    self.question_answers = Counter((c for l in lines for c in l))

class Day6(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    groups = [
      Day6Group(lines) for lines in self.input.block_lines_iterable()
    ]

    union = 0
    intersection = 0
    for g in groups:
      union += len(g.question_answers)
      intersection += sum((1 for v in g.question_answers.values() if v == len(g.line_list)))

    return dayrunner.RunResult(
      part_1_answer=union,
      part_2_answer=intersection,
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day6, 6)
