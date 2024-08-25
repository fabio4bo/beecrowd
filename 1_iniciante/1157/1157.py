#0s
N = int(input());

for i in range(1, N+1):
    if(N % i == 0):
        print(i);

#essa 0.067s, somente para testar
#one_ate_N = [x for x in range(1,N+1)];
#divisores_N = [x for x in one_ate_N if N % x == 0];
#for i in divisores_N:
#    print(i)