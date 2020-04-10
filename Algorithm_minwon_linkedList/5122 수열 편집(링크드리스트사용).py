class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodesize = 0

    def append(self, data): # 끝에 값을 추가해주는 메소드
        newNode = Node(data)
        if (self.head):
            current = self.head
            while current.next:
                current = current.next
            self.tail = newNode
            current.next = self.tail
        else:
            self.head = newNode
            self.tail = newNode
        self.nodesize += 1

    def insert(self, index, data):
        newNode = Node(data)
        if self.head:
            if index == 0:
                if self.nodesize == 1:
                    temp = Node(self.head.data, self.head.next)
                    self.head = newNode
                    self.tail = temp
                    self.head.next =  self.tail
                else:
                    temp = Node(self.head.data, self.head.next)
                    self.head = newNode
                    self.head.next = temp
            else:
                if index < self.nodesize:
                    current = self.head
                    cnt = 0
                    while cnt < index:
                        prevent = current
                        current = current.next
                        cnt += 1
                    prevent.next =  newNode
                    newNode.next = current
                else:
                    current =  self.head
                    cnt = 0
                    while cnt < index:
                        prevent =  current
                        current =  current.next
                        cnt += 1
                    self.tail = newNode
                    prevent.next = self.tail
        else:
            self.head = newNode
            self.tail = newNode
        self.nodesize += 1

    def