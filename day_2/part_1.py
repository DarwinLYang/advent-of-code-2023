from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt'), 'r') as f:
    lines = [line for line in f]
  return lines

def get_game_id_and_data(line):
  game_name, data = line.split(':')
  return int(game_name.split(' ')[1]), data

def main():
  colour_to_max = {
    'red': 12,
    'green': 13,
    'blue': 14,
  }
  total = 0

  for line in input_to_list():
    game_id, data = get_game_id_and_data(line)
    for round in data.split(';'):
      for cube in round.split(','):
        num, colour = cube.strip().split()
        if int(num) > colour_to_max[colour]:
          game_id = 0
          break
      else:
        continue
      break

    total += game_id

  print(total)

main()
