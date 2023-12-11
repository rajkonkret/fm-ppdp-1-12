#  wielodziedziczenie
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy \"B\"")  # Metoda z klasy "B"


class C(B, A):  # kolejność ma znaczenie
    """
    Klasa C dziedziczy po klasie A i B
    """

    def method(self):
        print("Metoda z klasy C")  # Metoda z klasy C
        super().method()  # Metoda z klasy "B"
        A.method(self)  # Metoda z klasy A


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()  # Metoda z klasy "B"
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>,
# <class '__main__.A'>, <class 'object'>)
