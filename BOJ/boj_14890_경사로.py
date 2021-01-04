N,L = map(int,input().split()) # ['6','2']
print(N,L)

# board = [list(map(int,input().split())) for _ in range(N)]
# print(board)
#list('3 3 3 3 3 3') = [ '3',' ','3']
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
print(board)