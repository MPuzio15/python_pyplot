def waga1(tab, n):
    s = 0
    for i in range(len(tab) - 1, -1, -1):
        if s + tab[i] <= n:
            s += tab[i]
        if s == n:
            print("s in loop", s)
            return True
    # end for
    print("S", s)
    return False


# end def


def waga(tab, n, p=0):
    """tablica z ciezarkami i ciezar, ktory chcemy zwazyc, i p = od ktorego zaczynam brac odw"""
    if n == 0:
        return True
    if p == len(tab):
        return False
    # wzialem odwaznik albo nie
    return waga(tab, n - tab[p], p + 1) or waga(tab, n, p + 1) or waga(tab, n + tab[p], p + 1)


# end def

odwazniki = [1, 3, 5, 10, 16, 24]  # odwazniki, czy tymi odwaznikami jestem w stanie zrownowazyc 23

for k in range(1, 40):
    print(k, waga(odwazniki, k, 0), waga1(odwazniki, k))

""" algorytm zachlanny - najpierw bierze odwazniki - pierwsza funkcja, 
jezlei nie ma odwaznieka ktory bedzie mniejszy niz suma poprzednich odwaznikow
 to wtedy algorytm zachlanny dziala poprawnie"""

"""Teraz albo biore na szalke albo nie biore w ogole, albo klade go na prawa szalke!!!"""
