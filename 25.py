grid=[[" "for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if(j==0):
            grid[i][j]="*"
        if(i==0 and i<6):
            grid[i][j]="*"
        if(i==4 and i<6):
            grid[i][j]="*"
for i in range(10):
    for j in range(10):
        print(grid[i][j],end=" ")
    print()