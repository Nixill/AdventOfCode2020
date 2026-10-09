from dataclasses import dataclass
from typing import NamedTuple
from functools import reduce

from adventofcoderunner import dayrunner

@dataclass
class Day3Run:
  deltaX: int
  deltaY: int
  x: int = 0
  y: int = 0
  trees: int = 0

class Day3(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    runs = [
      Day3Run(1, 1),
      Day3Run(3, 1),
      Day3Run(5, 1),
      Day3Run(7, 1),
      Day3Run(1, 2),
    ]

    # This statement intentionally burns the first line, so that it's not run in all_lines.
    width = len(self.input.next_line())

    for l in self.input.all_lines():
      for r in runs:
        r.y = (r.y + 1) % r.deltaY

        if r.y == 0:
          r.x = (r.x + r.deltaX) % width
          if l[r.x] == '#':
            r.trees += 1

    return dayrunner.RunResult(
      part_1_answer=runs[1].trees,
      part_2_answer=reduce(lambda p, r: p * r, map(lambda r: r.trees, runs)),
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day3, 3)
