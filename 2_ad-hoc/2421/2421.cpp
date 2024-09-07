/*
 * BEE 2421 - Álbum de Fotos - Nível 8 - Ad-hoc
 */
#include <iostream>
using namespace std;

int main()
{
    int x, y, l0, h0, l1, h1;

    cin >> x >> y >> l0 >> h0 >> l1 >> h1;

    if (
        l0 + l1 <= x and max(h0, h1) <= y or
        l0 + h1 <= x and max(h0, l1) <= y or
        l0 + l1 <= y and max(h0, h1) <= x or
        l0 + h1 <= y and max(h0, l1) <= x or
        max(l0, l1) <= x and h0 + h1 <= y or
        max(l0, h1) <= x and h0 + l1 <= y or
        max(l0, l1) <= y and h0 + h1 <= x or
        max(l0, h1) <= y and h0 + l1 <= x)

        cout << 'S' << endl;
    else
        cout << 'N' << endl;
}
