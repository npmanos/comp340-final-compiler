# ruff: noqa: F403
# ruff: noqa: F405

from .binarytree import TreeNode
from .simple_tokens import *


class EvaluationError(Exception):
    pass


def evaluate(srcTree: TreeNode[TokenBase]) -> int | float:
    if isinstance(srcTree.data, Number) and srcTree.right is None:
        if srcTree.left is not None and isinstance(srcTree.left.data, PrefixOperator):
            return srcTree.left.data.eval_prefix(operand=float(srcTree.data))
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

    raise EvaluationError
