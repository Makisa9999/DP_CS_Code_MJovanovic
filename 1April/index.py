def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
#         loop throught the list and add make a new list that will add all the extra candies to each kid:
#             [1,2,3,4,21,12,1,1,1] extra candies: 2
#             [3,4,5,6,23,14,3,3,3]
#             then loop throught both list and check if the number is greater or equal to every item in the list, if it is return true otherwise false
    
    lst = []
    for i in range(len(candies)):
        a = sorted(candies)
        # [1,2,3,3,5]
        if a[-1] <= (candies[i]+extraCandies):
            lst.append(True)
        else: 
            lst.append(False)
    return lst
# print(kidsWithCandies([2,3,5,1,3],3))
def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    a = []
    count = 0
    for i in range(len(jewels)):
        a.append(jewels[i])
        for j in range(len(stones)):
            if a[i] == stones[j]:
                count += 1
    return count
print(numJewelsInStones("aA","aAAbbbb"))