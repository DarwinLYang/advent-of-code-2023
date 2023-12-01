from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f]
  return lines

def word_to_num(word):
  if word == 'one':
    return '1'
  if word == 'two':
    return '2'
  if word == 'three':
    return '3'
  if word == 'four':
    return '4'
  if word == 'five':
    return '5'
  if word == 'six':
    return '6'
  if word == 'seven':
    return '7'
  if word == 'eight':
    return '8'
  if word == 'nine':
    return '9'
  return ''

def set_nums(first_num, second_num, letter):
  if letter.isnumeric():
    if first_num == '':
      return letter, second_num
    return first_num, letter
  return first_num, second_num


def main():
  input = input_to_list()

  total = 0
  for line in input:
    first_num = ''
    second_num = ''
    maybe_word_num = []
    
    for letter in line:
      maybe_word_num = [maybe_word + letter for maybe_word in maybe_word_num]
      maybe_word_num.append(letter)

      for maybe_word in maybe_word_num:
        first_num, second_num = set_nums(first_num, second_num, word_to_num(maybe_word))
      first_num, second_num = set_nums(first_num, second_num, letter)

      if letter.isnumeric():
        maybe_word_num = []

    total += int(first_num + second_num)

  print(total)

main()
