# stworzyc funkcji kantor
def kantor(waluta):
    print("Uruchamiam kantor")

    def usd(kwota=0):
        print("Wymieniam dolary", kwota * 4.01)

    def eur():
        print("wymieniam eur")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')
kantor_usd()
kantor_usd(2000)
kantor_usd(1500)

kantor_eur = kantor('eur')
kantor_eur()
