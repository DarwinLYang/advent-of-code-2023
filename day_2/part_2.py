from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def main():
  total = 0

  for line in input_to_list():
    _, data = line.split(':')
    red = 0
    green = 0
    blue = 0

    for round in data.split(';'):
      for cube in round.split(','):
        cube = cube.strip()
        num, colour = cube.split(' ')
        if colour == 'red':
          red = max(red, int(num))
        elif colour == 'green':
          green = max(green, int(num))
        elif colour == 'blue':
          blue = max(blue, int(num))
    
    total += red * green * blue

  print(total)

main()
