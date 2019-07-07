# -*- coding: utf-8 -*-
# @Author   : morn
# @Time     : 2019/7/6 11:54
# @File     : longest_substring.py
# @Software : PyCharm
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def length_of_longest_substring_1(s: str) -> int:
    """
    这是第一种的解题思路，首先对字符串进行遍历，之后以每个字符串为起始，再遍历第二遍，有重复字符立马跳出循环
    并且将以当前字符的最大长度经过判断后选择性赋值给变量max_substring_len，直到遍历出所有字符
    该方法的时间复杂度是O(n^2)
    :param s:
    :return:
    """
    max_substring_len = 0
    for index, value in enumerate(s[: -1]):
        tmp_len = 1
        tmp_dict = {value: None}
        for sub_value in s[index + 1:]:
            if sub_value not in tmp_dict:
                tmp_dict[sub_value] = None
                tmp_len += 1
            else:
                break
        max_substring_len = tmp_len if tmp_len > max_substring_len else max_substring_len
    return max_substring_len


def length_of_longest_substring_2(s: str) -> int:
    """
    这是第二种解题思路，第一种解题方法时间复杂度太高，效率太低，所以看了题解后，参考除了这种方法
    这种是利用滑动窗口的思路，在没有重复元素之前，一直向里面添加元素，保存最大长度值，直到有重复的，那么从s字符串保留在窗口的起始位置开始
    删除，直到没有重复元素，直到遍历完字符串，这种方法因为有一个for循环，一个while循环，我理解时间复杂度应该也是O(n^2),但是运行效率
    确实比第一种快了很多
    :param s:
    :return:
    """
    if not s:
        return 0
    max_substring_len = 0
    current_len = 0
    substring_set = set()
    start = 0
    for char in s:
        while char in substring_set:
            substring_set.remove(s[start])
            current_len -= 1
            start += 1
        substring_set.add(char)
        current_len += 1
        max_substring_len = current_len if current_len > max_substring_len else max_substring_len
    return max_substring_len


def longest_substring_length(s):
    """
    这是第三种做法，参考的是力扣上运行速度最快的，它生成一个字典，之后将字符及字符的位置加入到字典中，当有重复的时候，获取字符
    的位置并且+1，判断与当前的start起始位置比大小，大的话覆盖当前起始位置，这种解法当时理解了很久，才明白。。。
    时间复杂度：O(n),运行短的字符串与第二种差不多，长的没试验。
    :param s:
    :return:
    """
    # 创建字典，用来记录所有字符及其出现的位置，用于之后调整起始位置
    char_dict = dict()
    # 声明起始位置和最大长度
    maxlength = start = 0
    for index, char in enumerate(s):
        # 判断char是否在字典中，在的话说明字典中已经存在
        if char in char_dict:
            # 修改起始位置
            char_next_index = char_dict[char] + 1
            if char_next_index > start:
                start = char_next_index
        # 判断当前长度
        current_len = index - start + 1
        if current_len > maxlength:
            maxlength = current_len
        # 无论是否存在，将当前字符的位置写入字典
        char_dict[char] = index
    return maxlength
