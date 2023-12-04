from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    return [line.strip() for line in f]

def split_card(card):
  _, nums = card.split(':')
  winning_nums, my_nums = nums.split('|')
  return set(winning_nums.split()), set(my_nums.split())

def main():
  input = input_to_list()
  
  copies = {i: 1 for i in range(len(input))}
  for id, card in enumerate(input):
    winning_nums, my_nums = split_card(card)
    number_of_wins = len(winning_nums.intersection(my_nums))
    for copy_id in range(id + 1, min((id + 1) + number_of_wins, len(copies))):
      copies[copy_id] += copies[id]

  total_count = 0
  for count in copies.values():
    total_count += count

  print(total_count)

if __name__ == "__main__":
  main()
