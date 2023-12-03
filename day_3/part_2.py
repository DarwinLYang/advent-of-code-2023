from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def create_gear_grid(grid):
  gear_grid = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))]
  gears = {}
  for gear_x, row in enumerate(grid):
    for gear_y, value in enumerate(row):
      if value == '*':
        gear = (gear_x,gear_y)
        gears[gear] = []
        for x in range(max(gear_x - 1, 0), min(gear_x + 2, len(grid))):
          for y in range(max(gear_y - 1, 0), min(gear_y + 2, len(grid[0]))):
            gear_grid[x][y].add(gear)

  return gear_grid, gears

def main():
  input = input_to_list()
  grid = [list(row.strip()) for row in input]
  gear_grid, gear_to_nums = create_gear_grid(grid)

  total = 0
  for x, row in enumerate(grid):
    saved_num = ''
    gears = set()

    for y, value in enumerate(row):
      if value.isdigit():
        if gear_grid[x][y]:
          gears.update(gear_grid[x][y])
        saved_num += value
      else:
        if saved_num:
          for gear in gears:
            gear_to_nums[gear].append(int(saved_num))
          saved_num = ''
          gears = set()
    if saved_num:
      for gear in gears:
        gear_to_nums[gear].append(int(saved_num))

  for nums in gear_to_nums.values():
    if len(nums) == 2:
      total += nums[0] * nums[1]

  print(total)

main()
