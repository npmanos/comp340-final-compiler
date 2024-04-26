# ruff: noqa: F403
# ruff: noqa: F405

from compiler.binarytree import TreeNode
from compiler.tokens.simple_tokens import *


class EvaluationError(Exception):
    pass


def evaluate(srcTree: TreeNode[TokenBase]) -> float:
    ...
