class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best = [float('inf')]

        def helper(index, dsum):
            if index == len(toppingCosts):
                if abs(target - dsum) < abs(target - best[0]):
                    best[0] = dsum
                elif abs(target - dsum) == abs(target - best[0]):
                    best[0] = min(best[0], dsum)
                return

            helper(index + 1, dsum)
            helper(index + 1, dsum + toppingCosts[index])
            helper(index + 1, dsum + 2 * toppingCosts[index])

        for base in baseCosts:
            helper(0, base)

        return best[0]