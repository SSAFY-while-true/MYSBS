N, r, c = map(int, input().split())


answer = 0
size = 2 ** N

while size > 1:
    size //= 2

    if r < size and c < size:
        continue

    elif r < size and c >= size:
        answer += size * size
        c -= size

    elif r >= size and c < size:

        answer += 2 * size * size
        r -= size

    else:

        answer += 3 * size * size
        r -= size
        c -= size

print(answer)