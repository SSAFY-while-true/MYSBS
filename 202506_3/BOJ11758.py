p_1 = list(map(int, input().split()))
p_2 = list(map(int, input().split()))
p_3 = list(map(int, input().split()))

left = (p_2[1] - p_1[1]) * (p_3[0] - p_2[0])
right = (p_3[1] - p_2[1]) * (p_2[0] - p_1[0])

if left == right:
    print(0)
elif left > right:
    print(-1)
else:
    print(1)