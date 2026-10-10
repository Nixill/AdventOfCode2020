import re
from dataclasses import dataclass

from adventofcoderunner import dayrunner

def try_int(text: str) -> int | None:
  try:
    return int(text)
  except ValueError:
    return None

color_regex = re.compile(r'^#[0-9a-fA-F]{6}$')
height_regex = re.compile(r'^\d+(in|cm)$')

@dataclass(frozen=True)
class Day4Passport:
  byr: str = ''
  '''Birth year'''

  iyr: str = ''
  '''Issue year'''

  eyr: str = ''
  '''Expiration year'''

  hgt: str = ''
  '''Height'''

  hcl: str = ''
  '''Hair color'''

  ecl: str = ''
  '''Eye color'''

  pid: str = ''
  '''Passport ID'''

  cid: str = ''
  '''Country ID'''

  @staticmethod
  def parse_passport(text: str) -> Day4Passport:
    fields = text.split()
    kvps = [t.split(':') for t in fields]
    d = {t[0]: t[1] for t in kvps}

    return Day4Passport(**d)

  def is_loosely_valid(self) -> bool:
    return bool(self.byr
      and self.eyr
      and self.ecl
      and self.hcl
      and self.hgt
      and self.iyr
      and self.pid)

  # A guess at part two!
  def is_strictly_valid(self) -> tuple[bool, str]:
    if not self.is_loosely_valid(): return False, 'Not even loosely valid'
    birth_year = try_int(self.byr)
    if not birth_year: return False, "Birth year isn't number"
    issue_year = try_int(self.iyr)
    if not issue_year: return False, "Issue year isn't number"
    if birth_year > issue_year: return False, "Issued before birth"
    if issue_year > 2020: return False, "Issued after 2020"
    expiry_year = try_int(self.eyr)
    if not expiry_year: return False, "Expiry year isn't number"
    if expiry_year < 2020: return False, "Expired before 2020"
    height = height_regex.match(self.hgt)
    if not height: return False, "Height isn't inches or centimeters"
    hair_color = color_regex.match(self.hcl)
    if not hair_color: return False, "Hair color isn't color"
    eye_color = self.ecl
    if len(eye_color) != 3: return False, "Eye color isn't color name"
    passport_id = try_int(self.pid)
    if not passport_id: return False, "Passport ID isn't number"
    if self.cid:
      country_id = try_int(self.cid)
      if not country_id: return False, "Country ID isn't number"
    return True, "Success"

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
