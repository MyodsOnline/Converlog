from converter import get_dollars_and_rub
from logfile import log_in_file
from read_log import read_logfile, extract_number
from utils import print_separator


def counter():
  while True:
    print_separator()
    option = input('Select: \n1 | e - конвертация бата\n2 | s - записать расходы\n3 | p - вывести отчет\n4 | q - выход\n')
    
    if option == '4' or option == 'q':
      print('bye 🫶')
      print_separator()  
      return False
      #break
    elif option == '1' or option == 'e':
      get_dollars_and_rub()
    elif option == '2' or option == 's':
      print_separator()
      log_in_file(input('Расход: '), input('Цель: '))
    elif option == '3' or option == 'p':
      extract_number()
    else:
      print(f'странный выбор {option} 🤮')

  
  
if __name__ == '__main__':
  counter()
  
