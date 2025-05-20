import math

from mypyc.codegen.literals import format_int


def primeTerms(number) -> list:
    if number <= 2:
        return [number]

    primes = soe(number)

    for i in range(2, number):
        if primes[i] and primes[number - i]:
            return [i, number - i]

    return []


def soe(number: int):
    primes = [True] * number
    primes[0] = False
    primes[1] = False

    for i in range(2, int(math.sqrt(number)) + 1):
        if primes[i]:
            for j in range(i*i, number, i):
                primes[j] = False

    return primes

def main():
    print(primeTerms(1000))


if __name__ == '__main__':
    main()
