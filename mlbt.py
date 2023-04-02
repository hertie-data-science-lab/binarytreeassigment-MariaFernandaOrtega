# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:31:59 2023

@author: Maria Fernanda Ortega and Maria Jose Lee
"""

from linkedbinarytree import LinkedBinaryTree

class MutableLinkedBinaryTree(LinkedBinaryTree):
    """
    Provides public wrapper functions for each of the inherited nonpublic update methods.
    """
    
    def add_root(self, e):
        return self._add_root(e)
        
    def add_left(self, p, e):
        return self._add_left(p, e)
    
    def add_right(self, p, e):
        return self._add_right(p, e)
        
    def replace(self, p, e):
        return self._replace(p, e)
    
    def delete(self, p):
        return self._delete(p)
        
    def attach(self, p, T1, T2):
        return self.attach(p, T1, T2)

    def preorder(self):
        return self._preorder()

    def subtree_preorder(self, p):
        return self._subtree_preorder(p)

    def postorder(self):
        return self._postorder()

    def subtree_postorder(self, p):
        return self._subtree_postorder(p)

    def inorder(self):
        return self._inorder()

    def subtree_inorder(self, p):
        return self._subtree_inorder(p)


