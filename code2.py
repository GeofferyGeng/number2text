import re
'''
本文的代码参照csdn[]，侵删
'''

with open("少年歌行.txt", "r") as f:
    text = f.read()
p = re.compile(r'\d+')
shuzi = p.findall(text)

print(shuzi)
import re,time
#主程序
def ranki():
    rank=[]
    for i in range(len(shuzi)):
        i=turn(shuzi[i])
        rank.append(i)
    return rank
#如果超过万，则分为两部分以节约代码和运行速度
def turn(x):
    i=str(x)
    if len(i) >4:
        i=tran(i[0:-4])+'万'+tran(i[-4:])
    else:
        i=tran(i[-4:])
    return i
#转换数字并插入对应单位，单位为‘零’则再插入一个‘零’以方便正则表达式替换
def tran(x):
    num=['零','一','二','三','四','五','六','七','八','九']
    kin=['零','十','百','千']
    x=list(reversed(x))
    for i in x:
        x[(x.index(i))]=num[int(i)]
    if len(x) >= 2:
        if x[1]==num[0]:
            x.insert(1,kin[0])
        else:
            x.insert(1,kin[1])
        if len(x) >= 4:
            if x[3]==num[0]:
                x.insert(3,kin[0])
            else:
                x.insert(3,kin[2])
            if len(x) >= 6:
                if x[5]==num[0]:
                    x.insert(5,kin[0])
                else:
                    x.insert(5,kin[3])
    x=delz(x)
    return x
def delz(x):
    x=''.join(x)
    if '零零'in x:
        x=re.sub('零+','零',x)
    if x.startswith('零'):
        x=list(x)
        x.remove('零')
    x=reversed(x)
    x=''.join(x)
    return x
start=time.time()
rank=ranki()
print(rank)
end=time.time()-start
print('程序共用时：%0.2f'%end)
for i in range(len(rank)):
    rank[i]="第"+rank[i]+"章"
    text=text.replace(shuzi[i],rank[i])
print(text[0:5000])
with open("少年歌行2.txt", "w") as f:
    f.write(text)
