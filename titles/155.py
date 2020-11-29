class MinStack(object):
# 根据题解 学会了使用辅助栈
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()


    def push(self, x:int):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.min_stack.append(x)
        else:
            if self.min_stack[-1] < x:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(x)
        self.stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """


        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()

