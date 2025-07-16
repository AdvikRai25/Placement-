# a=input("enter the name:")
# b=input("enter the name:")
# a1=list(a)
# b1=list(b)
# for i in range(len(a1)):
#     for j in range(len(b1)):
#         if(a1[i]==b1[j]):
#             a1[i]='2'
#             b1[j]='2'
# print(a1+b1)
# count=0
# for i in a1:
#     if(i!='2'):
#         count=count+1
# for i in b1:
#     if(i!='2'):
#         count=count+1
# print(count)
#
# ans=['F','L','A','M','E','S']
# index=0
# while(len(ans)!=1):
#     index=(index+(count-1))%len(ans)
#     ans.pop(index)
# print("the relation is",ans[0])
boy=input("Enter boy name:")
girl=input("Enter girl name:")
a1=list(boy)
a2=list(girl)
for i in range(len(a1)):
    for j in range(len(a2)):
        if a1[i]==a2[j]:
            a1[i]='2'
            a2[j]='2'
for i in a1:
    if(i=='2'):
        a1.remove(i)
for i in a2:
    if(i=='2'):
        a2.remove(i)
num=len(a1)+len(a2)
print(num)
ans=['F','L','A','M','E','S']
index=0
while(len(ans)!=1):
    index=(index+(num-1))%len(ans)
    ans.pop(index)
print("The relation is",ans[0])
