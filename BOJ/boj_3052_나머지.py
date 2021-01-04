unique = set()
for _ in range(10):
    unique.add(int(input())%42)
print(len(unique))