score = []
for i in range(8):
    score.append([int(input()),i+1])
s_score = sorted(score)[3:]

print(sum(map(lambda x:x[0],s_score)))

# r_score = sorted(s_score,key=lambda x:x[1])
# for i in r_score:
#     print(i[1])

print(*sorted(map(lambda x:x[1],s_score)))