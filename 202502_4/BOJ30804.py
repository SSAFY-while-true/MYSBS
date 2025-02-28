import sys

input = sys.stdin.readline

N = int(input())
tanghulu = list(map(int, input().split()))

max_fruit = 0
a= 0

fruit1 = -1
fruit1_idx = -1
fruit2 = -1
fruit2_idx = -1

for b in range(N):
    if tanghulu[b] == fruit1 or fruit1 == -1:
        fruit1 = tanghulu[b]
        fruit1_idx = b
    elif tanghulu[b] == fruit2 or fruit2 == -1:
        fruit2 = tanghulu[b]
        fruit2_idx = b
    
    else:
        if fruit1_idx < fruit2_idx:
            a = fruit1_idx + 1
            fruit1 = tanghulu[b]
            fruit1_idx = b
        else:
            a = fruit2_idx + 1
            fruit2 = tanghulu[b]
            fruit2_idx = b

    max_fruit = max(max_fruit, b-a+1)

print(max_fruit)