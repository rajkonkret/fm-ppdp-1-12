tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
tekst2 = tekst.upper()
print(tekst)  # Witaj świecie
print(tekst2)  # WITAJ ŚWIECIE
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie
# teksty są niemutowalne

tekst3 = tekst.lower()
print(tekst3)  # witaj świecie
print(tekst)  # Witaj świecie

print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst)

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
# \x  - dane w systemie szesnastkowym
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 0, 1,2,3 = 5,6,7,8 z prawej zbior otwarty
print(tekst.count("i", 5, 9))  # 0, 1,2,3 = 5,6,7,8 z prawej zbior otwarty
print(tekst.count("j", 0, 4))  # 0, 1,2,3 = 5,6,7,8 z prawej zbior otwarty
# "Witaj świecie" 0

imie = "Radek"
# f -string - string sformatowany
tekst_format = f"\tMam na imię {imie}\n i lubie pythona.\b Dodatkowe zdanie"
print(tekst_format)
# \t tabulator
# \n znak nowej lini
# \b  backspace

starszy = "Witaj %s!"
print(starszy % imie)

print("Witaj {}!".format(imie))  # Witaj Radek!

print("""
tekst
    wielolinijkowy
    """)
# tekst
#     wielolinijkowy
