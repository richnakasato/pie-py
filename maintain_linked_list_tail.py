import random

class LinkedList():

    class Node():

        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        res = ''
        dummy = LinkedList.Node()
        dummy.next = self.head
        curr = dummy
        res += '(size={}) '.format(self.size)
        while curr.next:
            res+='{}-> '.format(curr.next.data)
            curr = curr.next
        res+='None'
        return res

    def insert_after(self, node, data):
        temp = LinkedList.Node(data)
        if not node:
            if not self.head:
                self.head = self.tail = temp
            else:
                temp.next = self.head
                self.head = temp
        else:
            curr = self.head
            while curr:
                if curr == node:
                    temp.next = curr.next
                    curr.next = temp
                    if self.tail == node:
                        self.tail = temp
                    break
                else:
                    curr = curr.next
        self.size+=1

    def delete(self, node):
        if not node or not self.head:
            raise Exception('cannot delete')
        else:
            dummy = LinkedList.Node()
            dummy.next = self.head
            curr = dummy
            while curr.next:
                if curr.next == node:
                    curr.next = curr.next.next
                    if self.tail == node:
                        self.tail = curr.next
                    break
                else:
                    curr = curr.next
            self.size-=1


def main():
    ll = LinkedList()
    ll.insert_after(None, 1)
    ll.insert_after(None, 2)
    print(ll.head.data)
    print(ll.tail.data)
    print(ll)



if __name__ == "__main__":
    main()

