n, m, y = map(int, input().split())

res = []

for x in range(0, m):
    result = 1 
    
    for i in range(n):
        result = ((result % m) * (x % m)) % m
    
    result = result % m
    
    if result == y:
        res.append(x)

if len(res) == 0:
    print(-1)
else:
    for i in res:
        print(i, end=' ')