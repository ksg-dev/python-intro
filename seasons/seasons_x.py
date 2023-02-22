from datetime import date

import inflect

p = inflect.engine()

def main():
  age_day = get()
  bday_minutes = age_minutes(age_day)
  if bday_minutes:
    print(p.number_to_words(bday_minutes, andword=""), 'minutes')

def get():
  try:
    birthday = date.fromisoformat(input('Date of Birth: '))
    today = date.today()
    age = today - birthday
    return age
  except TypeError:
    print('Invalid date')
  except ValueError:
    print('Invalid date')

def age_minutes(age):
  x = age.total_seconds() / 60
  return(round(x))

if __name__ == '__main__':
  main()