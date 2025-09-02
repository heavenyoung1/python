import sys
from sys import stdin

def main():
    sys.setrecursionlimit(1 << 25)
    N, Q = map(int, stdin.readline().split())
    parent = list(range(N + 1))
    rank = [1] * (N + 1)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
            rank[u_root] += rank[v_root]
        else:
            parent[u_root] = v_root
            rank[v_root] += rank[u_root]
        return True

    edges = []
    for _ in range(Q):
        l, r = map(int, stdin.readline().split())
        edges.append((l - 1, r))

    parent = list(range(N + 1))
    rank = [1] * (N + 1)
    count = 0
    for u, v in edges:
        if find(u) != find(v):
            union(u, v)
            count += 1
            if find(0) == find(N):
                print("Yes")
                print(count)
                return

    # After processing all edges, check again
    if find(0) == find(N):
        print("Yes")
        print(count)
    else:
        print("No")

if __name__ == "__main__":
    main()