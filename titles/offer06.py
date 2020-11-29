from dataStructer.Single_linked_List import ListUtility


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack_ = list()
        res_lst = list()
        if not head:
            return []

        while (head.next):
            stack_.append(head.val)
            head = head.next
        stack_.append(head.val)
        for i in range(0, len(stack_)):
            res_lst.append(stack_.pop())
        return res_lst
SingleLinklist = ListUtility()
head = SingleLinklist.createList(nodeNum=6)
so = Solution()
res = so.reversePrint(head)
print(res)

