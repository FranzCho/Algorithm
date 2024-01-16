import sys
from collections import deque
 
input = sys.stdin.readline
 
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
 
n = int(input())
 
def bfs(l, a,b,c,d):
    map = [[-1] * l for _ in range(l)]
    map[a][b] = 0
    dq = deque()
    dq.append((a,b))
    while dq:
        x,y = dq.popleft()
        if x == c and y == d: #나이트가 이동하려는 칸과 일치 (도착)
            break
        for i in range(8): #나이트가 한번에 이동할 수 있는 step
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and map[nx][ny]==-1: #새 좌표가 체스판 내에 포함 & 아직 방문X
                map[nx][ny]=map[x][y]+1
                dq.append((nx,ny))
    return map[c][d]
 
for _ in range(n):
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ans = bfs(l,a,b,c,d)
    print(ans)
