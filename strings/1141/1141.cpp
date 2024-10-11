#include<bits/stdc++.h>
using namespace std;

#define K 52
#define MAX 112345
#define to_i(ch) ((ch) >= 'a' ? (ch) - 'a' + 26 : (ch) - 'A')


struct node {
    // pc -> char pelo qual veio do pai
    int next[K], terminal = 0, p, pc, link = -1, go[K], exit_ = -1, occ = 0;
    vector<int> idx;

    node(int _p = 0, int _pc = 0) : p(_p), pc(_pc){
        memset(next, -1, sizeof(next));
        memset(go, -1, sizeof(go));
    }};

vector<node> aca; //Aho-Corasick Automaton
int occ[MAX];

void inserir(char s[], int idx){
    int i, u = 0;

    for (i = 0; s[i]; i++){
        int c = to_i(s[i]);

        if (aca[u].next[c] == -1){//não existe
            aca[u].next[c] = aca.size();
            aca.emplace_back(u, c);
        }
        u = aca[u].next[c];
    }
    aca[u].terminal = 1; aca[u].idx.push_back(idx);
}

int go(int u, int c);

int link(int u){
    if (aca[u].link != -1) return aca[u].link;

    return aca[u].link = (u == 0 || aca[u].p == 0) ? 0 : go(link(aca[u].p), aca[u].pc);
}

int go(int u, int c){
    if (aca[u].go[c] != -1) return aca[u].go[c];

    if(aca[u].next[c] != -1) return aca[u].go[c] = aca[u].next[c];

    return aca[u].go[c] = u == 0 ? 0 : go(link(u), c);
}

int exit_(int u){
    int v = link(u);
    if (aca[u].exit_ != -1) return aca[u].exit_;

    return aca[u].exit_ = (v == 0 || aca[v].terminal) ? v : exit_(v);
}


void process(char t[]){
    int i, u = 0;
    for (i = 0; t[i]; i++){
        int c = to_i(t[i]);
        u = go(u, c);
        for(int v = u; v; v = exit_(v))
            aca[v].occ++;
    }
    for (u = 0; u < (int)aca.size(); u++)
        for (auto &idx : aca[u].idx)
            occ[idx] += aca[u].occ;
}


int main(void){
    int ncases, i, q;
    char t[MAX];
    scanf("%d", &ncases);

    while(ncases--){
        aca.clear(); aca.emplace_back();
        memset(occ, 0, sizeof(occ));

        scanf(" %s %d", t, &q);

        for (i = 0; i < q; i++){
            char s[MAX];
            scanf(" %s", s);
            inserir(s, i);
        }
    process(t);

    for (i = 0; i < q; i++)
        printf("%c\n", occ[i] ? 'y' : 'n');


    }
    return 0;
}