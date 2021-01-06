# X = int(input())
# answer = 0
# while X>0:
#     answer += X%2
#     X = X//2
# print(answer)

X = int(input())
answer = 0
binary = bin(X)[2:]
for i in binary:
    if i=='1':
        answer+=1
print(answer)