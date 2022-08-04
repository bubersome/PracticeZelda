
"""
# 541. 反转字符串II
，贡献其他语言版本的代码，拥抱开源，让更多学习算法的小伙伴们收益！

简单的反转还不够，我要花式反转

力扣题目链接
https://leetcode.cn/problems/reverse-string-ii/

给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:
"""

def reverseStr(s: str, k: int) -> str:
    p = 0
    while p < len(s):
        p2 = p + k

        s = s[:p] + s[p: p2][::-1] + s[p2:] #[::-1]
        p = p + 2 * k
    return s
"""
Assuming a is a string. The Slice notation in python has the syntax -

list[<start>:<stop>:<step>]
So, when you do a[::-1], it starts from the end towards the first taking each element. So it reverses a. This is applicable for lists/tuples as well.

"""
# reverseStr("abcde",2)
print(reverseStr("abcde",2))


def reverseStringI(s :str) -> str:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    s = list(s)
    # print(s[1])
    # 该方法已经不需要判断奇偶数，经测试后时间空间复杂度比用 for i in range(right//2)更低
    # 推荐该写法，更加通俗易懂
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
        new_s = str().join(s)
        # new_s = ''.join(s)
    return new_s

s= "abcd"
print(reverseStringI(s))
