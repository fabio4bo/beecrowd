/*
BEE 1061 - Tempo de um Evento - Level 3 - Mathematics
*/
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int dia_i, dia_t, w, x, y, z, tempo_dia_i, tempo_dia_t, total_tempo;
    string N;

    cin >> N >> dia_i;

    scanf("%d : %d : %d", &x, &y, &z);

    tempo_dia_i = 86400 - (x * 3600 + y * 60 + z);

    cin >> N >> dia_t;

    scanf("%d : %d : %d", &x, &y, &z);
    tempo_dia_t = x * 3600 + y * 60 + z;

    total_tempo = tempo_dia_i + tempo_dia_t;

    w = dia_t - dia_i - 1;
    w += total_tempo / 86400;
    x = total_tempo % 86400 / 3600;
    y = total_tempo % 86400 % 3600 / 60;
    z = total_tempo % 86400 % 3600 % 60;

    cout << w << " dia(s)" << endl;
    cout << x << " hora(s)" << endl;
    cout << y << " minuto(s)" << endl;
    cout << z << " segundo(s)" << endl;

    return 0;
}