import sys
from pathlib import Path

script_folder = Path(sys.path[0])

if len(sys.argv) > 1:
  day_index = sys.argv[1]
else:
  day_index = input("Enter day: ")

source = f'''
from adventofcoderunner import dayrunner

class Day{day_index}(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    return dayrunner.RunResult(
      part_1_answer=None,
      part_2_answer=None,
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day{day_index}, {day_index})
'''

source = source.lstrip()

with open(script_folder / f'day{day_index}.py', 'w') as file:
  file.write(source)