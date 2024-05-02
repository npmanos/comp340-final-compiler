# ruff: noqa: F403
# ruff: noqa: F405

from .binarytree import TreeNode
from .simple_tokens import *


class EvaluationError(Exception):
    pass


def evaluate(srcTree: TreeNode[TokenBase]) -> float:
    if isinstance(srcTree.data, Number) and srcTree.right is None:
        if srcTree.left is not None and isinstance(srcTree.left.data, PrefixOperator):
            return srcTree.left.data.evaluate(operand=float(srcTree.data))
        else:
            return float(srcTree.data)

    if (
        isinstance(srcTree.data, InfixOperator)
        and srcTree.left is not None
        and srcTree.right is not None
    ):
        return srcTree.data.evaluate(
            left_operand=evaluate(srcTree.left), right_operand=evaluate(srcTree.right)
        )

    raise EvaluationError
