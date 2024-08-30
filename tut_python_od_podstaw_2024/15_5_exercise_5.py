# liczby pierwsze
# Napisz program, który wyświetli wszystkie liczby pierwsze z zakresu od 1 do 100.
#
# Podpowiedź: liczba pierwsza to taka liczba, która dzieli się tylko przez 1 i samą siebie.
for i in range(1, 101):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        