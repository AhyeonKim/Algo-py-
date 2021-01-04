a = [ 1, 2, 3 ]
length = len(a)
print(length)  # 3

print(len('91284'))  # 5

# for 문을 index, value 두가지방법
## index 필요할 때
print('인덱스')
for i in range(len(a)):
    # i -> 0,1,2
    # range(3) - > 0,1,2
    print(i, a[i])

## 값만 필요하다
print('값') 
for i in a:
    print(i)

a[1] = 5
print(a)
a[1], a[2] = a[2] , a[1]
print(a)

a1, a2, a3 = a
print(a1, a2, a3)