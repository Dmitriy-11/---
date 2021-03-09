from Valute.main.Parsing import Parsing

pars = Parsing('http://www.cbr.ru/scripts/XML_daily.asp?')
data = pars.getResult()
for valute in data:
    print('1 ', valute.get("name"), ' = ', valute.get("value"), ' рублей.\n')
