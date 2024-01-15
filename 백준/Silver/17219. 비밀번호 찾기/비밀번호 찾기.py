n, m = map(int, input().split())

data = {}
for i in range(n):
    site, pw = map(str, input().split())
    data[site] = pw
    
for i in range(m):
    add = input()
    print(data[add])