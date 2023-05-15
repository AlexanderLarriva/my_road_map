from collections import Counter
from datetime import datetime


def get_men_counted_by_year(users):
  result = []
  for i in users:
    if 'male' in i.values():
      Year = datetime.strptime(i['birthday'], '%Y-%m-%d').year
      result.append(Year)
  return Counter(result)


users = [
    {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
    {'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
    {'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
    {'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
    {'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
    {'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
    {'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
    {'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
]

print(type(users))

print(get_men_counted_by_year(users))
print(type(get_men_counted_by_year(users)))
c = Counter([1,2,3,1,2,3])
d = Counter({1973: 'male', 1973: 'male'})
print(c)
print(d)

print('male' in {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'}.values()) #проверка мужик

MyDict = {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'}

ds3 = '1973-03-23'
dt3 = datetime.strptime(ds3, '%Y-%m-%d').year #получить год
print(datetime.strptime(MyDict['birthday'], '%Y-%m-%d').year)
# print(dt3.date())
# print(dt3.year)
# print(dt3.month)
# print(dt3.day)
print(dt3)

# from datetime import datetime
# datetime.strptime('2014-12-04', '%Y-%m-%d').date()
# datetime.date(2014, 12, 4)