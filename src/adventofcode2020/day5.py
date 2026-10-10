from adventofcoderunner import dayrunner

def get_seat(code: str) -> int:
  return int(''.join([('0' if c in 'FL' else '1') for c in code]), 2)

class Day5(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    seats = {get_seat(line) for line in self.input.all_lines()}
    empty_seats = {i for i in range(128 * 8) if i not in seats}
    my_seat = {i for i in empty_seats if (i+1) in seats and (i-1) in seats} if self.input.process_p2 else {None}

    return dayrunner.RunResult(
      part_1_answer=max(seats),
      part_2_answer=my_seat.pop(),
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day5, 5)
