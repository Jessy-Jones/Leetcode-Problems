def numberOfEmployeesWhoMetTargetHours(hours: [int], target: int) -> int:
    count = 0
    for hour in hours:
        if hour >= target:
            count += 1
    return count

# Time complexity: O(n)
# Space complexity: O(1)

