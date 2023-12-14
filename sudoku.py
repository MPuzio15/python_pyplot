import time


def wczytaj(nazwa):
    t = {}
    f = open(nazwa, "r")
    for w in range(0, 9):
        line = f.readline()
        for k in range(0, 9):
            t[w, k] = line[k]
        # end for
    # end for
    f.close()
    print("t", t)
    return t


# end def

def wypisz(t):
    for w in range(0, 9):
        for k in range(0, 9):
            print(' ' + t[w, k], end='')
        # end for
        print()
    # end for
    print()


# end def

def puste(t):
    res = []
    for w in range(0, 9):
        for k in range(0, 9):
            if t[w, k] == '-':
                res.append((w, k))
            # end if
        # end for
    # end for
    return res


# end def

def mozliwe(t, w, k):
    res = "123456789"  # zakladam ze wszystko mozna wpisac
    for i in range(0, 9): res = res.replace(t[w, i], '')
    for i in range(0, 9): res = res.replace(t[i, k], '')
    for i in range(k // 3 * 3, k // 3 * 3 + 3):
        for j in range(w // 3 * 3, w // 3 * 3 + 3): res = res.replace(t[j, i], '')
    # end for
    return res


# end def

def ruch(t, lp, n=0):
    # wypisz(t)
    # time.sleep(0.7)
    if n == len(lp):
        wypisz(t)
        # time.sleep(0.5)
        exit()
    else:
        w, k = lp[n]
        for x in mozliwe(t, w, k):
            t[w, k] = x
            ruch(t, lp, n + 1)
            t[w, k] = '-'
        # end for
    # end if


# end def


d = wczytaj("dane.txt")
wypisz(d)
lp = puste(d)
print(lp)

print("mozliwe: ", mozliwe(d, 0, 1))
ruch(d, lp)

# jezlei wyrzucimy wszystko z tablicy i zostawimy ja pusta to bedziemy mieli wszystkie mozliwe rozwiazania sudoku
