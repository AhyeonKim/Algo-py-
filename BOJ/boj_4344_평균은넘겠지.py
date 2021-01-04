C = int(input())
for _ in range(C):
    student = list(map(int,input().split()))
    N = student.pop(0)
    avg = sum(student)/N
    smart = 0
    for i in student:
        if i>avg:
            smart+=1
    # print(f'{round(smart/N*100,3)}%')
    ans = format(smart/N*100,'.3f')
    print(f'{ans}%')