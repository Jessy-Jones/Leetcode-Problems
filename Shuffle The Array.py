def shuffle(nums: [int], n: int) -> [int]:
    # Define an array to hold the shuffled array, and two other arrays to hold half each of the original array
    shuffledArray = []
    arrA = []
    arrB = []
    # Put the first half of the arry into arrA
    for x in range(0,n):
        arrA.append(nums[x])
    # Put the second half of the array into arrB
    for y in range(n, len(nums)):
        arrB.append(nums[y])
    # Alternate the items in arrA and arrB and put them into shuffledArray
    for z in range(0, len(arrA)):
        shuffledArray.append(arrA[z])
        shuffledArray.append(arrB[z])
    return shuffledArray


print(shuffle([1, 2, 3, 4, 5, 6], 3))