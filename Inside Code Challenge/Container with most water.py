from time import time


def most_water1(heights):
    process = 0  # Conta o quanto de vezes o processo foi feito
    result = 0
    for i in range(len(heights)):
        for j in range(i, len(heights)):
            process += 1

            area = abs(i-j) * min(heights[i], heights[j])
            result = max(result, area)
    print(process)
    return result


def most_water2(heights):
    result = 0  # Conta o quanto de vezes o processo foi feito
    left = 0
    right = len(heights) - 1
    process = 0

    while left < right:
        process += 1

        area = (right - left) * min(heights[left], heights[right])
        result = max(result, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    print(process)
    return result


if __name__ == '__main__':
    lista = [1, 3, 2, 0, 5, 2, 5, 4, 1, 2, 5, 2, 3, 4, 6, 1]*100

    tim = time()
    print(most_water1(lista))
    print(time() - tim)

    print('\n')

    tim = time()
    print(most_water2(lista))
    print(time() - tim)
