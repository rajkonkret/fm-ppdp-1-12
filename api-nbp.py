from typing import List
import os
from pydantic import BaseModel
import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
data = response.json()
print(data)
print(data['rates'][0]['mid'])  # 4.3396


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class CurrencyInfo(BaseModel):
    table: str
    code: str
    rates: List[Rate]


currency_info = CurrencyInfo(**data)
print(currency_info)
print("Kurs eur:", currency_info.rates[0].mid)
