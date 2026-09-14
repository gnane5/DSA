n=[1,2,3,4]
c=[]
# d=0
for i in range(len(n)):
    p=1
    for j in range(len(n)):
        if i != j:
            p=p*n[j]
    c.append(p)

print(c)