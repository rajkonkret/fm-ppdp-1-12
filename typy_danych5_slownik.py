# słownik - para: klucz wartość
# {'name' : 'Radek'}
# klucze nie mogą się powtarzac

my_dict = {"A": 'one', 'B': 'two', 'C': 'three'}
print(type(my_dict))  # <class 'dict'>
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three'}

# tworzenie pustego słownika
empty_dict = {}
empty_dict2 = dict()

print(empty_dict)  # {} - pusty słownik

dict_mixed = {1: 'one', 'A': 'two', 3: 'three'}
print(dict_mixed)

print(dict_mixed.keys())
print(dict_mixed.items())
print(dict_mixed.values())
# dict_keys([1, 'A', 3])
# dict_items([(1, 'one'), ('A', 'two'), (3, 'three')])
# dict_values(['one', 'two', 'three'])

dictionary = {'x': 2}
dictionary.update([('y', 2), ('z', 3)])
print(dictionary)  # {'x': 2, 'y': 2, 'z': 3}

empty_dict['imie'] = 'Radek'
print(empty_dict)  # {'imie': 'Radek'}
empty_dict['wiek'] = 39
print(empty_dict)  # {'imie': 'Radek', 'wiek': 39}
empty_dict["wiek"] = 43
print(empty_dict)  # {'imie': 'Radek', 'wiek': 43}

# wypisanie wartości zdla danego klucza
print(empty_dict['wiek'])
print(empty_dict.get('wiek'))
print(empty_dict.get('wiek2', 'default'))  # default
# print(empty_dict['wiek2'])  # KeyError: 'wiek2'
# 11:10
print(empty_dict.pop('wiek'))
empty_dict['age'] = 45
print(empty_dict)
print(empty_dict.popitem())  # ('age', 45)
empty_dict.clear()
print(empty_dict)  # {}

my_dict = dictionary.copy()  # kopiowanie elemntów
print(my_dict)  # {'x': 2, 'y': 2, 'z': 3}
# napisac program, ktory bedzie działał jak słownik angielsko-polski
# kaggle
# mockaroo.com
dict_word = {'name': 'imie', 'castle': 'zamek', 'water': 'woda'}
print(f"Potrafię przetłumaczyć : {dict_word.keys()}")
key = input("Podaj słowko do przetłumaczenia")  # str()
print(dict_word[key.lower().replace(" ", "")])
# input zwracas tring
a = float(input("Podaj pierwszą liczbę"))
b = input("Podaj drugą liczbę")
print(a + int(b))
