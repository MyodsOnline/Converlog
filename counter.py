from converter import get_dollars_and_rub
from logfile import log_in_file

from read_log import read_logfile, extract_number, count_by_category

from utils import print_separator


def counter():
  while True:
    print_separator()
    option = input('Select:\n1 | e - get exchange rate\n2 | s - записать расходы\n3 | p - вывести отчет\n4 | c - поиск и счет\n5 | q - выход\n')
    
    if option == '5' or option == 'q':
      print('bye 🫶')
      print_separator()  
      return False
      #break
    elif option == '1' or option == 'e':
      get_dollars_and_rub()
    elif option == '2' or option == 's':
      print_separator()
      log_in_file(input('Price: '), input('Aim: '))
    elif option == '3' or option == 'p':
      extract_number()
    elif option == '4' or option == 'c':
      count_by_category()
    else:
      print(f'странный выбор {option} 🤮')
  
  
  #currency = int(input('Select currency: \n1 - if US dollars\n2 - if Thai bath'))
  
  
if __name__ == '__main__':
  counter()
  
