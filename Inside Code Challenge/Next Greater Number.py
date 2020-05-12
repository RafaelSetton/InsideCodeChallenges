

def next_greater(num):
    list_num = [int(n) for n in str(num)]
    i = len(str(num)) - 1
    while True:

        if i == 0:
            return num

        if list_num[i] > list_num[i-1]:
            changes = list_num[i:]
            i -= 1
            buffer = list_num[i]
            least = max(changes)
            least_index = changes.index(least)
            for ind, n in enumerate(changes):
                if buffer < n < least:
                    least = n
                    least_index = ind

            changes.pop(least_index)
            changes.append(buffer)
            changes.sort()

            return int(''.join([str(n) for n in list_num[:i] + [least] + changes]))

        i -= 1


if __name__ == '__main__':
    print(next_greater(587))
