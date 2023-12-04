from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-12-04

time = datetime.now()
print(time)  # 2023-12-04 15:37:56.955819

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2023-12-05

print(time.hour)
print(today.day)

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 04/12/2023

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 15:41

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 200.0},
]

for product in products:
    # print(product)  # {'sku': 3, 'exp_date': datetime.date(2023, 12, 4), 'price': 200.0}
    if product['exp_date'] != today:
        continue
    product['price'] *= 0.8
    print(f"""
    Price for sku {product['sku']}
    is now {product['price']}""")
