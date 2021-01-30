alpha = set(['c=','c-','dz=','d-','lj','nj','s=','z='])
word = input()
cnt = 0
i=0
while i<len(word):
    if word[i:i+2] in alpha:
        cnt+=1
        i+=2
    elif word[i:i+3] in alpha:
        cnt+=1
        i+=3
    else:
        cnt+=1
        i+=1
print(cnt)