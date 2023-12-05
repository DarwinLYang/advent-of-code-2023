from collections import defaultdict
from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    return [line.strip() for line in f]

def build_maps(input):
  maps = defaultdict(list)
  map_name = ''
  for line in input:
    if not len(line):
      continue
    
    if line[0].isalpha():
      map_name = line.split()[0].split('-to-')[0]
    else:
      dest, source, map_range = line.split()
      maps[map_name].append((int(source), int(dest), int(map_range)))

  for map_key in maps.keys():
    maps[map_key].sort()

  return maps

def next_values(map, values, m_index, v_index) -> list:
  if v_index >= len(values):
    return []
  if m_index >= len(map):
    return values[v_index:]

  source, dest, map_range = map[m_index]
  value, value_range = values[v_index]

  if value_range == 0:
    return next_values(map, values, m_index, v_index + 1)

  if value < source:
    range_used = min(source - value, value_range)
    values[v_index] = (value + range_used, value_range - range_used)
    return next_values(map, values, m_index, v_index) + [(value, range_used)]
  elif value < source + map_range:
    range_used = min(source - value + map_range, value_range)
    values[v_index] = (value + range_used, value_range - range_used)
    return next_values(map, values, m_index, v_index) + [(dest + value - source, range_used)]
  else:
    return next_values(map, values, m_index + 1, v_index)

def main():
  input = input_to_list()

  next_map = {
    'seed': 'soil',
    'soil': 'fertilizer',
    'fertilizer': 'water',
    'water': 'light',
    'light': 'temperature',
    'temperature': 'humidity',
    'humidity': 'location'
  }
  maps = build_maps(input[2:])

  initial_values = [int(v) for v in input[0].split(': ')[1].split()]
  values = []
  for i in range(0, len(initial_values), 2):
    values.append((initial_values[i], initial_values[i + 1]))
  values.sort()

  map_name = 'seed'
  while map_name != 'location':
    values = sorted(next_values(maps[map_name], values, 0, 0))
    map_name = next_map[map_name]
  
  print(sorted(values)[0][0])

if __name__ == "__main__":
  main()
