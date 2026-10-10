from adventofcoderunner import dayrunner

def get_seat(code: str) -> int:
  return int(''.join([('0' if c in 'FL' else '1') for c in code]), 2)

class Day5(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    seats = {get_seat(line) for line in self.input.all_lines()}

    return dayrunner.RunResult(
      part_1_answer=max(seats),
      part_2_answer=None,
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day5, 5)
