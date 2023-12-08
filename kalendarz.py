# napisz funkcje, ktora na podstawie daty wyznacza dzien tygodnia

"""Funkcja zwraca numer dnia tygodnia dla dowolnej daty
w latach 1900-2099. Niedziela ma numer 0."""

# dzien = int(input("Dzien: "))
miesiac = int(input("Miesiac: "))
rok = int(input("Rok (1900 - 2099): "))


def what_day_do_we_have(r, m, d):

    rm = (-1, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5)
    dt = d + rm[m] + (r-1900) + (r-1900)//4
    if m < 3 and r % 4 == 0:
        dt = dt - 1
    result = dt % 7
    return result
# end def

def how_many_sundays_a_month(r, m):
    niedziele = 0
    liczba_dni_w_miesiacu = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    liczba_dni_w_miesiacu_rok_przestepny = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if r % 4 == 0:
        for d in range(1, liczba_dni_w_miesiacu_rok_przestepny[m] + 1):
            result = what_day_do_we_have(r, m, d)
            if result == 0:
                niedziele += 1
    else:
        for d in range(1, liczba_dni_w_miesiacu[m] + 1):
            result = what_day_do_we_have(r, m, d)
            if result == 0:
                niedziele += 1
    return niedziele
# end def


print(how_many_sundays_a_month(rok, miesiac))

months_with_five_sundays = []
for r in range(1900, 2100):
    for m in range(1, 13):
        result = how_many_sundays_a_month(r, m)
        if result == 5:
            months_with_five_sundays.append(f'{m}'+'.'+f'{r}')
print(months_with_five_sundays)


