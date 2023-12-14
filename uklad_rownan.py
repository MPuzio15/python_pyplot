import numpy as np

A = np.array([[1, 2], [5, 6]])
B = np.array([3, 4])

N = 100
AA = np.random.randn(N, N)
BB = np.array(range(1, N + 1))

print('Macierz A:')
print(AA)
print('Wektor B:')
print(BB)

w = np.linalg.det(AA)
print('Wyznacznik z macierzy A = ', w)

x = np.linalg.solve(AA, BB)
print('Rozwiazanie:')
print(x)

print('Iloczyn A*x')
print(np.dot(AA, x))

# poczytaj o wartosciach wlasnych !!!
