from dataStructer.Single_linked_List import ListUtility


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            head = head.next
            return head
        else:
            pre = head
            nxt = head.next
            while nxt.val != val:
                pre = nxt
                nxt = nxt.next
            pre.next = nxt.next
            return head


so = Solution()
lu = ListUtility()
node_list = lu.createList(9)
head = so.deleteNode(node_list,4)
while head:
    print(head.val)
    head = head.next
