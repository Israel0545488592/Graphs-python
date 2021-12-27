import unittest
from IMP.Classes import DiGraph, TagHeap


class TestTagHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.dg = DiGraph()
        for n in range(4):
            self.dg.add_node(n)
        self.dg.add_edge(0, 1, 1)
        self.dg.add_edge(1, 2, 1)
        self.dg.add_edge(0, 3, 1)
        self.dg.add_edge(0, 2, 1)

        self.th = TagHeap(self.dg.v_size(), self.dg)
        self.th.min = 0
        self.th.values[0] = 0

    def test_get_min(self):
        self.assertEqual(0, self.th.min)

    def test_get(self):
        self.assertEqual(0, self.th.get(0))

    def test_relax(self):
        self.fail()

    def test_update_chosen(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
