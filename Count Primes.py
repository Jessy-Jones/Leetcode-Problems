def countPrimes(n: int) -> int:
    # If the value of n given is less than 2, it means there are 0 prime numbers less than n
    if n < 2:
        return 0
    # Assign True to all values n downwards, labelling them as True from the onset
    prime = [True] * n
    # 0 and 1 are not prime numbers, so assign False
    prime[0] = prime[1] = False
    # Iterate through each number from 2 to n. If number is still labelled True,
    # find the multiples of the number and mark as False.
    for i in range(2, n):
        if prime[i]:
            for multiple in range(2 * i, n, i):
                prime[multiple] = False
    return sum(prime)

print(countPrimes(100))