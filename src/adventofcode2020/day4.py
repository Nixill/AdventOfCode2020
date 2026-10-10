import re
from dataclasses import dataclass

from adventofcoderunner import dayrunner

def try_int(d: dict[str, str], k: str) -> int | None:
  try:
    return int(d[k])
  except ValueError, KeyError:
    return None

def try_str(d: dict[str, str], k: str) -> str | None:
  try:
    return d[k]
  except KeyError:
    return None

color_regex = re.compile(r'^#[0-9a-fA-F]{6}$')
height_regex = re.compile(r'^\d+(in|cm)$')

@dataclass(frozen=True)
class Day4Passport:
  birth_year: int | None
  issue_year: int | None
  expiry_year: int | None
  height: str | None
  hair_color: str | None
  eye_color: str | None
  passport_id: int | None
  country_id: int | None

  @staticmethod
  def parse_passport(text: str) -> Day4Passport:
    fields = text.split()
    kvps = [t.split(':') for t in fields]
    d = {t[0]: t[1] for t in kvps}

    return Day4Passport(
      birth_year=try_int(d, 'byr'),
      issue_year=try_int(d, 'iyr'),
      expiry_year=try_int(d, 'eyr'),
      height=try_str(d, 'hgt'),
      hair_color=try_str(d, 'hcl'),
      eye_color=try_str(d, 'ecl'),
      passport_id=try_int(d, 'pid'),
      country_id=try_int(d, 'cid')
    )

  def is_loosely_valid(self) -> bool:
    return (self.birth_year is not None
      and self.expiry_year is not None
      and self.eye_color is not None
      and self.hair_color is not None
      and self.height is not None
      and self.issue_year is not None
      and self.passport_id is not None)

  # A guess at part two!
  def is_strictly_valid(self) -> bool:
    return (self.birth_year is not None
      and self.issue_year is not None
      and self.birth_year <= self.issue_year
      and self.issue_year <= 2020
      and self.expiry_year is not None
      and self.expiry_year >= 2020
      and self.eye_color is not None
      and len(self.eye_color) == 3
      and self.passport_id is not None
      and self.hair_color is not None
      and bool(color_regex.match(self.hair_color))
      and self.height is not None
      and bool(height_regex.match(self.height))
    )

class Day4(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    valid_p1 = 0
    valid_p2 = 0

    for t in self.input.block_iterable():
      pp = Day4Passport.parse_passport(t)

      if pp.is_loosely_valid():
        valid_p1 += 1
        if pp.is_strictly_valid():
          valid_p2 += 1

    return dayrunner.RunResult(
      part_1_answer=valid_p1,
      part_2_answer=valid_p2,
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day4, 4)
