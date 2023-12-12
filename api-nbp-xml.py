import xml.etree.ElementTree as ET

import requests as re

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = re.get(url)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x000002486DF26E80>

table_name = root.find(".//Table").text
print(table_name)

# <Rate>
#                 <Currency>bat (Tajlandia)</Currency>
#                 <Code>THB</Code>
#                 <Mid>0.1127</Mid>
#             </Rate>
rates = root.findall('.//Rate')
print(type(rates))
for rate in rates:
    # print(rate)
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"Currency: {currency}: code: {code} mid: {mid}")
