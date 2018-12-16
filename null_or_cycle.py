def has_cycle(head):
    slow = fast = head
    while slow and fast.next and fast.next.next:
        if slow = fast.next:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


def main():
    pass


if __name__ == "__main__":
    main()

