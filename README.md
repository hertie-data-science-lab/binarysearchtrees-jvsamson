[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/L0P4fZaj)
# Assignment:

Write a program that converts a binary tree into a binary search tree. I will not tell you the steps for how to do this, you will need to figure out the algorithm. However, here are some hints:

* What is the main difference between a binary search tree and a binary tree?
* What could be the middle step between a binary tree and a binary search tree?

You should start with a regular binary tree, using the code from the Binary Tree Assignment. Create a tree and then convert it to a binary search tree.
* Make your code *modular*!
* Respect code blocks and line spaces, naming conventions.
* Document (but do not leave comments)
* Do exactly what is asked. There will be no points for *Above and Beyond* this assignment.
* List your group's members in the header of the main file.


# Answers to Assignment Questions:
* What is the main difference between a binary search tree and a binary tree?

  The main difference between a binary search tree and a binary tree is that in a binary search tree, for each node, all the elements in the left subtree are smaller than the node's value, and all the elements in the right subtree are greater than or equal to the node's value. In a regular binary tree, there is no specific ordering rule.

* What could be the middle step between a binary tree and a binary search tree?

  The middle step between a binary tree and a binary search tree could be performing an in-order traversal of the binary tree, which will visit the nodes in a sorted order (if the tree were a binary search tree). The in-order traversal output can be used to construct a new binary search tree or modify the existing binary tree to adhere to the binary search tree rules.
