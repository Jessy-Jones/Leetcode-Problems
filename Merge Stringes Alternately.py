def mergeAlternately(word1: str, word2: str) -> str:
    # Intialize the merged string as an empty string
    mergedString = ""
    #Use the maximum length of the two words as the range, 
    # so that the extra characters of the longer word can still be added.
    for i in range (max(len(word1), len(word2))):
        # Append the character at word1[i] to mergedString if i is less than word1
        if i < len(word1):
            mergedString += word1[i]
        # Append the character at word2[i] to mergedString if i is less than word2
        if i < len(word2):
            mergedString += word2[i]
    return mergedString

print(mergeAlternately("Jessica", "Jones"))
