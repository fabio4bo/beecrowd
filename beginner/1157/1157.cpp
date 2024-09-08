//
// BEE 1157 - Divisores I - Level 1 - Beginner
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