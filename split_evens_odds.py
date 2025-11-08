# split_evens_odds.py
from singly_linked_list import SinglyLinkedList, Node

class SplitEvensOdds(SinglyLinkedList):
    def split_even_odd(self):
        """Split into (evens, odds) by re-linking existing nodes only.
        Leaves self empty. No new nodes created or deleted.
        """
        if self.is_empty():
            raise ValueError("Cannot split an empty list.")

        evens = SinglyLinkedList()
        odds  = SinglyLinkedList()

        cur = self.head
        # clear original list
        self.head = self.tail = None
        self.count = 0

        while cur:
            nxt = cur.next
            cur.next = None  # detach
            target = evens if (cur.data % 2 == 0) else odds
            if target.tail is None:
                target.head = target.tail = cur
            else:
                target.tail.next = cur
                target.tail = cur
            target.count += 1
            cur = nxt

        return evens, odds
