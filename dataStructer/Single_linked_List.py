class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class ListUtility:
    def __init__(self):
        self.head = None
        self.tail = None
    def createList(self,nodeNum):
        if nodeNum <= 0:
            return None
        head = None
        val = 0
        node = None
        while nodeNum > 0:
            if head is None:
                head = ListNode(val)
                node = head
            else:
                node.next = ListNode(val)
                node = node.next
                self.tail = node
            val += 1
            nodeNum -= 1
        self.head = head
        return head