# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:01:59 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

from mlbt import MutableLinkedBinaryTree

def in_order_traversal(tree, position):
    if tree.left(position) is not None:
        in_order_traversal(tree, tree.left(position))
    print(position.element(), end=" ")
    if tree.right(position) is not None:
        in_order_traversal(tree, tree.right(position))

def construct_bst(tree, position, elements):
    if len(elements) == 0:
        return
    mid = len(elements) // 2
    tree.replace(position, elements[mid])
    if len(elements) > 1:
        left_elements = elements[:mid]
        right_elements = elements[mid+1:]

        if tree.left(position) is None:
            tree.add_left(position, None)
        if tree.right(position) is None:
            tree.add_right(position, None)

        construct_bst(tree, tree.left(position), left_elements)
        construct_bst(tree, tree.right(position), right_elements)


def convert_to_bst(tree):
    in_order_elements = [p.element() for p in tree.inorder()]
    in_order_elements.sort()
    construct_bst(tree, tree.root(), in_order_elements)