import json
from bs4 import BeautifulSoup

class JsonExtractor:
    def extractHiddenData(htmlText):
        htmlSoup = BeautifulSoup(htmlText, 'html.parser')
        jsonText = htmlSoup.find('script', id="__NEXT_DATA__").text
        return json.loads(jsonText)