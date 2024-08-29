//
// BEE 1157 - Divisores I - Nível 1 - Iniciante
//
#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;

    for (int i = 1; i < N + 1; i++)
    {
        if (N % i == 0)
            cout << i << endl;
    }
    return 0;
}