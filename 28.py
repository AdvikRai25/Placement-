from operator import index
n=int(input("Enter the number of teams: "))
teams=[]
for i in range(n):
    a=input("Enter team name: ")
    teams.append(a)
meet=int(input("Enter the number of faceoff between one pair: "))
match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append([teams[i],teams[j]])
print("____________________________")
index=1
for i in match:
    print("Match {}: {} vs {}".format(index, i[0], i[1]))
    index+=1