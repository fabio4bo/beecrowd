/*
BEE 2453 - Língua do P - Level 4 - Ad-hoc
*/
//Submissão: 18/02/2018 15:27 

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string texto_em_p, novo_texto;
    bool pori = true;
    getline(cin, texto_em_p);
    int tamanho = texto_em_p.size();

    for (int i = 0; i < tamanho; i++)
    {
        if (texto_em_p[i] == ' ')
        {
            novo_texto += ' ';
            pori = !pori;
        }
        else if (pori and i % 2 != 0)
            novo_texto += texto_em_p[i];
        else if (!pori and i % 2 == 0)
            novo_texto += texto_em_p[i];
    }

    cout << novo_texto << endl;
    return 0;
}
