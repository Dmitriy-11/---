import requests
import xml.etree.ElementTree as ET


class Parsing(object):

    def __init__(self, url):
        self.url = url

    def getResult(self):
        # list for all result
        lst_result = []

        result = requests.get(self.url)
        # if a answer is received successfully
        if result.status_code == 200:
            # getting content from answer
            content = ET.fromstring(result.content)
            list_valute = content.findall("./Valute")
            for valute in list_valute:
                name = valute.find("./Name").text
                value = valute.find("./Value").text
                lst_result.append({"name": name, "value": value})
        return lst_result

