word = input()
cnt = [0]*26
for i in word:
    cnt[ord(i)-ord('a')]+=1
print(*cnt)