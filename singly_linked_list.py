# singly_linked_list.py

class Node:
    __slots__ = ("data", "next")
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # -------- utilities --------
    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.count

    def __str__(self):
        parts = ["Head ->"]
        cur = self.head
        while cur:
            parts.append(f" {cur.data} ->")
            cur = cur.next
        parts.append(" None")
        return " ".join(parts)

    def _append_node(self, node: Node):
        node.next = None
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def _prepend_node(self, node: Node):
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.count += 1

    # -------- build methods (per assignment) --------
    def build_list_forward(self, values):
        self.head = self.tail = None
        self.count = 0
        for v in values:
            self._append_node(Node(v))

    def build_list_backward(self, values):
        self.head = self.tail = None
        self.count = 0
        for v in values:
            self._prepend_node(Node(v))

    # -------- deletions --------
    def delete_first(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.count -= 1
        if self.head is None:
            self.tail = None

    def delete_last(self):
        if self.is_empty():
            return
        if self.head is self.tail:
            self.head = self.tail = None
            self.count = 0
            return
        prev, cur = None, self.head
        while cur.next:
            prev, cur = cur, cur.next
        prev.next = None
        self.tail = prev
        self.count -= 1

    def delete_value(self, value):
        """Delete first occurrence of value (interior delete)."""
        prev, cur = None, self.head
        while cur:
            if cur.data == value:
                if prev is None:
                    self.delete_first()
                elif cur is self.tail:
                    prev.next = None
                    self.tail = prev
                    self.count -= 1
                else:
                    prev.next = cur.next
                    self.count -= 1
                return True
            prev, cur = cur, cur.next
        return False

    # -------- required extras --------
    def remove_all(self, value):
        """Remove all nodes with the given value."""
        prev, cur = None, self.head
        while cur:
            if cur.data == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self.count -= 1
                cur = cur.next
            else:
                prev, cur = cur, cur.next

    def display_reverse_nr(self):
        """Non-recursive reverse print using a stack (format like sample)."""
        stack = []
        cur = self.head
        while cur:
            stack.append(cur.data)
            cur = cur.next
        if not stack:
            return "None <- Head"
        out = ["None <-", f" {stack.pop()}"]
        while stack:
            out.append(f" -> {stack.pop()}")
        out.append(" <- Head")
        return " ".join(out)
