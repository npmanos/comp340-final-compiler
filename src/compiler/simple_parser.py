import os
from compiler.binarytree import TreeNode
from compiler.simple_tokenizer import Token, tokenize
import logging as log


def parse(srcList: list[Token]) -> TreeNode[Token]:
    if len(srcList) == 1:
        return TreeNode(srcList[0])
    
    log.debug(f'##### srcList = {srcList} #####')
    
    root = op = TreeNode(srcList[1])
    op.left = TreeNode(srcList[0])

    log.debug('op = ')
    log.debug(op)

    right_tree = parse(srcList[2:])

    log.debug('op = ')
    log.debug(op)

    log.debug('right_tree = ')
    log.debug(right_tree)
    
    if op.data.precedence >= right_tree.data.precedence:
        while right_tree is not None and op.data.precedence >= right_tree.data.precedence:
            log.debug(f'--- op ({op.data.value}): {op.data.precedence} >= right_tree ({right_tree.data.value}): {right_tree.data.precedence} ---')

            parent = op.parent

            op.right = right_tree.left

            log.debug('# op.right = right_tree.left')
            log.debug('op = ')
            log.debug(op)

            right_tree.left = op

            log.debug('# right_tree.left = op')
            log.debug('right_tree = ')
            log.debug(right_tree)
            
            if parent is not None:
                parent.left = right_tree
            else:
                root = right_tree

            op = right_tree.left
            right_tree = op.right

        log.debug('root = ')
        log.debug(root)

        log.debug('**** return root ****')
    
        return root

    op.right = right_tree

    log.debug('op = ')
    log.debug(op)

    log.debug('**** return op ****')
    

    return op

if __name__ == '__main__':
    log.basicConfig(level=log.DEBUG)

    os.system('clear')

    test_str = '1 + 3 * 2 - 5 / 4 + 7'
    # test_str = '1 * 3 + 4'
    # test_str = '1 + 3 * 4'

    log.debug(test_str)

    tokens = tokenize(test_str)
    parsed = parse(tokens)

    log.debug(parsed)

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
    
    log.debug('CORRECT ANSWER:')
    log.debug(root)
