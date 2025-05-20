import math


def sieve_of_eratosthenes(n: int):
    array = [True] * n
    array[0] = False
    array[1] = False
    for i in range (2, int(math.sqrt(n)) + 1):
        if array[i]:
            for j in range(i*i, n, i):
                array[j] = False

    result = []
    for i in range(n):
        if array[i]:
            result.append(i)


    return result


def main():
    print(sieve_of_eratosthenes(10))


if __name__ == '__main__':
    main()