#coding ： utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def carryHandle(l):
    '''
    :param l:
    :return:
    进位操作
    '''
    lr = l
    tip = 0
    while True:
        lr.val += tip
        if lr.val > 9:
            tip = 1
            lr.val -= 10
        else:
            tip = 0

        if lr.next is not None:
            lr = lr.next
        else:
            if tip == 0:
                return l
            else:
                lr.next = ListNode(1)
                return l


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3_h = ListNode(l1.val + l2.val)
        l3 = l3_h
        while True:
            if l1.next is not None or l2.next is not None:
                if l1.next is not None:
                    l1 = l1.next
                else:
                    l1.next = ListNode(0)
                    l1 = l1.next

                if l2.next is not None:
                    l2 = l2.next
                else:
                    l2.next = ListNode(0)
                    l2 = l2.next
            else:
                return carryHandle(l3_h)

            l3.next = ListNode(l1.val + l2.val)
            l3 = l3.next