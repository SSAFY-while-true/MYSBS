n, d = map(int, input().split())

pedigree = list(map(int, input().split()))
child_count = [0] * (n + 1)
result_count = 0

for ancestor in pedigree:
    child_count[ancestor] += 1

for child in child_count:
    # 최대한 크게 집고
    # 집은만큼 빼고 뭉탱이니까 1더하고 즉 d-1만큼 빼줘 그리고 카운트를 샌다
    while child > d:
        result_count += 1
        child = child - d + 1

print(result_count)