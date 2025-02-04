'''
328. Odd Even Linked List
Link: https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Examples:
1. [1, 2, 3, 4, 5] -> [1, 3, 5, 2, 4]
2. [2, 1, 3, 5, 6, 4, 7] -> [2, 3, 6, 7, 1, 5, 4]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    odd_head = ListNode(0)
    odd = odd_head

    even_head = ListNode(0)
    even = even_head

    count = 1
    while head:
        if count % 2 == 0:
            even.next = head
            even = head
        else:
            odd.next = head
            odd = head

        count += 1
        head = head.next

    even.next = None
    odd.next = even_head.next


def oddEvenList_v2(head):
    if not head or not head.next:
        return head

    odd, even = head, head.next
    even_head = even

    while even and even.next:
        nxt_odd, nxt_even = odd.next.next, even.next.next

        odd.next = nxt_odd
        odd = nxt_odd

        even.next = nxt_even
        even = nxt_even

    odd.next = even_head
    return head


def oddEvenList_v3(head):
    if not head or not head.next:
        return head

    odd, even = head, head.next
    even_head = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head
    return head
