

def plus_one(array: list):
    num = array[-1]
    if num == 9:
        array[-1] = 0
        try:
            array[:-1] = plus_one(array[:-1])
        except IndexError:
            array = [1, 0] + array[1:]
    else:
        array[-1] += 1

    return array


if __name__ == '__main__':
    lista = [5, 9, 1, 9]
    print(plus_one(lista))
