import requests
from decimal import *
from requests import get, utils


def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content_parts = content.strip('/').split(' ')
    str_content = "".join(content_parts)
    # print(type(str_content))
    if val not in str_content:
        return None
    rub = str_content[str_content.find('<Value', str_content.find(val)) + 7:str_content.find('</Value>', str_content.find(val))]
    return  f"{Decimal(rub.replace(',', '.'))}"

print(currency_rates('usd'))
print(currency_rates('evr'))
print(currency_rates('EUR'))