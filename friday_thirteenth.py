def what_day_do_we_have(r, m, d):

    rm = (-1, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5)
    dt = d + rm[m] + (r-1900) + (r-1900)//4
    if m < 3 and r % 4 == 0:
        dt = dt - 1
    res = dt % 7
    return res
# end def


friday_13th = []
for rok in range(1900, 2100):
    for miesiac in range(1, 13):
        result = what_day_do_we_have(rok, miesiac, 13)
        if result == 5:
            friday_13th.append(f'{miesiac}'+'.'+f'{rok}')
print(friday_13th)
