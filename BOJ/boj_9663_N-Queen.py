def dfs(n):
    # n번째줄인거야 n번째 depth
    if n == N:
        return

    for i in range(N):
        # n번째 줄의 하나하나씩
        other = [(n,i)]
        for y in range(N-n):
            for d in [-1,0,1]:
                n_y = n+y
                n_x = i+d*y
                if -1< n_x<N and not visit[n_y][n_x]:
                    other.append((n_y,n_x))
        ## 1. 조건문을 통해서 
        # 놓지 못하는 장소,
        # False인 것들을 other에 담아
        for (x,y) in other:
            visit[x][y] = True
        ## 2. other에 있는 것들을 다 visit=True 처리
        ## 3. 다음 뎁스 dfs(n+1) !! 일단은 가지말고 
        dfs(n+1)
        # for v in visit:
        #     print(v)
        # print('--------')
        for (x,y) in other:
            visit[x][y] = False
        
        # 4. 초기화 other에 있는것을 visit=False
N = int(input())
ans = 0
visit = [[False]*N for _ in range(N)]
# di,dj = [0,1,1],[1,1,0]
dfs(0)