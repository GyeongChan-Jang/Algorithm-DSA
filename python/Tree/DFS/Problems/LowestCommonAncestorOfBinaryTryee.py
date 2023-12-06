# 문제에서 Binary 트리 하나와 해당 트리에 속한 두개의 노드가 주어진다.
# 이 때, 두 노드의 공통 조상중 가낭 낮은 node 즉, the lowest common ancestor(LCA)를 찾아라

# 조건
# 2<= node 개수 <= 10^5
# -10^9 <= Node.val <= 10^9
# 모든 Node.val은 Unique하다.
# p != q
# p, q는 모두 주어진 Tree에 속해 있다.

def LCA(root, p, q):
    if root == None:
        return None

    left = LCA(root, p, q)
    right = LCA(root, p, q)
    if root == p or root == q:
        root
    elif left and right:
        return root
    return left or right
