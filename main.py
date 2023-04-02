# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Maria Fernanda Ortega and Maria Jose Lee
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)




print(len(lbt))
print(lbt.height(lbt.root()))

print("Pre-order method:")
for p in lbt.preorder():
    print(p.element())

print("Post-order method:")
for node in lbt.postorder():
    print(node.element())


print("In-order method:")
for p in lbt.inorder():
    print(p.element())



