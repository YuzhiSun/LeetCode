# 虽然可以运行 但是方法错误 因为用了三个栈
class CQueue_err(object):

    def __init__(self):
        self.head_stk = list()
        self.tail_stk = list()

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.tail_stk.append(value)
        self.update_head()

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.head_stk:
            res = self.head_stk.pop()
            self.update_tail()
            return res

        else:
            return -1
    def update_head(self):
        """
        while tail is changed
        :return: None
        """
        tmp_stk = self.tail_stk.copy()
        self.head_stk.clear()
        while self.tail_stk:
            self.head_stk.append(self.tail_stk.pop())
        self.tail_stk = tmp_stk.copy()
        del tmp_stk
    def update_tail(self):
        """
        while head is changed
        :return: None
        """
        tmp_stk = self.head_stk.copy()
        self.tail_stk.clear()
        while self.head_stk:
            self.tail_stk.append(self.head_stk.pop())
        self.head_stk = tmp_stk.copy()
        del tmp_stk
class CQueue(object):

    def __init__(self):
        self.push_stk = list()
        self.pop_stk = list()

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.push_stk.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if self.pop_stk:
            return self.pop_stk.pop()
        elif self.push_stk:
            while self.push_stk:
                self.pop_stk.append(self.push_stk.pop())
            return self.pop_stk.pop()
        else:
            return -1



obj = CQueue()
obj.appendTail(3)
param_2 = obj.deleteHead()
param_3 = obj.deleteHead()
