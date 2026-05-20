class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while right > left:
            if height[left] > height[right]:
                h = height[right]
            else:
                h = height[left]
                
            area = h * (right - left)
            
            if area > max_water:
                max_water = area
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return max_water