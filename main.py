# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:03:47 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

from mlbt import MutableLinkedBinaryTree
from tree_converter import in_order_traversal, convert_to_bst


if __name__ == "__main__":
    lbt = MutableLinkedBinaryTree()
    lbt.add_root(10)
    lbt.add_left(lbt.root(), 3)
    lbt.add_right(lbt.root(), 1)

    l = lbt.left(lbt.root())
    r = lbt.right(lbt.root())

    lbt.add_left(l, 2)
    lbt.add_right(l, 6)

    lbt.add_left(r, 9)
    lbt.add_right(r, 7)

    print("Original Tree (In-order traversal):")
    in_order_traversal(lbt, lbt.root())
    print()

    convert_to_bst(lbt)

    print("Binary Search Tree (In-order traversal):")
    in_order_traversal(lbt, lbt.root())
