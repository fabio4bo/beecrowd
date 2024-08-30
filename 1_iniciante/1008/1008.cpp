//
// BEE 1008 - Salário - Nível 2 - Iniciante
// Submissão: 16/06/2017 16:49:10
//

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    cout << fixed << setprecision(2);
    int number, qtHoras;
    double pgtHora;
    cin >> number >> qtHoras >> pgtHora;

    cout << "NUMBER = " << number << "\nSALARY = U$ " << (qtHoras * pgtHora) << endl;

    return 0;
}