s="nagaram"
t="anagram"

c=dict()
o=dict()

for i in s:
    if i in c:
        c[i]+=1
    else:
        c[i]=1

print(c)


for i in t:
    if i in o:
        o[i]+=1
    else:
        o[i]=1

print(o)

if c==o:
    print(True)
else:
    print(False)