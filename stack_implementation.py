import random

class Stack():

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        result = list()
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        result.reverse()
        return str(result)

    def __len__(self):
        return self.size

    def push(self, data):
        temp = Stack.Node(data)
        if not self.head:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
        self.size+=1

    def peek(self):
        if not self.head:
            return None
        else:
            return self.head.data

    def pop(self):
        if not self.head:
            raise Exception('empty stack!')
        else:
            temp = self.head
            self.head = self.head.next
            self.size-=1
            return temp.data


def main():
    their_stack = list()
    my_stack = Stack()
    assert len(their_stack)==len(my_stack)
    n = 10
    lo = 0
    hi = 99
    arr = [random.randint(lo, hi) for i in range(n)]
    for num in arr:
        their_stack.append(num)
        my_stack.push(num)
        assert str(their_stack)==str(my_stack)
        assert len(their_stack)==len(my_stack)
    for _ in arr:
        val1 = their_stack.pop()
        val2 = my_stack.pop()
        assert val1==val2
        assert len(their_stack)==len(my_stack)


if __name__ == "__main__":
    main()

