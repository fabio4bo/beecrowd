// 
// BEE 1161 - Soma de Fatoriais - Nível 5 - Matemática
// 
#include <iostream>

using namespace std;

long long int Fatorial(int N)
{
    if (N == 0)
        return 1;
    return N * Fatorial(N - 1);
}

int main()
{
    int M, N;

    while (cin >> M >> N)
    {
        cout << Fatorial(M) + Fatorial(N) << endl;
    }

    return 0;
}