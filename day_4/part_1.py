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
  
  points = 0
  for card in input:
    winning_nums, my_nums = split_card(card)
    number_of_wins = len(winning_nums.intersection(my_nums))
    if number_of_wins > 0:
      points += 2**(number_of_wins - 1)

  print(points)

if __name__ == "__main__":
  main()
