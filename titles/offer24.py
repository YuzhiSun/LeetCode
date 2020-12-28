from dataStructer.Single_linked_List import ListUtility


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

so = Solution()
list_nodes = ListUtility()
head = list_nodes.createList(5)
head1 = so.reverseList(head)
while head1:
    print(head1.val)
    head1 = head1.next
