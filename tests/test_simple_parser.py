# ruff: noqa: F403
# ruff: noqa: F405

from compiler.binarytree import TreeNode
from compiler.simple_tokens import *
from compiler.simple_parser import parse


class TestSimpleParser:
    def test_simple_src_no_reorder(self):
        test_src_tokens = [
            Number('1'),
            Plus(),
            Number('3'),
            Mult(),
            Number('4'),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Plus())
        expected_tree.left = TreeNode(Number('1'))
        expected_tree.right = TreeNode(Mult())
        expected_tree.right.left = TreeNode(Number('3'))
        expected_tree.right.right = TreeNode(Number('4'))

        assert expected_tree == parse(test_src_tokens)

    def test_simple_src_with_reorder(self):
        test_src_tokens = [
            Number('1'),
            Mult(),
            Number('3'),
            Plus(),
            Number('4'),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Plus())
        expected_tree.left = TreeNode(Mult())
        expected_tree.left.left = TreeNode(Number('1'))
        expected_tree.left.right = TreeNode(Number('3'))
        expected_tree.right = TreeNode(Number('4'))

        assert expected_tree == parse(test_src_tokens)

    def test_complex_src(self):
        test_src_tokens = [
            Number('1'),
            Plus(),
            Number('3'),
            Mult(),
            Number('2'),
            Minus(),
            Number('5'),
            Div(),
            Number('4'),
            Plus(),
            Number('7'),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Plus())
        expected_tree.left = TreeNode(Minus())
        expected_tree.left.left = TreeNode(Plus())
        expected_tree.left.left.left = TreeNode(Number('1'))
        expected_tree.left.left.right = TreeNode(Mult())
        expected_tree.left.left.right.left = TreeNode(Number('3'))
        expected_tree.left.left.right.right = TreeNode(Number('2'))
        expected_tree.left.right = TreeNode(Div())
        expected_tree.left.right.left = TreeNode(Number('5'))
        expected_tree.left.right.right = TreeNode(Number('4'))
        expected_tree.right = TreeNode(Number('7'))

        assert expected_tree == parse(test_src_tokens)
    
    def test_simple_parens(self):
        test_src_tokens = [
            Number('1'),
            Mult(),
            LeftParen(),
            Number('3'),
            Plus(),
            Number('4'),
            RightParen(),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Mult())
        expected_tree.left = TreeNode(Number('1'))
        expected_tree.right = TreeNode(Plus())
        expected_tree.right.left = TreeNode(Number('3'))
        expected_tree.right.right = TreeNode(Number('4'))

        assert expected_tree == parse(test_src_tokens)
    
    def test_complex_parens(self):
        # (1 + 3) * (2 - (5 / 4 + 7))
        test_src_tokens = [
            LeftParen(),
            Number('1'),
            Plus(),
            Number('3'),
            RightParen(),
            Mult(),
            LeftParen(),
            Number('2'),
            Minus(),
            LeftParen(),
            Number('5'),
            Div(),
            Number('4'),
            Plus(),
            Number('7'),
            RightParen(),
            RightParen(),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Mult())
        expected_tree.left = TreeNode(Plus())
        expected_tree.left.left = TreeNode(Number('1'))
        expected_tree.left.right = TreeNode(Number('3'))
        expected_tree.right = TreeNode(Minus())
        expected_tree.right.left = TreeNode(Number('2'))
        expected_tree.right.right = TreeNode(Plus())
        expected_tree.right.right.left = TreeNode(Div())
        expected_tree.right.right.left.left = TreeNode(Number('5'))
        expected_tree.right.right.left.right = TreeNode(Number('4'))
        expected_tree.right.right.right = TreeNode(Number('7'))

        assert expected_tree == parse(test_src_tokens)
    
    def test_single_negation(self):
        # -3
        test_src_tokens = [
            Minus(),
            Number('3')
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Number('3'))
        expected_tree.left = TreeNode(Minus())

        assert expected_tree == parse(test_src_tokens)
    
    def test_simple_negation_with_no_reorder(self):
        # 1 + -3 * 4
        test_src_tokens = [
            Number('1'),
            Plus(),
            Minus(),
            Number('3'),
            Mult(),
            Number('4'),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Plus())
        expected_tree.left = TreeNode(Number('1'))
        expected_tree.right = TreeNode(Mult())
        expected_tree.right.left = TreeNode(Number('3'))
        expected_tree.right.left.left = TreeNode(Minus())
        expected_tree.right.right = TreeNode(Number('4'))

        assert expected_tree == parse(test_src_tokens)
    
    def test_simple_negation_with_reorder(self):
        # 1 * -3 + 4
        test_src_tokens = [
            Number('1'),
            Mult(),
            Minus(),
            Number('3'),
            Plus(),
            Number('4'),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Plus())
        expected_tree.left = TreeNode(Mult())
        expected_tree.left.left = TreeNode(Number('1'))
        expected_tree.left.right = TreeNode(Number('3'))
        expected_tree.left.right.left = TreeNode(Minus())
        expected_tree.right = TreeNode(Number('4'))

        assert expected_tree == parse(test_src_tokens)
    
    def test_complex_negation(self):
        # (1 + -3) * -(2 - (-5 / 4 + -7))
        test_src_tokens = [
            LeftParen(),
            Number('1'),
            Plus(),
            Minus(),
            Number('3'),
            RightParen(),
            Mult(),
            Minus(),
            LeftParen(),
            Number('2'),
            Minus(),
            LeftParen(),
            Minus(),
            Number('5'),
            Div(),
            Number('4'),
            Plus(),
            Minus(),
            Number('7'),
            RightParen(),
            RightParen(),
        ]

        expected_tree: TreeNode[TokenBase] = TreeNode(Mult())
        expected_tree.left = TreeNode(Plus())
        expected_tree.left.left = TreeNode(Number('1'))
        expected_tree.left.right = TreeNode(Number('3'))
        expected_tree.left.right.left = TreeNode(Minus())
        expected_tree.right = TreeNode(Mult())
        expected_tree.right.left = TreeNode(Number('1'))
        expected_tree.right.left.left = TreeNode(Minus())
        expected_tree.right.right = TreeNode(Minus())
        expected_tree.right.right.left = TreeNode(Number('2'))
        expected_tree.right.right.right = TreeNode(Plus())
        expected_tree.right.right.right.left = TreeNode(Div())
        expected_tree.right.right.right.left.left = TreeNode(Number('5'))
        expected_tree.right.right.right.left.left.left = TreeNode(Minus())
        expected_tree.right.right.right.left.right = TreeNode(Number('4'))
        expected_tree.right.right.right.right = TreeNode(Number('7'))
        expected_tree.right.right.right.right.left = TreeNode(Minus())

        assert expected_tree == parse(test_src_tokens)
