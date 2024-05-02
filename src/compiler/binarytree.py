from typing import Generic, TypeVar
from PrettyPrint import PrettyPrintTree


T = TypeVar("T", covariant=True)


class TreeNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, TreeNode)
            and (self.data == value.data)
            and (self.left == value.left)
            and (self.right == value.right)
        )

    @property
    def _children(self) -> list["TreeNode[T]"]:
        child_list = []
        if self.left is not None:
            child_list.append(self.left)
        if self.right is not None:
            child_list.append(self.right)

        return child_list

    def __str__(self) -> str:
        def get_children(node: TreeNode[T]) -> list["TreeNode[T]"]:
            return node._children

        def get_val(node: TreeNode[T]) -> str:
            return str(node.data)

        pt = PrettyPrintTree(
            get_children=get_children, get_val=get_val, return_instead_of_print=True
        )  # type: ignore

        return "\n" + str(pt(self))  # type: ignore

    def __repr__(self) -> str:
        return f'TreeNode(data={repr(self.data)}{"" if self.left is None else ", left=" + repr(self.left)}{"" if self.right is None else ", right=" + repr(self.right)})'


if __name__ == "__main__":
    __package__ = __package__ or "compiler"

    node = TreeNode("+")
    node.left = TreeNode("1")
    node.right = TreeNode("3")

    print(node)
