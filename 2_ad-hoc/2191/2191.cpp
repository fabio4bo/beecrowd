/*
BEE 2191 - Saldo de Gols - Nível 8 - Ad-hoc
*/

#include <iostream>
using namespace std;

int main()
{

    int testes = 0, x, y, n, primeiro, prim_temp, ultimo, s_atual, s_maior;

    while (true)
    {
        cin >> n;
        if (n == 0)
            break;
        testes++;
        primeiro = 0;
        ultimo = 0;
        prim_temp = 0;
        s_maior = -1;
        s_atual = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> x >> y;
            s_atual += x - y;

            if (s_atual < 0)
            {
                prim_temp = i + 1;
                s_atual = 0;
            }

            if (s_atual >= s_maior)
            {
                s_maior = s_atual;
                primeiro = prim_temp;
                ultimo = i;
            }
        }
        cout << "Teste " << testes << endl;
        if (s_maior > 0)
            cout << primeiro + 1 << " " << ultimo + 1 << endl
                 << endl;
        else
            cout << "nenhum" << endl
                 << endl;
    }
    return 0;
}