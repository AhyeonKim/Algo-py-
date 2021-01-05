A, B, V = map(int,input().split())
a,b = divmod(V-B,A-B)
print(a + (1 if b else 0))