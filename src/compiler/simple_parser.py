import os
from typing import cast
from compiler.binarytree import TreeNode
from compiler.simple_tokenizer import Token, tokenize


def parse(srcList: list[Token]) -> TreeNode[Token]:
    def parse_impl(srcList: list[TreeNode[Token]], last_precedence=-1) -> TreeNode[Token]:
        while len(srcList) > 1:
            left_tree = srcList.pop()

            if last_precedence >= srcList[-1].data.precedence:
                return left_tree
            
            op = srcList.pop()
            right_tree = parse_impl(srcList, op.data.precedence)

            op.left = left_tree
            op.right = right_tree

            srcList.append(op)

        return srcList.pop()
    
    # reverse list because python list implements stack ops backwards
    # and then wrap each token in a tree node
    nodeList = list(map(lambda t: TreeNode(t), srcList[::-1]))

    return parse_impl(nodeList)

if __name__ == '__main__':
    os.system('clear')

    test_str = '1 + 3 * 2 - 5 / 4 + 7'
    # test_str = '1 * 3 + 4'
    # test_str = '1 + 3 * 4'

    print(test_str)

    tokens = tokenize(test_str)
    parsed = parse(tokens)

    print(parsed)

    root = TreeNode('+')
    root.left = TreeNode('-')
    root.left.left = TreeNode('+')
    root.left.left.left = TreeNode('1')
    root.left.left.right = TreeNode('*')
    root.left.left.right.left = TreeNode('3')
    root.left.left.right.right = TreeNode('2')
    root.left.right = TreeNode('/')
    root.left.right.left = TreeNode('5')
    root.left.right.right = TreeNode('4')
    root.right = TreeNode('7')
    
    print('CORRECT ANSWER:')
    print(root)
