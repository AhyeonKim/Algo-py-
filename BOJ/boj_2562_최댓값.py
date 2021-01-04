num = []
for _ in range(9):
    num.append(int(input()))
max_n = max(num)
print(max_n)
print(num.index(max_n)+1)