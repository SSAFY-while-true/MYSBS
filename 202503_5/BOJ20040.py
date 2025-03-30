import sys
input = sys.stdin.readline


def find(parent, x):
    while parent[x] != x:           # 재귀가 깊어지면 안되니까 while문으로 수정
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a 
        return True
    
    else:
        return False 
    

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]

parent = [x for x in range(n)]

for i in range(1, m + 1):
    a, b = data[i-1]
    if not union(parent, a, b):
        print(i)
        break

else:
    print(0)

