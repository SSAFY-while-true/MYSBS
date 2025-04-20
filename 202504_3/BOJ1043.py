import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        if b_root in ture_people:
            parent[a_root] = b_root

        else:
            parent[b_root] = a_root


N, M = map(int, input().split())
ture_people = list(map(int, input().split()))
if ture_people[0] == 0:
    result = M

else:
    ture_people = set(ture_people[1:])

    parent = [x for x in range(N + 1)]
    party = []

    for _ in range(M):
        data = list(map(int, input().split()))
        party.append(data)
        for i in range(1, data[0]):
            union(data[i], data[i+1]) # 이번친구와 옆친구를 유니온 한다

    result = 0
    for party_group in party:
        for i in range(1, party_group[0]+1):
            find(party_group[i])    # 한번더 파인드를 해줘야 내것으로 돌아옴
            if parent[party_group[i]] in ture_people:
                break
        else:
            result += 1

print(result)




