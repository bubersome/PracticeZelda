class Solution():
    """
    https://programmercarl.com/0349.两个数组的交集.html#其他语言版本
    """
    def __init__(self):
        self.nums1 # = [] it's ok to comment out the list
        self.nums2 = []

    def intersection( nums1, nums2) -> [int]:
        return list(set(nums1) & set(nums2))    # 两个数组先变成集合，求交集后还原为数组

s = [1,2,3,4,5]
t = [6,2,3,4,5]

ans = Solution.intersection(s,t)
print(ans)

"""
original: 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))    # 两个数组先变成集合，求交集后还原为数组
"""