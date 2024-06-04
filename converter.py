from utils import print_separator

B_to_R_rate = 2.45
B_to_D_rate = 36.5


def get_dollars_and_rub():
  while True:
    print_separator()
    bath = input('Стоимость в батах: ')
    if bath:
      try:
        bath = float(bath)
        print(f'==> {round(bath/B_to_D_rate, 2)} $\n==> {round(bath*B_to_R_rate, 2)} ₽')
        return True
      except ValueError:
        print(f'enter correct data or tap enter to exit\n{"="*10}')
    else: 
      return False


def to_rub_converter(bath):
  return f'{round(bath*B_to_R_rate, 2)}'
  

if __name__ == '__main__':
  get_dollars_and_rub()
    
