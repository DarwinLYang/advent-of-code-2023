from pathlib import Path

def input_to_list():
  with open(Path(__file__).with_name('input.txt')) as f:
    return [line.strip() for line in f]

def main():
  input = input_to_list()

if __name__ == "__main__":
  main()
