class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


def mth_to_last(head, m):
    if not head:
        return None
    else:
        count = 0
        slow = fast = head
        while fast.next:
            fast = fast.next
            if count == m:
                slow = slow.next
            else:
                count += 1
        return slow


def main():
    head = Node(1)
    head.next = Node(2)
    mth_node = Node(3)
    head.next.next = mth_node
    m = 0
    assert mth_to_last(head, m)==mth_node
    head.next.next.next = Node(4)
    m = 1
    assert mth_to_last(head, m)==mth_node
    m = 10
    assert mth_to_last(head, m)==head
    m = 2
    assert mth_to_last(head, m)==head.next
    return


if __name__ == "__main__":
    main()

