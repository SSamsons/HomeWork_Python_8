import csv
log = open('log.txt', 'w')
def webcc_analis(n):
  name = n[0]
  device_type = n[1]
  browser = n[2]
  sex = n[3]
  age = n[4]
  bill = n[5]
  region = n[6]
  def gender(sex):
    if sex == 'female':
      return 'женского пола'
    else:
      return 'мужского пола'
  def years(age):
    if age.isdigit() == 1:
      age = int(age)
    else:
      age = float(age)
    wf = 'лет'
    if (age // 10) % 10 != 1:
      if age % 10 == 1:
        wf = 'год'
      elif age % 10 in (2, 3, 4):
        wf = 'года'
    return f'{age} {wf}'
  def genderdo(sex):
    if sex == 'female':
      return 'совершила'
    else:
      return 'совершил'
  def device(device_type):
    if device_type == 'mobile':
      return 'с мобильного браузера'
    else:
      return 'с десктопного браузера'
  return (
      f'Пользователь {name} {gender(sex)}, {years(age)} {genderdo(sex)} покупку на '
      f'{bill} у.е. {device(device_type)} {browser}. '
      f'Регион, из которого совершалась покупка: {region}.\n')

with open("web_clients_correct.csv", encoding='utf-8') as webcc_file:
  webcc_reader = csv.reader(
      webcc_file,
      delimiter=",")
  next(webcc_reader)
  for n in webcc_reader:
    log.write(webcc_analis(n))
