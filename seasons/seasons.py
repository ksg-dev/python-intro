from datetime import date

import inflect

p = inflect.engine()

def main():
  bday_minutes = get()
  if bday_minutes:
    print(p.number_to_words(bday_minutes, andword=""), 'minutes')

def get():
  try:
    birthday = date.fromisoformat(input('Date of Birth: '))
    today = date.today()
    age = today - birthday
    x = age.total_seconds() / 60
    return (round(x))
  except TypeError:
    print('Invalid date')
  except ValueError:
    print('Invalid date')

if __name__ == '__main__':
  main()

