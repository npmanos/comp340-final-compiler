from PrettyPrint import PrettyPrintTree


class TreeNode[T]:
    def __init__(self, data: T) -> None:
        self.data = data
        self.parent: TreeNode[T] | None = None
        self._left: TreeNode[T] | None = None
        self._right: TreeNode[T] | None = None

    @property
    def left(self) -> "TreeNode[T] | None":
        return self._left

    @left.setter
    def left(self, value: "TreeNode[T] | None") -> None:
        self._left = value

        if self._left is not None:
            self._left.parent = self

    @property
    def right(self) -> "TreeNode[T] | None":
        return self._right

    @right.setter
    def right(self, value: "TreeNode[T] | None") -> None:
        self._right = value

        if self._right is not None:
            self._right.parent = self

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

        return pt(self)  # type: ignore


if __name__ == "__main__":
    __package__ = __package__ or 'compiler'

    node = TreeNode("+")
    node.left = TreeNode("1")
    node.right = TreeNode("3")

    print(node)
