while True:

    n = -1
    while not n.is_integer() or n < 0:
        print("nota invalida")
        n = float(input())

    m = -1
    while not n.is_integer() or n < 0:
        print("nota invalida")
        n = float(input())

    print(f"media = {n+m / 2:.2f}")

    r = int(input())
    while r != 1 and r != 2:
        print("novo calculo (1-sim 2-nao)")
        r = int(input())

    if r == 2:
        break
