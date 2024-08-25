C = int(input());

for i in range(C):
    N = int(input());
    S = 0;
    for j in range(N):
        if(j % 2 == 0):
            S+=1;
        else:
            S-=1;
    print(S);
