class Stack(object):
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈的存放极限

    def push(self, data):  # 存入数据
        if len(self.stack) >= self.limit:  # 判断是否为空
            print('stack overflow')
            pass
        self.stack.append(data)

    def pop(self):  # 弹出最外层的数据
        if self.stack:
            self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')  # 空栈不能弹出

    def peek(self):  # 查看栈顶的元素
        if self.stack:
            return self.stack[-1]

    def is_empty(self):  # 判断是否为空
        return not bool(self.stack)

    def size(self):  # 返回栈的大小
        return len(self.stack)

A = Stack()
A.push('stack')
A.push('数据结构')
print(A.size())
print(A.is_empty())
print(A.peek())
A.pop()
print(A.peek())
A.pop()
print(A.peek())
