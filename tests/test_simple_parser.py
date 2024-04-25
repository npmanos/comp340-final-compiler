from compiler.binarytree import TreeNode
from compiler.simple_tokenizer import Token
from compiler.simple_parser import parse


class TestSimpleParser:
    def test_simple_src_no_reorder(self):
        test_src_tokens = [
            Token(value="1", type="NUMB"),
            Token(value="+", type="PLUS"),
            Token(value="3", type="NUMB"),
            Token(value="*", type="MULT"),
            Token(value="4", type="NUMB"),
        ]

        expected_tree = TreeNode(Token(value="+", type="PLUS"))
        expected_tree.left = TreeNode(Token(value="1", type="NUMB"))
        expected_tree.right = TreeNode(Token(value="*", type="MULT"))
        expected_tree.right.left = TreeNode(Token(value="3", type="NUMB"))
        expected_tree.right.right = TreeNode(Token(value="4", type="NUMB"))

        assert expected_tree == parse(test_src_tokens)

    def test_simple_src_with_reorder(self):
        test_src_tokens = [
            Token(value="1", type="NUMB"),
            Token(value="*", type="MULT"),
            Token(value="3", type="NUMB"),
            Token(value="+", type="PLUS"),
            Token(value="4", type="NUMB"),
        ]

        expected_tree = TreeNode(Token(value="+", type="PLUS"))
        expected_tree.left = TreeNode(Token(value="*", type="MULT"))
        expected_tree.left.left = TreeNode(Token(value="1", type="NUMB"))
        expected_tree.left.right = TreeNode(Token(value="3", type="NUMB"))
        expected_tree.right = TreeNode(Token(value="4", type="NUMB"))

        assert expected_tree == parse(test_src_tokens)

    def test_complex_src(self):
        test_src_tokens = [
            Token(value="1", type="NUMB"),
            Token(value="+", type="PLUS"),
            Token(value="3", type="NUMB"),
            Token(value="*", type="MULT"),
            Token(value="2", type="NUMB"),
            Token(value="-", type="MINUS"),
            Token(value="5", type="NUMB"),
            Token(value="/", type="DIV"),
            Token(value="4", type="NUMB"),
            Token(value="+", type="PLUS"),
            Token(value="7", type="NUMB"),
        ]

        expected_tree = TreeNode(Token("+", "PLUS"))
        expected_tree.left = TreeNode(Token("-", "MINUS"))
        expected_tree.left.left = TreeNode(Token("+", "PLUS"))
        expected_tree.left.left.left = TreeNode(Token("1", "NUMB"))
        expected_tree.left.left.right = TreeNode(Token("*", "MULT"))
        expected_tree.left.left.right.left = TreeNode(Token("3", "NUMB"))
        expected_tree.left.left.right.right = TreeNode(Token("2", "NUMB"))
        expected_tree.left.right = TreeNode(Token("/", "DIV"))
        expected_tree.left.right.left = TreeNode(Token("5", "NUMB"))
        expected_tree.left.right.right = TreeNode(Token("4", "NUMB"))
        expected_tree.right = TreeNode(Token("7", "NUMB"))

        assert expected_tree == parse(test_src_tokens)
