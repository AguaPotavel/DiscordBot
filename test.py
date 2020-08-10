from google import google


def search(search):
    search_ = google.search(search, 1)
    search_
    return search_.name, search_.description, search_.link

def calcul(calcular):
    a = google.calculate(calcular)
    print(a)

a = input('')
calcul(a)