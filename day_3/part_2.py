from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def main():
  def get_gears(original_x, original_y):
    seen = set()
    for x in range(max(original_x - 1, 0), min(original_x + 2, max_x)):
      for y in range(max(original_y - 1, 0), min(original_y + 2, max_y)):
        if (x,y) not in seen and grid[x][y] == '*':
          seen.add((x,y))
    return seen

  input = input_to_list()
  grid = [list(row.strip()) for row in input]
  gear_grid = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

  max_x = len(grid)
  max_y = len(grid[0])

  total = 0

  for x, row in enumerate(grid):
    saved_num = ''
    gears = set()

    for y, value in enumerate(row):
      if value.isdigit():
        gears.update(get_gears(x, y))
        saved_num += value
      else:
        if saved_num:
          for gear_x, gear_y in gears:
            gear_grid[gear_x][gear_y].append(int(saved_num))
          saved_num = ''
          gears = set()
    if saved_num:
      for gear_x, gear_y in gears:
        gear_grid[gear_x][gear_y].append(int(saved_num))

  for gear_row in gear_grid:
    for gear_nums in gear_row:
      if len(gear_nums) == 2:
        total += gear_nums[0] * gear_nums[1]

  print(total)



main()
