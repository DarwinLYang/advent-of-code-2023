from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def create_valid_grid(grid):
  valid_grid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      if not value.isdigit() and value != '.':
        for valid_x in range(max(x - 1, 0), min(x + 2, len(grid))):
          for valid_y in range(max(y - 1, 0), min(y + 2, len(grid[0]))):
            valid_grid[valid_x][valid_y] = True

  return valid_grid

def main():
  input = input_to_list()
  grid = [list(row.strip()) for row in input]
  valid_grid = create_valid_grid(grid)
  
  total = 0
  for x, row in enumerate(grid):
    valid = False
    saved_num = ''
    for y, value in enumerate(row):
      if value.isdigit():
        valid = valid or valid_grid[x][y]
        saved_num += value
      else:
        if saved_num and valid:
          total += int(saved_num)
        valid = False
        saved_num = ''
    if saved_num and valid:
      total += int(saved_num)

  print(total)

main()
