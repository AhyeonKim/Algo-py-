N = input()
cnt = [0]*10
for n in N:
    if n=='9' or n=='6':
        if cnt[6]<=cnt[9]:
            cnt[6]+=1
        elif cnt[6]>cnt[9]:
            cnt[9]+=1
    else:
        cnt[int(n)]+=1
print(max(cnt))