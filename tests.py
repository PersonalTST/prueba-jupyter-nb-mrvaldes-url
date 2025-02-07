# test.py
import unittest
from Lab3 import TreeNode, minimax

class TestMinimax(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(0, [
            TreeNode(3),
            TreeNode(5, [
                TreeNode(6),
                TreeNode(9),
                TreeNode(1)
            ]),
            TreeNode(-2, [
                TreeNode(7),
                TreeNode(-3),
                TreeNode(4)
            ])
        ])

    def test_minimax_maximizing(self):
        self.assertEqual(minimax(self.root, True), 5, "La prueba falló: el valor óptimo debería ser 5")

    def test_minimax_minimizing(self):
        self.assertEqual(minimax(self.root, False), 3, "La prueba falló: el valor óptimo debería ser 3")

if __name__ == '__main__':
    unittest.main()
