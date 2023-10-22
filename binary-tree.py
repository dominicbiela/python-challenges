from typing import Optional


class BinarySearchTreeNode:
    def __init__(self,
                 data: int,
                 left: Optional['BinarySearchTreeNode'] = None,
                 right: Optional['BinarySearchTreeNode'] = None):
        self.data = data
        self.left = left
        self.right = right

    def add_child(self, data: int):
        # Can't contain duplicates
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self) -> list[int]:
        elements = []
        # Left side first
        if self.left:
            elements += self.left.in_order_traversal()
        # Root node
        elements.append(self.data)
        # Right side last
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value: int) -> bool:
        if value == self.data:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def delete(self, value: int):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def treeSum(self):
        if self is None:
            return 0
        else:
            leftsum = self.left.treeSum() if self.left else 0
            rightsum = self.right.treeSum()  if self.right else 0
            return self.data + leftsum + rightsum


def build_tree(elements: list[int]) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.search(200))
    print(number_tree.find_min())
    print(number_tree.find_max())
    print(number_tree.treeSum())
    numToDel = 20
    number_tree.delete(numToDel)
    print(f'After deleting {numToDel}', number_tree.in_order_traversal())
    numToDel = 9
    number_tree.delete(numToDel)
    print(f'After deleting {numToDel}', number_tree.in_order_traversal())
    numToDel = 17
    number_tree.delete(numToDel)
    print(f'After deleting {numToDel}', number_tree.in_order_traversal())