from adventofcode2020 import dayrunner

def find_product_for_sum(nums: list[int], sum: int, count: int) -> int:
  result = find_product_for_sum_r(nums, sum, count)
  if result == -1:
    raise ValueError('No answer found!')
  else:
    return result

def find_product_for_sum_r(nums: list[int], sum: int, count: int) -> int:
  if count == 1:
    return sum if sum in nums else -1
  
  for i in range(count-1, len(nums)):
    this = nums[i]
    if this > sum:
      return -1
    result = find_product_for_sum_r(nums[:i], sum - this, count - 1)
    if result != -1:
      return result * this

  return -1

class Day1(dayrunner.DayCode):
  def run(self) -> dayrunner.RunResult:
    numbers = sorted(int(l) for l in self.input.all_lines())

    return dayrunner.RunResult(
      part_1_answer=find_product_for_sum(nums=numbers, sum=2020, count=2),
      part_2_answer=find_product_for_sum(nums=numbers, sum=2020, count=3)
    )

if __name__ == '__main__':
  dayrunner.run_code_for_day(Day1, 1)