import re
from dataclasses import dataclass

from adventofcoderunner import dayrunner

def try_int(text: str) -> int | None:
  try:
    return int(text)
  except ValueError:
    return None

color_regex = re.compile(r'^#[0-9a-fA-F]{6}$')
height_regex = re.compile(r'^(\d+)(in|cm)$')

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
    if birth_year > 2002: return False, "Too young to travel"
    if birth_year < 1920: return False, "Too old to travel"
    issue_year = try_int(self.iyr)
    if not issue_year: return False, "Issue year isn't number"
    if issue_year > 2020: return False, "Issued in the future"
    if issue_year < 2010: return False, "Issued too long ago"
    expiry_year = try_int(self.eyr)
    if not expiry_year: return False, "Expiry year isn't number"
    if expiry_year < 2020: return False, "Expired in the past"
    if expiry_year > 2030: return False, "Valid for too long"
    height = height_regex.match(self.hgt)
    if not height: return False, "Height isn't inches or centimeters"
    if height.group(2) == 'in':
      inches = int(height.group(1))
      if inches < 59: return False, "Too short to travel (in inches)"
      if inches > 76: return False, "Too tall to travel (in inches)"
    else:
      cm = int(height.group(1))
      if cm < 150: return False, "Too short to travel (in centimeters)"
      if cm > 193: return False, "Too tall to travel (in centimeters)"
    hair_color = color_regex.match(self.hcl)
    if not hair_color: return False, "Hair color isn't color"
    eye_color = self.ecl
    if eye_color not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False, "Invalid eye color"
    passport_id = try_int(self.pid)
    if not passport_id: return False, "Passport ID isn't number"
    if len(self.pid) > 9: return False, "Passport ID too long"
    if len(self.pid) < 9: return False, "Passport ID too short"
    return True, "Success"

class Day4(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    valid_p1 = 0
    valid_p2 = 0

    for t in self.input.block_iterable():
      pp = Day4Passport.parse_passport(t)

      if pp.is_loosely_valid():
        valid_p1 += 1
        validity, reason = pp.is_strictly_valid()
        if validity:
          valid_p2 += 1

    return dayrunner.RunResult(
      part_1_answer=valid_p1,
      part_2_answer=valid_p2,
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day4, 4)
