class Solution:
    """
    两数之和
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/two-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    @staticmethod
    def two_sum_1(nums: list, target: int) -> list:
        """
        思路: 获取列表长度，嵌套for循环，因为不能重复，所以内循环开始的地方的外循环当前位置的后一个元素
        low比写法
        """
        for index_o, value_o in enumerate(nums):
            rest_value = target - value_o
            for index_i, value_i in enumerate(nums[index_o + 1:]):
                if value_i == rest_value:
                    return [index_o, index_i + index_o + 1]
        return []

    @staticmethod
    def two_sum_2(nums: list, target: int) -> list:
        """
        思路: 设定一个字典，保存着当前访问的列表的值和索引，之后判断是否在该字典中存在差值，存在的话即是所需
        """
        nums_dict = dict()
        for index, value in enumerate(nums):
            rest_value = target - value
            if rest_value in nums_dict:
                return [nums_dict[rest_value], index]
            nums_dict[value] = index
        return []
