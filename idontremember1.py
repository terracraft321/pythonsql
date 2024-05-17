opiskelija_lkm = int(input('Opiskelijoiden määrä? '))
testi_lkm = int(input('Testien määrä? '))

for opiskelija in range(opiskelija_lkm):
    summa = 0
    print(f'Opiskelijan numero {opiskelija + 1}')
    for testi in range(testi_lkm):
        while True:
                pisteet = float(input(f'Testi numero {testi + 1}: '))
                summa += pisteet
                break

    keskiarvo = summa / testi_lkm
    print(f'Opiskelijan {opiskelija + 1} keskiarvo on {keskiarvo:.2f}')
    print()
