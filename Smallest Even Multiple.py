def smallestEvenMultiple(n: int) -> int:
    return n if (n % 2 == 0) else n * 2

print(smallestEvenMultiple(6))

# Time Complexity: O(1)
# Space Complexity: O(1)