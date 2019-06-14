#各集合的个数n
n=input()
n=int(n)

numbers=[]
for i in range(n):
    number=input()
    numbers.append(number)

count=0
a=[]
b=[]
c=[]
d=[]
for j in range(len(numbers)):
    num=numbers[j].split(' ')
    a.append(int(num[0]))
    b.append(int(num[1]))
    c.append(int(num[2]))
    d.append(int(num[3]))

for i in a:
    for j in b:
        for k in c:
            for m in d:
                if i+j+k+m==0:
                    count=count+1

print(count)