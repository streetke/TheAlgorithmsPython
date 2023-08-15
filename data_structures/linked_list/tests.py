import unittest
import singly_linked_list


def has_cycle(head) -> bool:
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next
    return True


class TestSinglyLinkedList(unittest.TestCase):
    def test_head_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        self.assertEqual(0, linked_list.__getitem__(0))

    def test_tail_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        linked_list.insert_nth(1, 1)
        linked_list.insert_tail(2)
        self.assertEqual(2, linked_list.__getitem__(2))

    def test_nth_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        linked_list.insert_nth(1, 1)
        linked_list.insert_tail(2)
        self.assertEqual(1, linked_list.__getitem__(1))

    def test_delete_head_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        linked_list.insert_tail(2)
        linked_list.delete_head()
        self.assertEqual(2, linked_list.__getitem__(0))

    def test_delete_tail_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        linked_list.insert_nth(1, 1)
        linked_list.insert_tail(2)
        linked_list.delete_tail()
        self.assertEqual(1, linked_list.__getitem__(1))

    def test_empty_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        linked_list.insert_nth(1, 1)
        linked_list.insert_tail(2)
        linked_list.delete_nth(1)
        linked_list.delete_tail()
        linked_list.delete_head()
        self.assertTrue(linked_list.is_empty())

    def test_reverse_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        linked_list.insert_nth(1, 1)
        linked_list.insert_tail(2)
        linked_list.reverse()
        self.assertEqual(0, linked_list.__getitem__(2))
        self.assertEqual(2, linked_list.__getitem__(0))

    def test_cycle_singly_linked_list(self):
        linked_list = singly_linked_list.LinkedList()
        linked_list.insert_head(0)
        linked_list.insert_nth(1, 1)
        linked_list.insert_tail(2)
        response = has_cycle(linked_list.head)
        self.assertFalse(response)


if __name__ == '__main__':
    unittest.main(verbosity=2)

