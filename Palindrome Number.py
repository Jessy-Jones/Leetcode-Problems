def isPalindrome(x: int) -> bool:
    reverse = 0
     # Check for negative numbers or numbers ending with zero
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    # Reverse the second half of the number
    while x > reverse:
        reverse = (reverse * 10) + (x % 10)
        x //=10
    # Compare the original first half with the reversed second half
    return True if (x == reverse or x == reverse // 10) else False


print(isPalindrome(121))

# Time Complexity: O(log10(x))
# Space Complexity: O(1)

    