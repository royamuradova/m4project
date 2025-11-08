# main.py
from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

def test_singly_linked_list():
    sll = SinglyLinkedList()
    print("---- Build a forward list ----")
    sll.build_list_forward([10, 20, 30, 40, 50])
    print(str(sll))
    print("Delete the first node:", end=" ")
    sll.delete_first(); print(str(sll))
    print("Delete the last node:", end=" ")
    sll.delete_last(); print(str(sll))
    print("Delete the interior node:", end=" ")
    sll.delete_value(30); print(str(sll))

    print("\n---- Build a backward list ----")
    sll.build_list_backward([50, 40, 30, 20, 10])
    print(str(sll))
    print("Delete the first node:", end=" ")
    sll.delete_first(); print(str(sll))
    print("Delete the last node:", end=" ")
    sll.delete_last(); print(str(sll))
    print("Delete the interior node:", end=" ")
    sll.delete_value(30); print(str(sll))

    print("\n---- Non-recursive reverse print test----")
    sll = SinglyLinkedList()
    sll.build_list_forward([10, 20, 30, 40, 50])
    print("Insertion order:", str(sll))
    print("Reverse order (non-recursive):", sll.display_reverse_nr())

    print("\n---- Remove all test ----")
    sll = SinglyLinkedList()
    sll.build_list_forward([1, 2, 4, 6, 1, 3, 6])
    print(str(sll))
    print("Removing 1 and all duplicates:", end=" ")
    sll.remove_all(1); print(str(sll))
    print("Removing 6 and all duplicates:", end=" ")
    sll.remove_all(6); print(str(sll))

def test_split_evens_odds():
    base = SplitEvensOdds()
    base.build_list_forward([1,2,3,4,5,6,7,8,15,14,13,12,11,10,9])
    print(str(base))
    evens, odds = base.split_even_odd()
    print(str(evens))
    print(str(odds))
    print(str(base))  # original should now be empty → "Head -> None"

if __name__ == "__main__":
    test_singly_linked_list()
    print()
    test_split_evens_odds()
