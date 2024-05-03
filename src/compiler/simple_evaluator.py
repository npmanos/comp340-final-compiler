# ruff: noqa: F403
# ruff: noqa: F405

from functools import reduce

from .binarytree import TreeNode, treedata_isinstance
from .simple_tokens import *


class EvaluationError(SyntaxError):
    pass


def evaluate(srcTree: TreeNode[TokenBase]) -> NumberType:
    if isinstance(srcTree.data, Number) and srcTree.right is None:
        if srcTree.left is not None and treedata_isinstance(
            srcTree.left, PrefixOperator
        ):
            negation_stack: list[TreeNode[PrefixOperator]] = [srcTree.left]

            while negation_stack[-1].left is not None:
                if (
                    not treedata_isinstance(negation_stack[-1].left, PrefixOperator)
                    or negation_stack[-1].right is not None
                ):
                    raise EvaluationError(f'Unable to evaluate {srcTree.data}')

                negation_stack.append(negation_stack[-1].left)

            return reduce(
                lambda val, pre_op: pre_op.data.eval_prefix(val),
                negation_stack,
                int(srcTree.data),
            )
        else:
            return int(srcTree.data)

    if (
        isinstance(srcTree.data, InfixOperator)
        and srcTree.left is not None
        and srcTree.right is not None
    ):
        return srcTree.data.eval_infix(
            left_operand=evaluate(srcTree.left), right_operand=evaluate(srcTree.right)
        )

    raise EvaluationError(f'Unable to evaluate {srcTree.data}')
