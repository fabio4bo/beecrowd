# -*- coding: utf-8 -*-

"""
BEE 1022 - TDA Racional - Nível 4 - Estruturas e Bibliotecas
"""

import math

def imprime(rnf, rdf):
    print(f"{rnf}/{rdf}", end=" = ")
    mdc(rnf, rdf)

def mdc(rnf, rdf):
    mdc = math.gcd(rnf, rdf)
    rnf = rnf // mdc
    rdf = rdf // mdc
    print(f"{rnf}/{rdf}")


def soma(n1, d1, n2, d2):
    rnf = n1 * d2 + n2 * d1
    rdf = d1 * d2
    imprime(rnf, rdf)

def subtrai(n1, d1, n2, d2):
    rnf = n1 * d2 - n2 * d1
    rdf = d1 * d2
    imprime(rnf, rdf)


def multiplica(n1, d1, n2, d2):
    rnf = n1 * n2
    rdf = d1 * d2
    imprime(rnf, rdf)


def divide(n1, d1, n2, d2):
    rnf = n1 * d2
    rdf = d1 * n2
    imprime(rnf, rdf)

# comandos = "1 / 2 + 3 / 4".split(" ")
# comandos = "1 / 2 - 3 / 4".split(" ")
# comandos = "2 / 3 * 6 / 6".split(" ")
# comandos = "1 / 2 / 3 / 4 ".split(" ")

N = int(input())
for i in range(N):
    comandos = input().split(" ")
    n1 = int(comandos[0])
    d1 = int(comandos[2])
    n2 = int(comandos[4])
    d2 = int(comandos[6])
    op = comandos[3]
    if op == "+":
        soma(n1, d1, n2, d2)
    elif op == "-":
        subtrai(n1, d1, n2, d2)
    elif op == "*":
        multiplica(n1, d1, n2, d2)
    else:
        divide(n1, d1, n2, d2)
