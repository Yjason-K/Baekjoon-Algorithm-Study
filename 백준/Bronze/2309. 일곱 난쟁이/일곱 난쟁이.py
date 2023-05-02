a = []
for i in range(9):
    a.append(int(input()))

b = sum(a)
    
for j in range(9):
  for k in range(j+1, 9):
    if b - (a[j] + a[k]) == 100 :
        c = a.copy()
        d = a[j]
        e = a[k]
        c.remove(d)
        c.remove(e)
c.sort()

for l in range(7):
    print(c[l])