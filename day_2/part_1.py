from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def get_game_id_and_data(line):
  game_name, data = line.split(':')
  _, game_id = game_name.split(' ')

  return int(game_id), data

def main():
  total = 0

  for line in input_to_list():
    game_id, data = get_game_id_and_data(line)
    valid = True
    for round in data.split(';'):
      for cube in round.split(','):
        cube = cube.strip()
        num, colour = cube.split(' ')
        num = int(num)
        if (colour == 'red' and 12 < num) or (colour == 'green' and 13 < num) or (colour == 'blue' and 14 < num):
          valid = False
          break
      else:
        continue
      break
    
    if valid:
      total += game_id

  print(total)

main()
