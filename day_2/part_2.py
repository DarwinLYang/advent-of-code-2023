from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt'), 'r') as f:
    lines = [line for line in f]
  return lines

def main():
  total = 0

  for line in input_to_list():
    colour_map = {}
    for round in line.split(':')[1].split(';'):
      for cube in round.split(','):
        num, colour = cube.strip().split()
        colour_map[colour] = max(colour_map.get(colour, 0), int(num))

    product = 1
    for factor in colour_map.values():
      product *= factor
    total += product

  print(total)

main()
