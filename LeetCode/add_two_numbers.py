# -*- coding: utf-8 -*-
# @Author   : morn
# @Time     : 2019/7/5 23:14
# @File     : add_two_numbers.py
# @Software : PyCharm


class ListNode:
    """
    单向链表
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/add-two-numbers
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    @staticmethod
    def add_two_numbers_1(l1: ListNode, l2: ListNode) -> ListNode:
        """
        解题思路: 首先根据示例以及ListNode这个类的初始化定义来看，这两个数是一个单向链表
        需要考虑集中情况：
            ① 两个链表的节点数量相等
            ② 两个链表的节点不相等
        并且还注意到一点，两个数相加之后，该节点的val其实是除10取余的结果，而如果整除10的值大于0，在下一个节点中还需要加上这次整除10的值
        :return:
        """
        list_nodes = rest_list_nodes = None
        next_add = 0
        while True:
            if l1 and l2:
                l1v = l1.val
                l2v = l2.val
                next_add, value = divmod(l1v + l2v + next_add, 10)
                node = ListNode(value)
                if list_nodes is None:
                    list_nodes = node
                    rest_list_nodes = list_nodes
                else:
                    pass

