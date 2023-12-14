try:
    f = open("tekst.txt", "r", encoding="utf-8")
    t = {}
    for line in f:
        line = line.strip('\n').lower().split()
        for z in line:
            z = z.strip(',')  # usuwa wskazany znak
            if z in t:
                t[z] += 1
            else:
                t[z] = 1
    # end
    li = t.items()
    print("li", li)
    li2 = sorted(li)
    print("Sorted array:", li2)  # uporzadkowana wg kodu ASCII
    # posortuj wg liczby wystapien
    li3 = sorted(li, key=lambda words_number: words_number[1], reverse=True)
    print(("li3", li3))
    # ladniej
    for x in li3:
        print(x[0], x[1])
    f.close()
except:
    print("No file!")
# end

# python wypisal to z duzymi odstepami bo python wczytuje linie lacznie ze znakiem nowego wiersza
# sprobuj usunac ten znak nowego wiersza
