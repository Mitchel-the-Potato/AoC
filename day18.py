from binarytree import tree, Node
import math

def parse_tree(s):
    stack = []
    for c in s:
        if c == "[":
            stack.append(c)
        elif c == ",":
            pass
        elif c == "]":
            t2 = stack.pop()
            t1 = stack.pop()
            _ = stack.pop()
            assert _ == "["
            t = Node(0)
            t.left = t1
            t.right = t2
            stack.append(t)
        else:
            stack.append(Node(int(c)))
        # for b in stack:
        #     print(b)
    assert len(stack) == 1
    return stack[0]


def find_left_neighbour(root, node):
    leaves = [n for n in root.postorder if n.left is None]
    inds = [i for i, v in enumerate(leaves) if v == node]
    assert len(inds) == 1
    i = inds[0]
    neighbour = leaves[i - 1] if i > 0 else None
    return neighbour


def find_right_neighbour(root, node):
    leaves = [n for n in root.postorder if n.left is None]
    inds = [i for i, v in enumerate(leaves) if v == node]
    assert len(inds) == 1
    i = inds[0]
    neighbour = leaves[i + 1] if i < len(leaves) - 1 else None
    return neighbour

def tree_add(root, another):
    if root is None:
        return another
    a = Node(0)
    a.left = root
    a.right = another
    return a


def tree_explode(root):
    while root.height > 4:
        for parent in root.levels[4]:
            if parent.left is None:
                continue
            else:
                # assert: left / right must have value at same time.
                node_l = parent.left
                nb_l = find_left_neighbour(root, node_l)
                if nb_l:
                    nb_l.value += node_l.value

                node_r = parent.right
                nb_r = find_right_neighbour(root, node_r)
                if nb_r:
                    nb_r.value += node_r.value

                # reset this parent = 0
                parent.left = None
                parent.right = None
                parent.value = 0
            # print(root)
    return root

def tree_split(root):
    leaves = [n for n in root.postorder if n.left is None]
    for leaf in leaves:
        if leaf.value > 9:
            # print(leaf, leaf.left, leaf.right)
            leaf.left = Node(math.floor(leaf.value/2))
            leaf.right = Node(leaf.value - leaf.left.value)
            leaf.value = 0
            # only split first then check explode
            break
    else:
        # no leaf ever
        return root
    root = tree_explode(root)
    if root.max_node_value > 9:
        return tree_split(root)
    else:
        return root

def tree_sum(root):
    if root.left is None:
        return root.value
    else:
        return 3 * tree_sum(root.left) + 2 * tree_sum(root.right)


