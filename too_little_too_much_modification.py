# Proszę zmodyfikować program z zadania 3, tak aby komputer grał sam ze sobą.

from random import randint


def lets_play():
    x = randint(1, 100)
    while True:
        try:
            user_number = int(input("Jaka liczbe z zakresu <1, 100> wylosowal komputer?:"))
            if user_number < 1 or user_number > 100:
                print("To nie jest liczba z tego zakresu")
            elif user_number > x:
                print("Za duzo")
            elif user_number < x:
                print("Za malo")
            elif user_number == x:
                print("Tak! Komputer wylosowal ", x)
                break
        except ValueError:
            print("To nie jest liczba naturalna")


lets_play()
