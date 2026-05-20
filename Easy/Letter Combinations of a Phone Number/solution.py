class Solution:
    def combine(self, l1, l2): 
        res = []
        
        for i in range(len(l1)):
            for j in range(len(l2)):
                res.append(l1[i] + l2[j])
                
        return res

            
            
            
    def letterCombinations(self, digits: str):
        digits_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j','k', 'l'],
            '6': ['m', 'o', 'n'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 1:
            return digits_to_letters[digits[0]]

        res = self.combine(digits_to_letters[digits[0]], digits_to_letters[digits[1]])
        
        if len(digits) > 2:
            print("yes")
            for i in range(2, len(digits)):
                res = self.combine(res, digits_to_letters[digits[i]])

        return res
            
        