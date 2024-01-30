def isSelfDividing(num: int) -> bool:
    digits = [int(d) for d in str(num)]
    for digit in digits:
        if num == 0 or num % digit != 0:
            return False
    return True


def selfDividingNumbers(left: int, right: int) -> [int]:
    arr = []
    for i in range(left, right + 1):
        if isSelfDividing(i):
            arr.append(i)
    return arr

print(selfDividingNumbers(1, 22))
