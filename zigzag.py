def zigzag(a):
    row = len(a)
    col = len(a[0])
    
    r_high_lim = row-1
    r_low_lim = 0
    c_high_lim = col-1
    c_low_lim = 0
    
    sol = [a[0][0]]
    r = 1
    c = 0
    move = 1
    count = row*col-2
    while count>0:
        #print(sol)
        sol.append(a[r][c])
        if r==r_low_lim and move==1 and c+1<col:
            c += 1
            move = -1
        elif r==r_high_lim and move==-1:
            c+=1
            move = 1
        elif c==c_low_lim and move==-1 and r+1<row:
            r+=1
            move = 1
        elif c==c_high_lim and move==1:
            r+=1
            move = -1
        else:
            r-=move
            c+=move
        count-=1
    sol.append(a[r][c])
    return sol

t = int(input())
for testcases in range(t):
    row,col = [int(i) for i in input().split()]
    a = [[0 for i in range(col)] for i in range(row)]
    i = 1
    r = 0
    c = 0
    while r<row:
        c=0
        while c<col:
            a[r][c] = i
            i+=1
            c+=1
        r+=1
    for _ in a:
        print(_)
        
    print(zigzag(a))
