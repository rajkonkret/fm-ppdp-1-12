def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew


@dekor  # uzycie dekoratora
def hej():
    print("Hej!!!")


hej()
# po dodaniu dekoratora
# Dekorujemy
# Hej!!!