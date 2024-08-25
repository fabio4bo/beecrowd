# -*- coding: utf-8 -*-

"""
BEE 1022 - TDA Racional - Nível 4 - Estruturas e Bibliotecas
"""

import math

# math.gcd pode ser feito da seguite forma usando o algoritmo de euclides
# como no problema 1028 em java.


def MDC(numero1, numero2):
    return numero1 if numero2 == 0 else MDC(numero2, numero1 % numero2)


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
    elif op == "/":
        divide(n1, d1, n2, d2)
