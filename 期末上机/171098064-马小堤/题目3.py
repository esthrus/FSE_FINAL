#节点个数n
n=input()
n=int(n)

paths=[]
all=[]
for i in range(n-1):
    p=input()
    paths.append(p)

count=0
start=[] #每条路径的起始节点
end=[]  #每条路径的终止节点

for j in range(n-1):
    path=paths[j].split(' ')
    all.append(path)    #该树上所有的路径

flag=False
for i in range(len(all)):
    if all[i][0]=='1':
        for k in range(len(all)):
            if k!=i:
                newend=all[i][1]