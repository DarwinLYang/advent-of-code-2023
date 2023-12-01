from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def main():
  input = input_to_list()

  total = 0
  for line in input:
    first_num = ''
    second_num = ''
    for letter in line:
      if letter.isnumeric():
        if first_num == '':
          first_num = letter
        second_num = letter
    total += int(first_num + second_num)

  print(total)

main()
