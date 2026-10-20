class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        if numRows == 3:
            return [[1], [1,1], [1,2,1]]
        
        res = [[1], [1,1], [1,2,1]]

        for i in range(2, numRows -1):
            tmp = []
            curr = res[i]
            for j in range(len(curr)):
                if j == 0:
                    tmp.append(curr[j])
                if j > 0:
                    tmp.append(curr[j - 1] + curr[j])
                if j == len(curr) - 1:
                    tmp.append(curr[j])

            res.append(tmp)

        return res
