def waga(tab, n, p = 0, wynik = []):
    if n == 0:
        print(wynik)
        return
    if p == len(tab):
        return
    waga(tab, n-tab[p], p + 1, wynik + [tab[p]])
    waga(tab, n + tab[p], p + 1, wynik + [-tab[p]])
    waga(tab, n, p+1, wynik)
# end def


odw = [1, 3, 5, 10, 16, 24]

waga(odw, 1) # pokazuje na ile sposobow mozna 1 gram odwazyc:P
