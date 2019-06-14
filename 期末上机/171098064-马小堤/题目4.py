a=input()
a=a.split(' ')
n=int(a[0]) #城市数量
m=int(a[1]) #路径数量

fee=0
paths=[]
all=[]
for i in range(m):
    p=input()
    paths.append(p)

for j in range(m):
    path=paths[j].split(' ')
    all.append(path)    #该树上所有的路径

