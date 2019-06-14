#最终要去除的字符ch
ch=input()

str=[]
string=input()
str.append(string)
while(string!='@'):
    string=input()
    str.append(string)
str.pop()

new=[]
for s in str:
    new_s=s.replace(ch,'')
    new.append(new_s)

new.sort(reverse=True)
for s in new:
    print(s)