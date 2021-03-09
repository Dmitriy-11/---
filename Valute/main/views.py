from django.shortcuts import render
from . import Parsing
import requests
import xml.etree.ElementTree as ET


def getRes():
    # list for all result
    lst_result = []

    result = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?')
    # if a answer is received successfully
    if result.status_code == 200:
        # getting content from answer
        content = ET.fromstring(result.content)
        list_valute = content.findall("./Valute")
        for valute in list_valute:
            name = valute.find("./Name").text
            value = float(valute.find("./Value").text.replace(',', '.'))
            lst_result.append({"name": name, "value": value})
    return lst_result


def index(request):
    dt = getRes()
    data = {
        'data': dt
    }
    return render(request, 'main/index.html', data)
