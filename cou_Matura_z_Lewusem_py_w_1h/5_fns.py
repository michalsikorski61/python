lines = []
for line in open('file.txt', encoding='UTF-8'):
    lines.append(line.strip())



def silnia(n):
    # 5! = 5 * 4 * 3 * 2 * 1
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for line in lines:
    print(silnia(int(line)))