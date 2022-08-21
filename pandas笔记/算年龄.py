import datetime

id_card = '000000199912120000'
birth_year = int(id_card[6:10])
today_year = datetime.date.today().year
how_old = today_year - birth_year
print('今年{}岁'.format(how_old))


