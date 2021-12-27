from unittest import TestCase
from IMP.Classes import DiGraph, Path


class TestPath(TestCase):
    def setUp(self) -> None:
        self.dg = DiGraph()
        for n in range(4):
            self.dg.add_node(n)
        self.dg.add_edge(0, 1, 1)
        self.dg.add_edge(1, 0, 1)
        self.dg.add_edge(1, 2, 1)
        self.dg.add_edge(2, 3, 1)
        self.dg.add_edge(1, 3, 1)
        self.p = Path(self.dg)

    def test_add(self):
        self.assertEqual(0, self.p.get_length())
        self.p.add(0)
        self.p.add(1)
        self.assertEqual(2, self.p.get_length())
        self.assertEqual(1, self.p.weight)

    def test_remove(self):  # um.. wat
        self.assertEqual(0, self.p.get_length())
        self.p.add(0)
        self.p.add(1)
        self.assertEqual(2, self.p.get_length())
        self.assertEqual(1, self.p.weight)
        self.p.remove(True)     # remove last node -> 1
        self.assertEqual(0, self.p.weight)

    def test_merge(self):
        self.p.add(1)
        self.p.add(0)
        p2 = Path(self.dg)
        p2.add(3)
        p2.add(2)
        self.p.merge(p2)
        self.assertEqual(4, self.p.get_length())
        self.assertEqual(3, self.p.weight)


if __name__ == '__main__':
    TestCase.main()
