import datetime
from utils import print_separator


def log_in_file(price, user_string=None):
  data = datetime.datetime.now().strftime('%Y.%m.%d %H:%M')
  print(0)
  with open('logfile.txt', mode='a', encoding='utf-8') as file:
    file.write(f'{data}: {price} ฿ - {user_string}\n')
  print_separator()
  print(f'==> {user_string} for {price} ฿ added')
    

if __name__ == '__main__':
  log_in_file(input('test: '))

