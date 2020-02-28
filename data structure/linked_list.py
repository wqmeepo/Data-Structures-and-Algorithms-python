class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def print_el(self):
        print(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def init_list(self, data_list):  # 初始化链表
        self.head = Node(data_list[0])  # 创建头接点
        temp = self.head  # 逐步为datalist里面的数据创建接点
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def is_empty(self):  # 判断链表是否为空
        if self.head.next:
            return False
        else:
            print('linked list is empty')
            return True

    def get_length(self):  # 获取链表的长度
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def insert(self, key, value):
        if key<0 or key > self.get_length()-1:
            print('key is not valid')
        temp = self.head
        i = 0
        while i <= key:  # 遍历找到索引值为 key 的结点后, 在其后面插入结点
            pre = temp
            temp = temp.next
            i += 1
        node = Node(value)
        pre.next = node
        node.next = temp

    def print_list(self):
        print('linked list printed below')
        temp = self.head
        print_list = []
        while temp is not None:
            print_list.append(temp.data)
            temp = temp.next
        print(print_list)

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def remove(self, key):
        if key < 0 or key > self.get_length()-1:
            print('remove error')
        i = 0
        temp = self.head
        while i <= key:
            pre = temp
            temp = temp.next
            i += 1
        pre.next = temp.next

    def show_data(self, key):
        if key < 0 or key > self.get_length() - 1:
            print('error')
        i = 0
        temp = self.head
        while i <= key:
            pre = temp
            temp = temp.next
            i += 1
        pre.print_el()



