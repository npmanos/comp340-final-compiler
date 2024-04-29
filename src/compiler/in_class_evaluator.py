from compiler.binarytree import TreeNode


def evaluate(rootNode: TreeNode[list[str]]) -> int | float:
    if rootNode.left is None and rootNode.right is None:
        return int(rootNode.data[0])
    else:
        l = evaluate(rootNode.left) # type: ignore
        r = evaluate(rootNode.right) # type: ignore
        op = rootNode.data[1]

        match op:
            case 'MULT':
                return l * r
            case 'DIV':
                return l / r
            case 'PLUS':
                return l + r
            case 'MINUS':
                return l - r
            case _:
                # Throw error if op doesn't match any of the above
                raise ValueError(f"'op' must be a valid operator! {op=}")

if __name__ == '__main__':
    # 1 * 3 + 4 * 5
    rootNode = TreeNode(['+', 'PLUS'])
    rootNode.left = TreeNode(['*', 'MULT'])
    rootNode.left.left = TreeNode(['1', 'NUMB'])
    rootNode.left.right = TreeNode(['3', 'NUMB'])
    rootNode.right = TreeNode(['*', 'MULT'])
    rootNode.right.left = TreeNode(['4', 'NUMB'])
    rootNode.right.right = TreeNode(['5', 'NUMB'])
    print(f'{evaluate(rootNode)=}')

    # 1 + 3 * 4 + 5
    rootTwo = TreeNode(['+', 'PLUS'])
    rootTwo.left = TreeNode(['1', 'NUMB'])
    rootTwo.right = TreeNode(['+', 'PLUS'])
    rootTwo.right.left = TreeNode(['*', 'MULT'])
    rootTwo.right.left.left = TreeNode(['3', 'NUMB'])
    rootTwo.right.left.right = TreeNode(['4', 'NUMB'])
    rootTwo.right.right = TreeNode(['5', 'NUMB'])
    # print(rootTwo)

    print(f'{evaluate(rootTwo)=}')
