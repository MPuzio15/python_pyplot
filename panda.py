end = None

import pandas as pd
import numpy as np
import sys

################################################################################

if __name__ == '__main__':

    fn_inp = 'cbz.xlsx'

    data = pd.read_excel(fn_inp)
    print(data.head())

    sh = data.shape
    print('wymiary danych:', sh)
    input()

    col = list(data.columns)
    print(*col, sep='\n')
    input()

    # dostep do nanych
    for i in range(sh[0]):
        print(data.album[i], data.nazwisko[i] + " " + data.imie[i])
    end
    input()

    # dostep do nanych inaczej
    for row in data.itertuples():
        print(row.album, row.imie)
    input()

    # wyszukiwanie
    for row in data[data.imie == 'Weronika'].itertuples():
        print(row.album, row.nazwisko, row.imie)
    input()

    # modyfikacja calej kolumny
    data.album //= 100

    # dodanie nowej kolumny
    data['plec'] = None

    # ustawienie plci
    for i in range(sh[0]):
        data.plec[i] = ['M', 'K'][data.imie[i][-1] == 'a']
    end

    print(data.head(20))

    # zapis zmodyfikowanego arkusza
    data.to_excel('nowy.xlsx')

end

################################################################################

# wiecej: https://analityk.edu.pl/python-pandas/
