N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    group = {}
    prev = word[0]
    group[prev] = 1
    flag = True
    for w in word:
        if w==prev:
            continue
        if w in group:
            flag = False
            break
        else:
            group[w] = 1
            prev = w
    if flag:
        cnt+=1
print(cnt)