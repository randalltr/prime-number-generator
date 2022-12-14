primes = [2, 3, 5, 7]

numbers = range(11, 2000, 1)
not_prime = []

for number in numbers:
    for prime in primes:
        if number % prime == 0:
            not_prime.append(number)

    if number not in not_prime:
        primes.append(number)

print(primes)
