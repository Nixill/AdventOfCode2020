from adventofcoderunner import dayrunner

class Day3(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    trees = 0
    pos = 0
    # I'm intentionally burning a line here.
    width = len(self.input.next_line())

    for l in self.input.all_lines():
      pos += 3
      pos %= width
      if l[pos] == '#':
        trees += 1

    return dayrunner.RunResult(
      part_1_answer=trees,
      part_2_answer=None,
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day3, 3)
