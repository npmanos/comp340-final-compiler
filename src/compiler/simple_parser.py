# ruff: noqa: F403, F405


from .binarytree import TreeNode
from .simple_tokens import *


def parse(srcList: list[TokenBase]) -> TreeNode[TokenBase]:
    def parse_impl(
        srcList: list[TreeNode[TokenBase]], last_precedence=-1
    ) -> TreeNode[TokenBase]:
        while len(srcList) > 1:
            left_tree = srcList.pop()

            if (
                isinstance(left_tree.data, Minus)
                and (left_tree.left is None or isinstance(left_tree.left.data, Minus))
                and left_tree.right is None
            ):
                negated_token = srcList.pop()
                negated_token.left = left_tree
                srcList.append(negated_token)
                continue

            if isinstance(left_tree.data, LeftParen):
                paren_count = 1
                sub_list: list[TreeNode[TokenBase]] = []

                while paren_count > 0:
                    token = srcList.pop()

                    if isinstance(token.data, LeftParen):
                        paren_count += 1
                        sub_list.append(token)
                    elif isinstance(token.data, RightParen):
                        paren_count -= 1
                        if paren_count > 0:
                            sub_list.append(token)
                    else:
                        sub_list.append(token)

                bracketed = parse_impl(sub_list[::-1])

                if left_tree.left is not None and isinstance(
                    left_tree.left.data, Minus
                ):
                    negated_bracketed: TreeNode[TokenBase] = TreeNode(Mult())
                    negated_bracketed.left = TreeNode(Number("1"))
                    negated_bracketed.left.left = left_tree.left
                    negated_bracketed.right = bracketed

                    srcList.append(negated_bracketed)
                    continue

                srcList.append(bracketed)
                continue

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
