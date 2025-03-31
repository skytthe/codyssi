from dataclasses import dataclass

input = """ozNxANO | 576690
pYNonIG | 323352
MUantNm | 422646
lOSlxki | 548306
SDJtdpa | 493637
ocWkKQi | 747973
qfSKloT | 967749
KGRZQKg | 661714
JSXfNAJ | 499862
LnDiFPd | 55528
FyNcJHX | 9047
UfWSgzb | 200543
PtRtdSE | 314969
gwHsSzH | 960026
JoyLmZv | 833936

MUantNm | 422646
FyNcJHX | 9047""".split("\n\n")


with open("2025/round15/artifacts_at_atlantis.txt") as f:
    input = f.read().split("\n\n")


artifacts = [s.split(" | ") for s in input[0].splitlines()]
recheck = [s.split(" | ") for s in input[1].splitlines()]


class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, id, name, verbose=False):
        new_node = Node(id, name)
        if self.root is None:
            self.root = new_node
            if verbose:
                print(f"ROOT")
        else:
            self._insert_recursive(self.root, new_node, verbose, path=[])

    def _insert_recursive(self, current, new_node, verbose, path):
        path.append(current.name)
        if new_node.id < current.id:
            if current.left is None:
                current.left = new_node
                if verbose:
                    print(f"{'-'.join(path)}")
            else:
                self._insert_recursive(current.left, new_node, verbose, path)
        else:
            if current.right is None:
                current.right = new_node
                if verbose:
                    print(f"{'-'.join(path)}")
            else:
                self._insert_recursive(current.right, new_node, verbose, path)

    def get_level_nodes(self, level):
        result = []
        self._get_level_nodes_recursive(self.root, level, 0, result)
        return result

    def _get_level_nodes_recursive(self, current, target_level, current_level, result):
        if current is None:
            return
        if current_level == target_level:
            result.append((current.id, current.name))
        else:
            self._get_level_nodes_recursive(
                current.left, target_level, current_level + 1, result)
            self._get_level_nodes_recursive(
                current.right, target_level, current_level + 1, result)

    def get_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, current):
        if current is None:
            return -1
        left_height = self._get_height_recursive(current.left)
        right_height = self._get_height_recursive(current.right)
        return max(left_height, right_height) + 1

    def find_lca(self, id1, id2):
        return self._find_lca_recursive(self.root, id1, id2)

    def _find_lca_recursive(self, current, id1, id2):
        if current is None:
            return None
        if id1 < current.id and id2 < current.id:
            return self._find_lca_recursive(current.left, id1, id2)
        if id1 > current.id and id2 > current.id:
            return self._find_lca_recursive(current.right, id1, id2)
        return current


bst = BST()
for name, id in artifacts:
    # print(f"{id} : {name}")
    bst.insert(int(id), name)


# part 1
print(max(sum(n[0] for n in bst.get_level_nodes(i))
      for i in range(bst.get_height()))*(bst.get_height()+1))

# part 2
bst.insert(int(500000), "part 2", verbose=True)

# part 3
lca = bst.find_lca(int(recheck[0][1]), int(recheck[1][1]))
# print(f"id={lca.id}, name={lca.name}")
print(f"{lca.name}")
