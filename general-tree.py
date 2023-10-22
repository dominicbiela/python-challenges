from typing import TypeAlias, Optional

TreeNode: TypeAlias = 'TreeNode'


class TreeNode:
    def __init__(self, data: str, property: Optional[str] = None):
        self.data = data
        self.property = property
        self.children = []
        self.parent = None

    def add_child(self, child: TreeNode):
        if child in self.children:
            print('Child already present in Tree')
        else:
            self.children.append(child)
        child.parent = self

    def find_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, type: Optional[str] = None):
        if type == 'both' and self.data and self.property:
            value = self.data + ' (' + self.property + ')'
        elif type == 'name' and self.data:
            value = self.data
        elif type == 'property' and self.property:
            value = self.property
        elif type == 'property' and not self.property or type == 'both' and not self.property:
            return print('Need to set property')
        else:
            value = self.data

        spaces = '   ' * self.find_level()
        prefix = spaces + '->' if self.parent else ''
        print(prefix + value)
        for child in self.children:
            child.print_tree(type)


def build_electronic_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Apple'))
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('ThinkPad'))

    mobile = TreeNode('Mobile')
    mobile.add_child(TreeNode('iPhone'))
    mobile.add_child(TreeNode('Samsung'))
    mobile.add_child(TreeNode('Google Plus'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Toshiba'))
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    return root

def build_work_tree():
    root = TreeNode('Dominic', 'CEO')
    cto = TreeNode('David', 'CTO')
    infra_head = TreeNode('Noah', 'Infrastructure Head')
    infra_head.add_child(TreeNode('Alex', 'Cloud Manager'))
    infra_head.add_child(TreeNode('Emma', 'App Manager'))
    cto.add_child(TreeNode('James', 'Application Head'))
    cto.add_child(infra_head)

    hr_head = TreeNode('Lucy','HR Head')
    hr_head.add_child(TreeNode('Julie', 'Recruitment Manager'))
    hr_head.add_child(TreeNode('Sophia', 'Policy Manager'))

    coo = TreeNode('Alicia', 'COO')
    coo.add_child(TreeNode('Tristan', 'Director'))

    root.add_child(cto)
    root.add_child(hr_head)
    root.add_child(coo)

    return root


if __name__ == '__main__':
    root_node = build_work_tree()
    root_node.print_tree('both')
    root_node.print_tree('name')
    root_node.print_tree('property')
