numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for chislo in numbers:
    if chislo == 1:
        continue
    is_prime = True
    for delitel in range(2, chislo):
        if chislo % delitel == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(chislo)
    else:
        not_primes.append(chislo)
print("Простые числа:", primes)
print("Непростые числа:", not_primes)