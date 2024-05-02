# ruff: noqa: F403
# ruff: noqa: F405

from compiler.binarytree import TreeNode
from compiler.simple_evaluator import evaluate
from compiler.simple_tokens import *

class TestSimpleEvaluator:
    def test_add(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Plus())
        test_tree.left = TreeNode(Number('2'))
        test_tree.right = TreeNode(Number('1'))

        assert 2 + 1 == evaluate(test_tree)
    
    def test_minus(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Minus())
        test_tree.left = TreeNode(Number('2'))
        test_tree.right = TreeNode(Number('1'))

        assert 2 - 1 == evaluate(test_tree)
    
    def test_mult(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Mult())
        test_tree.left = TreeNode(Number('2'))
        test_tree.right = TreeNode(Number('1'))

        assert 2 * 1 == evaluate(test_tree)
    
    def test_div(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Div())
        test_tree.left = TreeNode(Number('2'))
        test_tree.right = TreeNode(Number('1'))

        assert 2 / 1 == evaluate(test_tree)
    
    def test_negation(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Number('2'))
        test_tree.left = TreeNode(Minus())

        assert -2 == evaluate(test_tree)
    
    def test_tree_with_no_reorder(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Plus())
        test_tree.left = TreeNode(Number('1'))
        test_tree.right = TreeNode(Mult())
        test_tree.right.left = TreeNode(Number('3'))
        test_tree.right.right = TreeNode(Number('4'))

        assert 1 + 3 * 4 == evaluate(test_tree)
    
    def test_tree_with_reorder(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Plus())
        test_tree.left = TreeNode(Mult())
        test_tree.left.left = TreeNode(Number('1'))
        test_tree.left.right = TreeNode(Number('3'))
        test_tree.right = TreeNode(Number('4'))

        assert 1 * 3 + 4 == evaluate(test_tree)
    
    def test_complex_tree(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Plus())
        test_tree.left = TreeNode(Minus())
        test_tree.left.left = TreeNode(Plus())
        test_tree.left.left.left = TreeNode(Number('1'))
        test_tree.left.left.right = TreeNode(Mult())
        test_tree.left.left.right.left = TreeNode(Number('3'))
        test_tree.left.left.right.right = TreeNode(Number('2'))
        test_tree.left.right = TreeNode(Div())
        test_tree.left.right.left = TreeNode(Number('5'))
        test_tree.left.right.right = TreeNode(Number('4'))
        test_tree.right = TreeNode(Number('7'))

        assert 1 + 3 * 2 - 5 / 4 + 7 == evaluate(test_tree)
    
    def test_simple_paren_tree(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Mult())
        test_tree.left = TreeNode(Number('1'))
        test_tree.right = TreeNode(Plus())
        test_tree.right.left = TreeNode(Number('3'))
        test_tree.right.right = TreeNode(Number('4'))

        assert 1 * (3 + 4) == evaluate(test_tree)
    
    def test_complex_paren_tree(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Mult())
        test_tree.left = TreeNode(Plus())
        test_tree.left.left = TreeNode(Number('1'))
        test_tree.left.right = TreeNode(Number('3'))
        test_tree.right = TreeNode(Minus())
        test_tree.right.left = TreeNode(Number('2'))
        test_tree.right.right = TreeNode(Plus())
        test_tree.right.right.left = TreeNode(Div())
        test_tree.right.right.left.left = TreeNode(Number('5'))
        test_tree.right.right.left.right = TreeNode(Number('4'))
        test_tree.right.right.right = TreeNode(Number('7'))

        assert (1 + 3) * (2 - (5 / 4 + 7)) == evaluate(test_tree)
    
    def test_simple_tree_with_negation_no_reorder(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Plus())
        test_tree.left = TreeNode(Number('1'))
        test_tree.right = TreeNode(Mult())
        test_tree.right.left = TreeNode(Number('3'))
        test_tree.right.left.left = TreeNode(Minus())
        test_tree.right.right = TreeNode(Number('4'))

        assert 1 + -3 * 4 == evaluate(test_tree)
    
    def test_simple_tree_with_negation_reorder(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Plus())
        test_tree.left = TreeNode(Mult())
        test_tree.left.left = TreeNode(Number('1'))
        test_tree.left.right = TreeNode(Number('3'))
        test_tree.left.right.left = TreeNode(Minus())
        test_tree.right = TreeNode(Number('4'))

        assert 1 * -3 + 4 == evaluate(test_tree)
    
    def test_complex_tree_with_negation(self):
        test_tree: TreeNode[TokenBase] = TreeNode(Mult())
        test_tree.left = TreeNode(Plus())
        test_tree.left.left = TreeNode(Number('1'))
        test_tree.left.right = TreeNode(Number('3'))
        test_tree.left.right.left = TreeNode(Minus())
        test_tree.right = TreeNode(Mult())
        test_tree.right.left = TreeNode(Number('1'))
        test_tree.right.left.left = TreeNode(Minus())
        test_tree.right.right = TreeNode(Minus())
        test_tree.right.right.left = TreeNode(Number('2'))
        test_tree.right.right.right = TreeNode(Plus())
        test_tree.right.right.right.left = TreeNode(Div())
        test_tree.right.right.right.left.left = TreeNode(Number('5'))
        test_tree.right.right.right.left.left.left = TreeNode(Minus())
        test_tree.right.right.right.left.right = TreeNode(Number('4'))
        test_tree.right.right.right.right = TreeNode(Number('7'))
        test_tree.right.right.right.right.left = TreeNode(Minus())

        assert (1 + -3) * -(2 - (-5 / 4 + -7)) == evaluate(test_tree)
