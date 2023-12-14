import pandas as pd
import os.path

pd.options.mode.chained_assignment = None  # default='warn'

end = None

# data frame - dwuwymiarowa tablica
# shape - zwraca krotke ktora okresla ilosc wierwszy i ilosc kolumn

if __name__ == '__main__':
    path_dir = os.path.abspath('cbz.xlsx')
    data = pd.read_excel(path_dir)

    sh = data.shape
    print('wymiary danych:', sh)
    input()

    col = list(data.columns)
    print(*col, sep='\n')
    input()

    # dostep do nanych
    for i in range(sh[0]):
        print(data.album[i], data.nazwisko[i] + " " + data.imie[i])
    # end
    input()

    # dostep do danych inaczej
    for row in data.itertuples():
        print(row.nazwisko, row.album)
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
    # end

    print(data.head(20))

    # zapis zmodyfikowanego arkusza
    data.to_excel('nowy.xlsx')

# end
