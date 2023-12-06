from math import sqrt


def get_user_input():
    try:
        natural = int(input("Podaj liczbe naturalna: "))
        return natural
    except ValueError:
        print("To nie jest liczba naturalna")


def check_prime_factors():
    natural_number = get_user_input()
    b = 2
    while b <= sqrt(natural_number):
        if natural_number % b == 0:
            print("Podzielne przez: ", b)
            natural_number = natural_number // b
        else:
            b = b + 1
        # end if
    # end while
    if natural_number > 1:
        print("END")


check_prime_factors()


# while n > 1:
#     if n % b == 0:
#         print(b)
#         n = n // b
#     else:
#         b = b + 1
#     # end if
# # end while
# print("END")