ss = """[[4,[3,[2,8]]],[[[8,5],4],[[3,5],[4,9]]]]
[[[8,[6,8]],2],[4,[[1,0],[4,5]]]]
[[4,3],[[[3,3],[1,8]],[[0,8],[5,8]]]]
[[[8,[5,8]],[[8,7],[2,1]]],[3,[[0,3],1]]]
[[9,[[9,2],3]],[3,[[9,7],[2,8]]]]
[[[7,[0,0]],[[4,3],[6,3]]],[6,[4,5]]]
[[[[4,2],[0,0]],[4,2]],[[[8,7],8],[[9,4],5]]]
[[4,[1,[1,1]]],[[[0,6],8],[[7,5],[7,3]]]]
[[[1,[9,9]],[4,3]],[[1,[5,8]],9]]
[[2,[6,[6,7]]],[[6,[1,5]],8]]
[4,[[[9,8],[1,3]],[7,[7,4]]]]
[[[[2,6],8],2],[[[2,2],8],[[3,7],8]]]
[[[[1,5],2],[[8,9],[8,3]]],[[[7,3],[1,1]],[[3,7],7]]]
[[[4,4],[8,9]],[5,3]]
[[[[1,4],[4,5]],9],[[2,8],0]]
[[[[4,4],[7,3]],[[9,7],[3,9]]],[9,[5,[5,1]]]]
[[5,[[5,9],6]],[[[5,9],[6,3]],1]]
[[[[1,0],[1,6]],5],[1,9]]
[[[[6,3],[7,2]],1],[[0,6],6]]
[[[3,4],[4,0]],[[[6,4],[2,0]],[7,[7,2]]]]
[[[[1,3],[9,6]],[[1,1],[9,3]]],[[3,8],[[9,5],2]]]
[[[[9,4],6],5],[[[7,6],[2,3]],[6,6]]]
[[6,[2,[0,7]]],[[3,0],[8,[1,9]]]]
[[[6,0],[1,7]],[[[4,2],[5,7]],[[5,0],9]]]
[[[7,[4,9]],0],[[5,[7,5]],[8,[5,1]]]]
[[[[6,1],[8,0]],[3,[4,5]]],[[[8,3],4],[0,2]]]
[[[[3,8],5],[4,8]],9]
[[0,[7,[9,4]]],[2,2]]
[[[[9,6],[4,0]],[1,1]],[3,[[3,6],8]]]
[[[6,[3,3]],[[7,6],3]],[[[2,8],[0,7]],3]]
[[[[3,2],[2,4]],[[8,7],7]],[[[0,2],[1,3]],[8,3]]]
[[[[4,2],[6,8]],6],[[[2,1],[0,3]],[[6,6],[5,6]]]]
[[[[9,0],[1,7]],[[0,3],1]],[[0,[4,3]],7]]
[[[1,[1,4]],1],[[[8,1],9],[[7,1],[7,2]]]]
[2,[2,[[4,2],2]]]
[6,0]
[[[[9,7],7],[2,3]],[[8,[9,4]],[2,3]]]
[[[[4,5],8],6],[5,9]]
[[[5,[6,7]],[[1,9],[8,6]]],7]
[7,[[0,5],4]]
[[[2,4],[2,[1,9]]],[8,[5,6]]]
[3,[[6,[4,8]],[[3,0],9]]]
[[[[4,4],[0,5]],[7,3]],[1,[4,5]]]
[8,[[2,[1,1]],9]]
[[[[5,6],[5,1]],[[7,6],[8,8]]],[2,[[2,1],[3,1]]]]
[[0,[2,[4,6]]],[[[6,0],[3,9]],[0,[1,6]]]]
[[[6,[9,5]],[0,[9,4]]],0]
[[[[5,6],[7,8]],[7,[8,8]]],[[7,[4,7]],[[3,9],7]]]
[1,0]
[[7,2],[9,[3,0]]]
[[[[4,8],9],[1,[0,4]]],[[[5,2],0],8]]
[[[9,[2,5]],[2,[5,8]]],[1,6]]
[[[[0,5],1],[0,4]],7]
[8,[5,9]]
[[[[8,8],[4,8]],[[7,8],7]],[[0,4],8]]
[[[0,6],[9,6]],2]
[[[[2,5],[0,6]],8],[[8,9],1]]
[[[0,9],[1,[1,2]]],[[[4,1],6],7]]
[[[[5,7],[4,6]],[[6,3],[8,2]]],[[[2,5],[0,9]],[5,1]]]
[[[5,0],[[4,5],[6,2]]],[[[1,7],[3,0]],[[8,2],[6,1]]]]
[[[[8,9],9],[9,0]],[4,[[7,2],9]]]
[[[[2,3],[0,5]],[8,8]],[9,[[9,1],8]]]
[[[5,9],[0,[6,2]]],[[3,2],[[1,2],[9,5]]]]
[[[5,2],[8,[0,0]]],[[6,9],[4,[8,4]]]]
[7,3]
[[[6,4],[[0,4],7]],[[5,[0,3]],[8,7]]]
[[1,2],[[3,[5,9]],0]]
[[[6,9],[3,0]],[[[2,1],4],6]]
[[[8,[7,9]],1],[[[2,2],8],8]]
[[[0,1],[6,[3,3]]],5]
[[[[3,9],0],7],2]
[[[3,0],[1,[7,6]]],0]
[[[[3,5],3],8],[[[1,2],[8,8]],[[1,6],[8,1]]]]
[[[9,7],[[1,3],[6,9]]],6]
[[[[1,8],1],[[6,4],[1,8]]],[[[1,7],[5,9]],[[7,0],0]]]
[[[1,[9,3]],[4,0]],7]
[[5,[9,6]],[[4,[0,8]],2]]
[3,[[1,0],[0,2]]]
[[[3,1],[2,7]],[[4,4],5]]
[[8,6],[[4,[5,9]],[[3,7],9]]]
[[[3,2],2],[[3,9],8]]
[[[[4,5],[4,5]],[[0,2],[7,0]]],[[1,4],2]]
[7,[[8,[3,8]],[[5,6],4]]]
[[[[2,8],[2,2]],[[4,4],0]],[[2,[8,0]],2]]
[4,[[[8,8],0],[[1,8],[4,6]]]]
[[[5,[1,2]],7],9]
[[9,[[0,0],9]],[[5,[1,3]],[4,[4,7]]]]
[[3,4],[8,[2,[9,6]]]]
[[[[3,0],1],[[7,6],[5,2]]],[[[9,9],[9,2]],[0,[2,2]]]]
[[[[0,8],[6,1]],[2,0]],[6,[[8,8],[9,1]]]]
[[[5,[1,9]],6],6]
[[[3,5],[[9,9],[2,2]]],[[1,0],4]]
[[4,0],[2,[[8,8],[5,4]]]]
[[6,1],5]
[[[2,[3,7]],0],[1,5]]
[[[[5,9],[5,3]],[6,2]],[[7,9],4]]
[[[5,[0,9]],[[5,6],3]],[3,[7,8]]]
[8,[[[4,6],5],[0,2]]]
[[[0,[6,2]],[6,[6,6]]],[[3,1],6]]
[1,[[6,4],[0,6]]]"""

root = None
for s in ss.split("\n"):
    t = parse_tree(s)
    # print(s)
    root = tree_split(tree_explode(tree_add(root, t)))

print(tree_sum(root))

# Q2
scores = []
for s1 in ss.split("\n"):
    for s2 in ss.split("\n"):
        t1 = parse_tree(s1)
        t2 = parse_tree(s2)
        # TODO: what if t1 == t2?
        scores.append(tree_sum(tree_split(tree_explode(tree_add(t1, t2)))))

# print(scores)
print(max(scores))