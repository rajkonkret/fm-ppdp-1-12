# argumenty słownikowe
def connect(**opcje):
    print(opcje)
    print(type(opcje))
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }

    connect_param['pwd'] = opcje
    print(connect_param)
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 9, 'name': 'Radek'}}


connect()  # {} <class 'dict'>
connect(a=9, name="Radek")  # {'a': 9, 'name': 'Radek'}
