# funkcja zagnieżdżona
def fun1():
    print("To jest fun1")

    def fun2():  # definicja funkcji - zapamięta adres
        print("To jest fun2")

    return fun2


print(fun1())  # <function fun1.<locals>.fun2 at 0x0000026AE3A88EE0>
xFun = fun1()
print(xFun)
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
