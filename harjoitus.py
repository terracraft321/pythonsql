import random

MIN = 1
MAX = 6

def main():
    toisto = 'k'
    while toisto == 'k' or toisto == 'K':
        print("Nopan heitto:")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        toisto = input('Heitetäänkö uudestaan?')

main()
