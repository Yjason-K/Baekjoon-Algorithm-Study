a = int(input())
b = int(input())

adj = [ [] for _ in range(a+1) ]
for _ in range(b):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)
    
def dfs(s):
    global ans
    ans +=1
    v[s] = 1
    
    for n in adj[s]:
        if v[n] == 0:
            dfs(n)
ans = 0
v = [0] * (a + 1)
dfs(1)
    
print(int(ans) - 1)