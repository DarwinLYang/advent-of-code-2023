from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def main():
  def is_valid(original_x, original_y):
    for x in range(max(original_x - 1, 0), min(original_x + 2, max_x)):
      for y in range(max(original_y - 1, 0), min(original_y + 2, max_y)):
        value = grid[x][y]
        if not value.isdigit() and value != '.':
          return True
    return False

  input = input_to_list()
  grid = [list(row.strip()) for row in input]

  max_x = len(grid)
  max_y = len(grid[0])

  total = 0

  for x, row in enumerate(grid):
    valid = False
    saved_num = ''
    for y, value in enumerate(row):
      if value.isdigit():
        valid = is_valid(x, y)
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
