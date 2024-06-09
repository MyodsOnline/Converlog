import re
from converter import to_rub_converter
from utils import print_separator

def read_logfile():
  '''
  открыть текстовый файл лога
  вернуть список строк
  '''
  with open('logfile.txt', 'r', encoding='utf-8') as file:
    log_data = []
    for line in file:
      text = line.strip()
      if text:
        line = text.split(" ")
        log_data.append(line)
  return log_data


def print_data(data_list):
  print_separator()
  data = data_list
  for item in data:
    print(' '.join(item))


def print_total(data):
  numbers_list = []
  print_separator()
  if data:
    for el in data:
      try:
        cnt = float(el[2])
        numbers_list.append(cnt)
      except ValueError:
        numbers_list.append(0)
    totat_cost_B = sum(numbers_list)
    totat_cost_R = to_rub_converter(totat_cost_B)
    print(f'Total cost - {totat_cost_B} ฿ / {totat_cost_R} ₽')
  else:
    print(f'nothing to calculate')


def extract_number():
  log_data = read_logfile()
  print_data(log_data)
  print_total(log_data)
  

def count_by_category():
  print_separator()
  user_input = input('Искомая строка: ')
  data = read_logfile()
  category_data = []
  for item in data:
    if item[0] != '_':
      for element in item:
        if user_input in element:
          category_data.append(item)
  print_data(category_data)
  print_total(category_data)

        
      
if __name__ == '__main__':
  #log_data = read_logfile()
  #extract_number()
  #print(log_data)
  count_by_category()
