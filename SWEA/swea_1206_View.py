testcase = 10
for tc in range(testcase):
    N = int(input())
    building = list(map(int,input().split()))
    answer = 0
    for i in range(2,N-2):
        tmp = building[i] - max(building[i-2],building[i-1],building[i+1],building[i+2])
        if tmp>0:
            answer += tmp
    print(f"#{tc+1} {answer}")
    print("#{} {}".format(tc+1,answer))
