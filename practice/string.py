INPUT = '55 185'
splited =INPUT.split()
print(splited) # [ '55' , '185']



# map(함수, iterable)

splited = list(map(int, INPUT.split()))
print(splited) # [ 55, 185 ]