class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating)-1):
            a, b = [0]*2, [0]*2
            for j in range(len(rating)):
                if rating[i] > rating[j]:
                    a[i < j] += 1
                if rating[i] < rating[j]:
                    b[i < j] += 1
            res += a[0]*b[1] + b[0]*a[1]
        return res