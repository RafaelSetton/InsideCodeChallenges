

def hanoi(n, ini='A', aux='B', fim='C'):

    def frase(origem, destino):
        print(f'De {origem} para {destino}.')

    if n == 1:
        frase(ini, fim)
    else:
        hanoi(n-1, ini, fim, aux)
        frase(ini, fim)
        hanoi(n-1, aux, ini, fim)


if __name__ == '__main__':
    hanoi(5)
