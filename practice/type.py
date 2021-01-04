string = type('1')
number = type(1)
obj = type({1:2})
array = type([1,2,3])

print(string)
print(number)
print(obj)
print(array)

# str - int
print(type(int('123')))
print(type(str(123)))

