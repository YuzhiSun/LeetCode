class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = list()
        self.stack = list()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min_stack:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
        else:
            return None




    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None


    def min(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(2)
obj.push(-1)
obj.pop()
param_3 = obj.top()
param_4 = obj.min()