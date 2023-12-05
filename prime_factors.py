from math import sqrt

# first solution - slower

n = int(input("Podaj liczbe naturalna: "))

b = 2

# while n > 1:
#     if n % b == 0:
#         print(b)
#         n = n // b
#     else:
#         b = b + 1
#     # end if
# # end while
# print("END")

# faster, because it does not check the numbers higher than sqrt(n)
while b <= sqrt(n):
    if n % b == 0:
        print(b)
        n = n // b
    else:
        b = b + 1
    # end if
# end while
if n > 1:
    print("END")





