a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 8
    b = 8
    print(a + b)


print("Zmienna a z góry", a)
dodaj()
print("Zmienna a z góry", a)
dodaj2()
print("Zmienna a z góry", a)
dodaj3()  # 16
print("Zmienna a z góry", a)  # Zmienna a z góry 8
dodaj2()  # 18
