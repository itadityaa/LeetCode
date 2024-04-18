candies = [2,3,5,1,3]
extraCandies = 3
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    max_c = max(candies)
    for ind, candy in enumerate(candies):
        if candy + extraCandies >= max_c:
            candies[ind] = True
            continue
        candies[ind] = False
    return candies

print(kidsWithCandies(candies, extraCandies)) # Output: [True, True, True, False, True]