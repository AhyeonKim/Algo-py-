n = 3
zero_list = [0] * n

print(zero_list)

zero_complex = [[0,0,0]] * 3
print('3 * 3배열 : ' , zero_complex)
zero_complex[0][0] = 1
print('곱하기 : ' , zero_complex)

zero_complex = [[0,0,0] for _ in range(3)]
zero_complex[0][0] = 1
print('for문 : ' , zero_complex)