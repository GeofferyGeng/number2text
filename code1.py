import re

with open("少年歌行.txt", "r") as f:
    text = f.read()
p = re.compile(r'\d+')
shuzi = p.findall(text)
print(shuzi)

t1 = [0,1,2,3,4,5,6,7,8,9]
t2 = ['零','一','二','三','四','五','六','七','八','九']

for i in range(len(shuzi)):
    x = shuzi[i]
    for j in range(10):
        x=x.replace(str(t1[j]),t2[j])
    text=text.replace(shuzi[i],'第'+x+'章')
print(text[0:5000])
with open("少年歌行2.txt", "w") as f:
    f.write(text)
