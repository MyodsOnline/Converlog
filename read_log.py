import re
from converter import to_rub_converter
from utils import print_separator

def read_logfile():
  with open('logfile.txt', 'r', encoding='utf-8') as file:
    log_data = []
    for line in file:
      text = line.strip()
      if text:
        line = text.split(" ")
        log_data.append(line)

  return log_data


def extract_number():
  log_data = read_logfile()
  numbers_list = []
  print_separator()
  for el in log_data:
    print(' '.join(el))
    try:
      cnt = float(el[2])
      numbers_list.append(cnt)
    except ValueError:
      numbers_list.append(0)
  print_separator()
  totat_cost_B = sum(numbers_list)
  totat_cost_R = to_rub_converter(totat_cost_B)
  print(f'Total cost - {totat_cost_B} ฿ / {totat_cost_R} ₽')

      
      
if __name__ == '__main__':
  #log_data = read_logfile()
  extract_number()
  #print(line)
  #extract_number(line)
