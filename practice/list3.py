default = [1,[0,1,4,6],5,6]
default.append(100)
print(default)

print(default[1][2])

for _ in range(len(default)):
    print(default.pop())
    print(default)
print('-------------')

# range
print(list(range(1,6)))
print(list(range(1,6,3)))


print(list(range(1,21,2)))
print(list(range(2,21,2)))
print(list(range(10,0,-1)))